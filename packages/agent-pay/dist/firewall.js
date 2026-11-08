"use strict";
/**
 * HAICHAIN Autonomous Financial Firewall & Bounded Loss Engine for Node.js / TypeScript
 * 1-Click Budget Invariant Protection & Anti-Prompt Injection Defense.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.haichain_firewall = exports.firewall = exports.HaiChainFirewall = void 0;
function extractPromptCandidate(arg) {
    if (!arg)
        return '';
    if (typeof arg === 'string')
        return arg;
    if (typeof arg === 'object') {
        const keys = ['prompt', 'input', 'query', 'task', 'message', 'content', 'user_input'];
        for (const key of keys) {
            if (typeof arg[key] === 'string')
                return arg[key];
        }
        for (const val of Object.values(arg)) {
            if (typeof val === 'string')
                return val;
        }
    }
    return '';
}
class HaiChainFirewall {
    spentToday = 0;
    lastResetTime = Date.now();
    defaultDailyCap;
    defaultPerCallCap;
    parentFirewall;
    delegatedBudgetsTotal = 0;
    subAgents = new Map();
    static ADVERSARIAL_PATTERNS = [
        /ignore\s+(all\s+)?(previous|prior)\s+instructions?/i,
        /transfer\s+(all|entire|remaining)\s+(balance|funds?|usdt|usdc|sol)/i,
        /drain\s+(the\s+)?(wallet|vault|treasury)/i,
        /send\s+(all\s+)?tokens?\s+to\s+0x[a-fA-F0-9]{40}/i,
        /send\s+(all\s+)?tokens?\s+to\s+[1-9A-HJ-NP-Za-km-z]{32,44}/i,
        /bypass\s+security\s+filter/i,
    ];
    constructor(options = {}) {
        this.defaultDailyCap = options.defaultDailyCap || 50.0;
        this.defaultPerCallCap = options.defaultPerCallCap || 1.0;
    }
    checkAndResetDaily() {
        const now = Date.now();
        if (now - this.lastResetTime >= 86400 * 1000) {
            this.spentToday = 0;
            this.lastResetTime = now;
        }
    }
    checkAdversarialPrompt(prompt) {
        if (!prompt || typeof prompt !== 'string')
            return;
        for (const pattern of HaiChainFirewall.ADVERSARIAL_PATTERNS) {
            if (pattern.test(prompt)) {
                throw new Error('[HaiChainFirewall] Malicious prompt injection pattern detected! Immediate circuit breaker activated.');
            }
        }
    }
    getSpentToday() {
        this.checkAndResetDaily();
        return this.spentToday;
    }
    getAvailableBudget() {
        this.checkAndResetDaily();
        return Math.max(0, this.defaultDailyCap - this.spentToday - this.delegatedBudgetsTotal);
    }
    /**
     * Hierarchical Sub-Agent Swarm Delegation (CrewAI / LangGraph / AutoGen support).
     * Partitions a bounded sub-budget from the parent agent to a sub-agent without requiring
     * human user re-authentication or repeated FaceID prompts.
     * Guarantees Bounded Loss Invariant: sum(child_budgets) <= parent_daily_cap - parent_spent.
     */
    delegateSubAgent(subAgentId, options) {
        if (!options.allocatedBudget || options.allocatedBudget <= 0) {
            throw new Error(`[HaiChainFirewall] Allocated budget for sub-agent must be > 0`);
        }
        const available = this.getAvailableBudget();
        if (options.allocatedBudget > available) {
            throw new Error(`[HaiChainFirewall] Hierarchical delegation error: Cannot delegate $${options.allocatedBudget.toFixed(4)} to sub-agent '${subAgentId}'. Available unallocated budget is only $${available.toFixed(4)}.`);
        }
        this.delegatedBudgetsTotal += options.allocatedBudget;
        const child = new HaiChainFirewall({
            defaultDailyCap: options.allocatedBudget,
            defaultPerCallCap: options.maxPerCall ?? Math.min(options.allocatedBudget, this.defaultPerCallCap)
        });
        child.parentFirewall = this;
        this.subAgents.set(subAgentId, child);
        return child;
    }
    recordSpend(amount, dailyCap, perCallCap) {
        this.checkAndResetDaily();
        if (amount > perCallCap) {
            throw new Error(`[HaiChainFirewall] Transaction amount $${amount.toFixed(4)} exceeds per-call cap $${perCallCap.toFixed(4)}!`);
        }
        if (this.spentToday + amount > dailyCap) {
            throw new Error(`[HaiChainFirewall] Cumulative spend ($${(this.spentToday + amount).toFixed(4)}) exceeds daily cap $${dailyCap.toFixed(4)}!`);
        }
        this.spentToday += amount;
        if (this.parentFirewall) {
            this.parentFirewall.recordChildSpend(amount);
        }
    }
    recordChildSpend(amount) {
        this.checkAndResetDaily();
        this.spentToday += amount;
        this.delegatedBudgetsTotal = Math.max(0, this.delegatedBudgetsTotal - amount);
        if (this.parentFirewall) {
            this.parentFirewall.recordChildSpend(amount);
        }
    }
    /**
     * Releases unspent allocated budget back to the parent agent.
     * Enables immediate recycling of sub-agent funds upon task completion in LangGraph / CrewAI swarms.
     */
    releaseToParent() {
        if (!this.parentFirewall)
            return 0;
        this.checkAndResetDaily();
        const unspent = Math.max(0, this.defaultDailyCap - this.spentToday);
        this.parentFirewall.reclaimDelegatedBudget(unspent);
        this.defaultDailyCap = this.spentToday; // Lock current sub-agent cap to spent amount
        return unspent;
    }
    reclaimDelegatedBudget(unspentAmount) {
        this.checkAndResetDaily();
        this.delegatedBudgetsTotal = Math.max(0, this.delegatedBudgetsTotal - unspentAmount);
        if (this.parentFirewall) {
            this.parentFirewall.reclaimDelegatedBudget(unspentAmount);
        }
    }
    /**
     * Wraps an async function or agent task with deterministic firewall bounds.
     */
    protect(options, fn) {
        const dailyCap = options.dailyCap ?? options.maxDailyBudget ?? this.defaultDailyCap;
        const perCallCap = options.perCallCap ?? options.maxPerCall ?? this.defaultPerCallCap;
        const anomalyKill = options.anomalyKill !== false;
        const callCost = options.callCost ?? 0.001;
        // Direct function wrapper
        if (fn) {
            return async (...args) => {
                const promptCandidate = extractPromptCandidate(args[0]);
                if (anomalyKill && promptCandidate) {
                    this.checkAdversarialPrompt(promptCandidate);
                }
                this.recordSpend(callCost, dailyCap, perCallCap);
                return await fn(...args);
            };
        }
        // Middleware or higher-order wrapper
        return (targetFn) => {
            return async (...args) => {
                const promptCandidate = extractPromptCandidate(args[0]);
                if (anomalyKill && promptCandidate) {
                    this.checkAdversarialPrompt(promptCandidate);
                }
                this.recordSpend(callCost, dailyCap, perCallCap);
                return await targetFn(...args);
            };
        };
    }
    /**
     * Express / Connect middleware for API protection
     */
    middleware(options = {}) {
        const dailyCap = options.dailyCap ?? options.maxDailyBudget ?? this.defaultDailyCap;
        const perCallCap = options.perCallCap ?? options.maxPerCall ?? this.defaultPerCallCap;
        const callCost = options.callCost ?? 0.001;
        return (req, res, next) => {
            try {
                const promptCandidate = extractPromptCandidate(req.body);
                if (promptCandidate) {
                    this.checkAdversarialPrompt(promptCandidate);
                }
                this.recordSpend(callCost, dailyCap, perCallCap);
                next();
            }
            catch (err) {
                res.status(403).json({ error: err.message, blockedBy: 'HaiChainFirewall' });
            }
        };
    }
}
exports.HaiChainFirewall = HaiChainFirewall;
exports.firewall = new HaiChainFirewall();
exports.haichain_firewall = exports.firewall;
