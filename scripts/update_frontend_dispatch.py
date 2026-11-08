import os

target_files = ['dashboard.html', os.path.join('app', 'dashboard.html')]

old_block = '''          const btnText = document.getElementById('confirm-hire-btn-text');
          confirmHireBtn.disabled = true;
          if (btnText) btnText.innerHTML = '<span class="w-3 h-3 rounded-full border-2 border-current border-t-transparent animate-spin inline-block mr-1"></span> Settling on Solana...';

          // Simulate 600ms network execution for high fidelity
          await new Promise(r => setTimeout(r, 600));

          const jobId = 'JOB-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(Math.random() * 9000 + 1000);
          const sig = '4AgntH1re' + Array.from({length: 78}, () => Math.floor(Math.random()*36).toString(36)).join('');
          
          let execResult = '';
          if (selectedHireAgent.category === 'data_extraction') {
            execResult = `[Executed by ${selectedHireAgent.name}]: Crawled target payload (${taskPayload.slice(0, 60)}...). Extracted 14 verified data entities into structured JSON schema with zero CAPTCHA delays.`;
          } else if (selectedHireAgent.category === 'security_audit') {
            execResult = `[Executed by ${selectedHireAgent.name}]: Completed AST static symbolic audit. Invariant I1-I9 integrity verified 100%, 0 reentrancy vulnerabilities discovered.`;
          } else if (selectedHireAgent.category === 'financial_intelligence') {
            execResult = `[Executed by ${selectedHireAgent.name}]: Scanned live orderbook liquidity and whale transaction volume for payload query. Consolidated real-time alpha signal into quantitative score.`;
          } else {
            execResult = `[Executed by ${selectedHireAgent.name}]: Completed autonomous workload (${taskPayload.slice(0, 80)}). Cryptographic settlement proof verified on Solana L1.`;
          }'''

new_block = '''          const btnText = document.getElementById('confirm-hire-btn-text');
          confirmHireBtn.disabled = true;
          if (btnText) btnText.innerHTML = '<span class="w-3 h-3 rounded-full border-2 border-current border-t-transparent animate-spin inline-block mr-1"></span> Broadcasting Solana Escrow...';

          let jobId = 'JOB-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(Math.random() * 9000 + 1000);
          let sig = '';
          let execResult = '';

          try {
            // Call Production Relayer API for real on-chain settlement & real task execution
            const resp = await fetch('/api/relayer/dispatch', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                agentId: selectedHireAgent.id || selectedHireAgent.agentId,
                taskPayload: taskPayload,
                bidAmountUsdt: selectedHireAgent.pricingUsdt || 0.003,
                recipientAddress: selectedHireAgent.recipientAddress || '5fCqijGpy7GefDM4kJr13cUv3vNdnvmKjNEpVw4iQiE3'
              })
            });

            if (!resp.ok) {
              const errData = await resp.json().catch(() => ({}));
              throw new Error(errData.error || `Server HTTP ${resp.status}`);
            }

            const data = await resp.json();
            jobId = data.jobId || jobId;
            sig = data.escrowSettlement?.txSignature || '';
            
            if (data.executionResult && typeof data.executionResult === 'object') {
              if (data.executionResult.title) {
                execResult = `[Live Execution - ${selectedHireAgent.name}]: Crawled "${data.executionResult.title}". Content: ${(data.executionResult.contentSummary || '').slice(0, 180)}...`;
              } else {
                execResult = `[Live Execution - ${selectedHireAgent.name}]: ` + JSON.stringify(data.executionResult).slice(0, 200);
              }
            } else {
              execResult = `[Executed by ${selectedHireAgent.name}]: Real On-Chain Escrow Confirmed on Solana Devnet (Slot #${data.escrowSettlement?.slot || 'Confirmed'}).`;
            }
          } catch (err) {
            console.error('Relayer dispatch error:', err);
            alert('Settlement Warning: ' + err.message + ' (Ensure HAIChain Relayer is running on port 8080/3700)');
            confirmHireBtn.disabled = false;
            if (btnText) btnText.textContent = 'Confirm & Hire Agent';
            return;
          }'''

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        c_norm = c.replace('\r\n', '\n')
        o_norm = old_block.replace('\r\n', '\n')
        n_norm = new_block.replace('\r\n', '\n')
        if o_norm in c_norm:
            c_norm = c_norm.replace(o_norm, n_norm)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(c_norm)
            print(f"SUCCESS: Updated {fpath}")
        else:
            print(f"FAILED: Old block not found in {fpath}")
