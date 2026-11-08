/**
 * HAICHAIN Autonomous Financial Firewall & Bounded Loss Engine for Node.js / TypeScript
 * 1-Click Budget Invariant Protection & Anti-Prompt Injection Defense.
 */
export interface FirewallOptions {
    maxDailyBudget?: number;
    maxPerCall?: number;
    dailyCap?: number;
    perCallCap?: number;
    allowedMerchants?: string[];
    anomalyKill?: boolean;
    callCost?: number;
}
export interface SubAgentDelegationOptions {
    allocatedBudget: number;
    maxPerCall?: number;
    allowedMerchants?: string[];
    expiresInSeconds?: number;
}
export declare class HaiChainFirewall {
    private spentToday;
    private lastResetTime;
    private defaultDailyCap;
    private defaultPerCallCap;
    private parentFirewall?;
    private delegatedBudgetsTotal;
    private subAgents;
    private static ADVERSARIAL_PATTERNS;
    constructor(options?: {
        defaultDailyCap?: number;
        defaultPerCallCap?: number;
    });
    private checkAndResetDaily;
    checkAdversarialPrompt(prompt: string): void;
    getSpentToday(): number;
    getAvailableBudget(): number;
    /**
     * Hierarchical Sub-Agent Swarm Delegation (CrewAI / LangGraph / AutoGen support).
     * Partitions a bounded sub-budget from the parent agent to a sub-agent without requiring
     * human user re-authentication or repeated FaceID prompts.
     * Guarantees Bounded Loss Invariant: sum(child_budgets) <= parent_daily_cap - parent_spent.
     */
    delegateSubAgent(subAgentId: string, options: SubAgentDelegationOptions): HaiChainFirewall;
    recordSpend(amount: number, dailyCap: number, perCallCap: number): void;
    protected recordChildSpend(amount: number): void;
    /**
     * Releases unspent allocated budget back to the parent agent.
     * Enables immediate recycling of sub-agent funds upon task completion in LangGraph / CrewAI swarms.
     */
    releaseToParent(): number;
    protected reclaimDelegatedBudget(unspentAmount: number): void;
    /**
     * Wraps an async function or agent task with deterministic firewall bounds.
     */
    protect<T extends (...args: any[]) => Promise<any>>(options: FirewallOptions, fn?: T): any;
    /**
     * Express / Connect middleware for API protection
     */
    middleware(options?: FirewallOptions): (req: any, res: any, next: () => void) => void;
}
export declare const firewall: HaiChainFirewall;
export declare const haichain_firewall: HaiChainFirewall;
