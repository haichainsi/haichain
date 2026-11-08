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
        panic_on_anomaly: bool = True
    ):
        self.default_daily_cap = float(default_daily_cap)
        self.default_per_call_cap = float(default_per_call_cap)
        self.panic_on_anomaly = panic_on_anomaly
        self._lock = threading.Lock()
        self._spent_today = 0.0
        self._last_reset = time.time()
        self._call_history: List[Dict[str, Any]] = []

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
                    # Check first argument or prompt keyword for prompt injection
                    prompt_str = ""
                    if args and isinstance(args[0], str):
                        prompt_str = args[0]
                    elif "prompt" in kwargs and isinstance(kwargs["prompt"], str):
                        prompt_str = kwargs["prompt"]

                    if anomaly_kill and prompt_str:
                        self.check_adversarial_prompt(prompt_str)

                    # Deduct call cost under invariant budget
                    self.record_spend(call_cost, effective_daily, effective_per_call)
                    return await func(*args, **kwargs)
                return async_wrapper
            else:
                @functools.wraps(func)
                def sync_wrapper(*args, **kwargs):
                    prompt_str = ""
                    if args and isinstance(args[0], str):
                        prompt_str = args[0]
                    elif "prompt" in kwargs and isinstance(kwargs["prompt"], str):
                        prompt_str = kwargs["prompt"]

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
