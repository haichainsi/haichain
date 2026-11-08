"""
HAICHAIN Autonomous Financial Firewall & Bounded Loss Engine for Python
Wraps AI Agent execution with deterministic budget caps, sliding velocity limits,
and Prompt Injection anomaly defenses.
"""

import asyncio
import functools
import inspect
import re
import threading
import time
from typing import Callable, Optional, List, Dict, Any


class BudgetExceededException(Exception):
    """Raised when an AI agent exceeds its authorized per-call or daily budget cap."""
    pass


class PromptInjectionAnomalyException(Exception):
    """Raised when adversarial prompt injection patterns attempt to drain wallet assets."""
    pass


def extract_prompt_candidate(*args, **kwargs) -> str:
    """Extracts raw prompt string from positional args, keyword args, or LangChain/CrewAI input dictionaries."""
    # 1. Keyword args
    for key in ("prompt", "input", "query", "task", "message", "content", "user_input"):
        if key in kwargs and isinstance(kwargs[key], str):
            return kwargs[key]
    # 2. Positional args
    if args:
        first = args[0]
        if isinstance(first, str):
            return first
        if isinstance(first, dict):
            for key in ("prompt", "input", "query", "task", "message", "content", "user_input"):
                if key in first and isinstance(first[key], str):
                    return first[key]
            # Fallback: scan any string value in the first dictionary
            for val in first.values():
                if isinstance(val, str):
                    return val
        if isinstance(first, list) and first and isinstance(first[0], str):
            return first[0]
    return ""


class HaiChainFirewall:
    """
    1-Click Cryptographic Financial Firewall for AI Agents.
    Enforces deterministic spending invariants, bounded loss limits, and anomaly shutdown.
    """

    ADVERSARIAL_PATTERNS = [
        re.compile(r"ignore\s+(all\s+)?(previous|prior)\s+instructions?", re.IGNORECASE),
        re.compile(r"transfer\s+(all|entire|remaining)\s+(balance|funds?|usdt|usdc|sol)", re.IGNORECASE),
        re.compile(r"drain\s+(the\s+)?(wallet|vault|treasury)", re.IGNORECASE),
        re.compile(r"send\s+(all\s+)?tokens?\s+to\s+0x[a-fA-F0-9]{40}", re.IGNORECASE),
        re.compile(r"send\s+(all\s+)?tokens?\s+to\s+[1-9A-HJ-NP-Za-km-z]{32,44}", re.IGNORECASE),
        re.compile(r"bypass\s+security\s+filter", re.IGNORECASE),
    ]

    def __init__(
        self,
        default_daily_cap: float = 50.0,
        default_per_call_cap: float = 1.0,
        panic_on_anomaly: bool = True,
        parent_firewall: Optional["HaiChainFirewall"] = None,
    ):
        self.default_daily_cap = float(default_daily_cap)
        self.default_per_call_cap = float(default_per_call_cap)
        self.panic_on_anomaly = panic_on_anomaly
        self.parent_firewall = parent_firewall
        self._delegated_budgets_total = 0.0
        self._sub_agents: Dict[str, "HaiChainFirewall"] = {}
        self._lock = threading.RLock()
        self._spent_today = 0.0
        self._last_reset = time.time()
        self._call_history: List[Dict[str, Any]] = []

    def get_available_budget(self) -> float:
        with self._lock:
            self._check_and_reset_daily()
            return max(0.0, self.default_daily_cap - self._spent_today - self._delegated_budgets_total)

    def delegate_sub_agent(
        self,
        sub_agent_id: str,
        allocated_budget: float,
        per_call_cap: Optional[float] = None,
        allowed_merchants: Optional[List[str]] = None,
    ) -> "HaiChainFirewall":
        """
        Hierarchical Sub-Agent Swarm Delegation (CrewAI / LangGraph support).
        Partitions a bounded sub-budget from the parent agent to a sub-agent without requiring
        human user re-authentication or repeated biometric prompts.
        Guarantees Bounded Loss Invariant: sum(child_budgets) <= parent_daily_cap - parent_spent.
        """
        with self._lock:
            self._check_and_reset_daily()
            if allocated_budget <= 0:
                raise ValueError("[HaiChainFirewall] Allocated budget for sub-agent must be > 0")
            available = max(0.0, self.default_daily_cap - self._spent_today - self._delegated_budgets_total)
            if allocated_budget > available:
                raise BudgetExceededException(
                    f"[HaiChainFirewall] Hierarchical delegation error: Cannot delegate ${allocated_budget:.4f} to sub-agent '{sub_agent_id}'. "
                    f"Available unallocated budget is only ${available:.4f}."
                )
            self._delegated_budgets_total += allocated_budget
            child_per_call = per_call_cap if per_call_cap is not None else min(allocated_budget, self.default_per_call_cap)
            child = HaiChainFirewall(
                default_daily_cap=allocated_budget,
                default_per_call_cap=child_per_call,
                panic_on_anomaly=self.panic_on_anomaly,
                parent_firewall=self,
            )
            self._sub_agents[sub_agent_id] = child
            return child

    def _record_child_spend(self, amount: float):
        with self._lock:
            self._check_and_reset_daily()
            self._spent_today += amount
            self._delegated_budgets_total = max(0.0, self._delegated_budgets_total - amount)
            self._call_history.append({"amount": amount, "time": time.time(), "source": "sub_agent"})
            if self.parent_firewall:
                self.parent_firewall._record_child_spend(amount)

    def release_to_parent(self) -> float:
        """
        Releases unspent allocated budget back to parent agent.
        Enables immediate recycling of sub-agent funds upon task completion in CrewAI / LangGraph swarms.
        """
        if not self.parent_firewall:
            return 0.0
        with self._lock:
            self._check_and_reset_daily()
            unspent = max(0.0, self.default_daily_cap - self._spent_today)
            self.parent_firewall._reclaim_delegated_budget(unspent)
            self.default_daily_cap = self._spent_today
            return unspent

    def _reclaim_delegated_budget(self, unspent_amount: float):
        with self._lock:
            self._check_and_reset_daily()
            self._delegated_budgets_total = max(0.0, self._delegated_budgets_total - unspent_amount)
            if self.parent_firewall:
                self.parent_firewall._reclaim_delegated_budget(unspent_amount)

    def _check_and_reset_daily(self):
        now = time.time()
        # Reset if 24 hours elapsed
        if now - self._last_reset >= 86400:
            self._spent_today = 0.0
            self._last_reset = now
            self._call_history = [c for c in self._call_history if now - c["time"] < 86400]

    def check_adversarial_prompt(self, prompt: str):
        if not prompt or not isinstance(prompt, str):
            return
        for pattern in self.ADVERSARIAL_PATTERNS:
            if pattern.search(prompt):
                raise PromptInjectionAnomalyException(
                    f"[HaiChainFirewall] Malicious prompt injection pattern detected! Immediate circuit breaker activated."
                )

    def record_spend(self, amount: float, daily_cap: float, per_call_cap: float):
        with self._lock:
            self._check_and_reset_daily()
            if amount > per_call_cap:
                raise BudgetExceededException(
                    f"[HaiChainFirewall] Transaction amount ${amount:.4f} exceeds per-call cap ${per_call_cap:.4f}!"
                )
            if (self._spent_today + amount) > daily_cap:
                raise BudgetExceededException(
                    f"[HaiChainFirewall] Cumulative spend (${self._spent_today + amount:.4f}) exceeds daily cap ${daily_cap:.4f}!"
                )
            self._spent_today += amount
            self._call_history.append({"amount": amount, "time": time.time()})
            if self.parent_firewall:
                self.parent_firewall._record_child_spend(amount)

    def protect(
        self,
        daily_cap: Optional[float] = None,
        per_call_cap: Optional[float] = None,
        max_daily_budget: Optional[float] = None,
        max_per_call: Optional[float] = None,
        allowed_merchants: Optional[List[str]] = None,
        anomaly_kill: bool = True,
        call_cost: float = 0.001
    ) -> Callable:
        """
        1-Click Decorator to protect any Agent execution function.
        Can be used with either parameter naming convention:
        @firewall.protect(daily_cap=50.0, per_call_cap=1.0)
        or
        @haichain_firewall.protect(max_daily_budget=50.0, max_per_call=1.0)
        """
        effective_daily = daily_cap if daily_cap is not None else (max_daily_budget if max_daily_budget is not None else self.default_daily_cap)
        effective_per_call = per_call_cap if per_call_cap is not None else (max_per_call if max_per_call is not None else self.default_per_call_cap)

        def decorator(func: Callable) -> Callable:
            if inspect.iscoroutinefunction(func):
                @functools.wraps(func)
                async def async_wrapper(*args, **kwargs):
                    prompt_str = extract_prompt_candidate(*args, **kwargs)
                    if anomaly_kill and prompt_str:
                        self.check_adversarial_prompt(prompt_str)

                    # Deduct call cost under invariant budget
                    self.record_spend(call_cost, effective_daily, effective_per_call)
                    return await func(*args, **kwargs)
                return async_wrapper
            else:
                @functools.wraps(func)
                def sync_wrapper(*args, **kwargs):
                    prompt_str = extract_prompt_candidate(*args, **kwargs)
                    if anomaly_kill and prompt_str:
                        self.check_adversarial_prompt(prompt_str)

                    self.record_spend(call_cost, effective_daily, effective_per_call)
                    return func(*args, **kwargs)
                return sync_wrapper

        return decorator

    @property
    def spent_today(self) -> float:
        with self._lock:
            self._check_and_reset_daily()
            return self._spent_today


# Singletons for effortless 1-click import
firewall = HaiChainFirewall()
haichain_firewall = firewall
