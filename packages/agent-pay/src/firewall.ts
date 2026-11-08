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

export class HaiChainFirewall {
  private spentToday: number = 0;
  private lastResetTime: number = Date.now();
  private defaultDailyCap: number;
  private defaultPerCallCap: number;

  private static ADVERSARIAL_PATTERNS = [
    /ignore\s+(all\s+)?(previous|prior)\s+instructions?/i,
    /transfer\s+(all|entire|remaining)\s+(balance|funds?|usdt|usdc|sol)/i,
    /drain\s+(the\s+)?(wallet|vault|treasury)/i,
    /send\s+(all\s+)?tokens?\s+to\s+0x[a-fA-F0-9]{40}/i,
    /send\s+(all\s+)?tokens?\s+to\s+[1-9A-HJ-NP-Za-km-z]{32,44}/i,
    /bypass\s+security\s+filter/i,
  ];

  constructor(options: { defaultDailyCap?: number; defaultPerCallCap?: number } = {}) {
    this.defaultDailyCap = options.defaultDailyCap || 50.0;
    this.defaultPerCallCap = options.defaultPerCallCap || 1.0;
  }

  private checkAndResetDaily(): void {
    const now = Date.now();
    if (now - this.lastResetTime >= 86400 * 1000) {
      this.spentToday = 0;
      this.lastResetTime = now;
    }
  }

  public checkAdversarialPrompt(prompt: string): void {
    if (!prompt || typeof prompt !== 'string') return;
    for (const pattern of HaiChainFirewall.ADVERSARIAL_PATTERNS) {
      if (pattern.test(prompt)) {
        throw new Error(
          '[HaiChainFirewall] Malicious prompt injection pattern detected! Immediate circuit breaker activated.'
        );
      }
    }
  }

  public recordSpend(amount: number, dailyCap: number, perCallCap: number): void {
    this.checkAndResetDaily();
    if (amount > perCallCap) {
      throw new Error(
        `[HaiChainFirewall] Transaction amount $${amount.toFixed(4)} exceeds per-call cap $${perCallCap.toFixed(4)}!`
      );
    }
    if (this.spentToday + amount > dailyCap) {
      throw new Error(
        `[HaiChainFirewall] Cumulative spend ($${(this.spentToday + amount).toFixed(4)}) exceeds daily cap $${dailyCap.toFixed(4)}!`
      );
    }
    this.spentToday += amount;
  }

  /**
   * Wraps an async function or agent task with deterministic firewall bounds.
   */
  public protect<T extends (...args: any[]) => Promise<any>>(
    options: FirewallOptions,
    fn?: T
  ): any {
    const dailyCap = options.dailyCap ?? options.maxDailyBudget ?? this.defaultDailyCap;
    const perCallCap = options.perCallCap ?? options.maxPerCall ?? this.defaultPerCallCap;
    const anomalyKill = options.anomalyKill !== false;
    const callCost = options.callCost ?? 0.001;

    // Direct function wrapper
    if (fn) {
      return async (...args: any[]) => {
        const promptCandidate = typeof args[0] === 'string' ? args[0] : (args[0]?.prompt || '');
        if (anomalyKill && promptCandidate) {
          this.checkAdversarialPrompt(promptCandidate);
        }
        this.recordSpend(callCost, dailyCap, perCallCap);
        return await fn(...args);
      };
    }

    // Middleware or higher-order wrapper
    return (targetFn: T) => {
      return async (...args: any[]) => {
        const promptCandidate = typeof args[0] === 'string' ? args[0] : (args[0]?.prompt || '');
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
  public middleware(options: FirewallOptions = {}) {
    const dailyCap = options.dailyCap ?? options.maxDailyBudget ?? this.defaultDailyCap;
    const perCallCap = options.perCallCap ?? options.maxPerCall ?? this.defaultPerCallCap;
    const callCost = options.callCost ?? 0.001;

    return (req: any, res: any, next: () => void) => {
      try {
        const promptCandidate = req.body?.prompt || req.body?.query || '';
        if (promptCandidate) {
          this.checkAdversarialPrompt(promptCandidate);
        }
        this.recordSpend(callCost, dailyCap, perCallCap);
        next();
      } catch (err: any) {
        res.status(403).json({ error: err.message, blockedBy: 'HaiChainFirewall' });
      }
    };
  }
}

export const firewall = new HaiChainFirewall();
export const haichain_firewall = firewall;
