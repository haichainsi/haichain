import os
import re

# 1. Update server/production-agent-relayer.js
with open('server/production-agent-relayer.js', 'r', encoding='utf-8') as f:
    relayer_code = f.read().replace('\r\n', '\n')

old_task_exec = """  async executeDownstreamTask(agentId, payload) {
    const startTime = Date.now();
    let resultData = null;

    if (agentId.includes('scraper')) {
      resultData = await this.relayWebExtraction(payload);
    } else if (agentId.includes('market') || agentId.includes('arbitrage') || agentId.includes('sentiment')) {
      resultData = await this.relayFinancialIntelligence(payload);
    } else if (agentId.includes('sec') || agentId.includes('audit')) {
      resultData = await this.relaySecurityAudit(payload);
    } else {
      resultData = {
        status: 'SUCCESS',
        mode: 'TEE_WASM_SANDBOX',
        inputPayload: payload,
        outputDigest: Buffer.from(payload).toString('base64'),
        output: `Processed ${Buffer.byteLength(payload)} input bytes inside hardware-isolated enclave.`
      };
    }

    const latencyMs = Date.now() - startTime;
    return {
      latencyMs,
      result: resultData
    };
  }"""

new_task_exec = """  async executeDownstreamTask(agentId, payload) {
    const startTime = Date.now();
    let resultData = null;

    // Check if agent is a registered community or external agent with an endpointUrl
    const matchedAgent = (this.allAgents || []).find(a => a.agentId === agentId);
    if (matchedAgent && matchedAgent.endpointUrl) {
      resultData = await this.relayRemoteAgentEndpoint(matchedAgent, payload);
    } else if (agentId.includes('scraper')) {
      resultData = await this.relayWebExtraction(payload);
    } else if (agentId.includes('market') || agentId.includes('arbitrage') || agentId.includes('sentiment')) {
      resultData = await this.relayFinancialIntelligence(payload);
    } else if (agentId.includes('sec') || agentId.includes('audit')) {
      resultData = await this.relaySecurityAudit(payload);
    } else {
      resultData = {
        status: 'SUCCESS',
        mode: 'TEE_WASM_SANDBOX',
        inputPayload: payload,
        outputDigest: Buffer.from(payload).toString('base64'),
        output: `Processed ${Buffer.byteLength(payload)} input bytes inside hardware-isolated enclave.`
      };
    }

    const latencyMs = Date.now() - startTime;
    return {
      latencyMs,
      result: resultData
    };
  }

  /**
   * Real Autonomous HTTP 402 Handshake & Remote Agent Dispatch
   */
  async relayRemoteAgentEndpoint(agent, payload) {
    console.log(`[Remote Agent Relay] Dispatching task to external agent: ${agent.name} (${agent.endpointUrl})`);
    
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 8000);

    try {
      let resp = await fetch(agent.endpointUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'User-Agent': 'HAICHAIN-Autonomous-Agent-Relayer/1.1'
        },
        body: JSON.stringify({ taskPayload: payload, clientTimestamp: Date.now() }),
        signal: controller.signal
      });

      // If HTTP 402 Payment Required: Settle on-chain and retry with payment signature!
      if (resp.status === 402) {
        console.log(`[Remote Agent Relay] Agent returned HTTP 402 Payment Required! Initiating Solana micro-escrow...`);
        const challengeHeaders = Object.fromEntries(resp.headers.entries());
        let challengeBody = {};
        try { challengeBody = await resp.json(); } catch (_) {}
        
        const challenge = this.parse402Challenge(challengeHeaders, challengeBody);
        const recipient = challenge.payee || agent.recipientAddress || DEFAULT_TREASURY;
        const amountUsdt = challenge.amountUsdt || agent.pricingUsdt || 0.003;

        // Broadcast Real Solana Transaction
        const payment = await this.broadcastRealSolanaPayment(recipient, amountUsdt);
        console.log(`[Remote Agent Relay] Micro-payment confirmed: ${payment.txSignature}. Retrying downstream task with voucher...`);

        // Second attempt: Present on-chain payment signature
        const retryResp = await fetch(agent.endpointUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `X402 ${payment.txSignature}`,
            'X-Payment-Signature': payment.txSignature,
            'User-Agent': 'HAICHAIN-Autonomous-Agent-Relayer/1.1'
          },
          body: JSON.stringify({ taskPayload: payload, txSignature: payment.txSignature }),
          signal: controller.signal
        });

        clearTimeout(timeoutId);
        if (!retryResp.ok) {
          throw new Error(`Downstream agent failed verification after payment: HTTP ${retryResp.status}`);
        }

        const data = await retryResp.json().catch(async () => ({ text: await retryResp.text() }));
        return {
          status: 'SUCCESS',
          protocolHandshake: 'HTTP_402_PAYMENT_SETTLED',
          agentEndpoint: agent.endpointUrl,
          onChainSettlement: payment,
          downstreamResponse: data
        };
      }

      clearTimeout(timeoutId);
      const data = await resp.json().catch(async () => ({ text: await resp.text() }));
      return {
        status: 'SUCCESS',
        protocolHandshake: 'DIRECT_DISPATCH',
        agentEndpoint: agent.endpointUrl,
        downstreamResponse: data
      };
    } catch (err) {
      clearTimeout(timeoutId);
      throw new Error(`Remote agent dispatch failed (${agent.endpointUrl}): ${err.message}`);
    }
  }"""

if old_task_exec in relayer_code:
    relayer_code = relayer_code.replace(old_task_exec, new_task_exec)
    with open('server/production-agent-relayer.js', 'w', encoding='utf-8') as f:
        f.write(relayer_code)
    print("SUCCESS: Updated server/production-agent-relayer.js with remote HTTP 402 dispatch!")
else:
    print("WARNING: old_task_exec not matched in relayer")

print("Remote dispatch script finished.")
