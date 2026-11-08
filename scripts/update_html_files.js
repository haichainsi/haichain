const fs = require('fs');
const path = require('path');

console.log('=== UPGRADING INDEX.HTML & DASHBOARD.HTML ===');

function updateIndexHtml(filePath) {
  if (!fs.existsSync(filePath)) return;
  let code = fs.readFileSync(filePath, 'utf8');

  // 1. Audits passed text
  code = code.replace(
    '<span class="hidden md:inline text-black dark:text-white font-mono font-semibold" data-i18n="cluster.auditsPassed">15/15 Audits Passed</span>',
    '<span class="hidden md:inline text-black dark:text-white font-mono font-semibold" data-i18n="cluster.auditsPassed">15/15 Test Vectors Verified</span>'
  );

  // 2. Whitepaper navigation links (fail-safe)
  const oldDesktopWp = `<a href="javascript:void(0)" onclick="event.preventDefault(); window.openPdfViewerModal && window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_' + ((window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en')).toUpperCase() + '.pdf');" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">`;
  const newDesktopWp = `<a href="/HAICHAIN_WHITEPAPER_V1.0_EN.pdf" target="_blank" onclick="if (window.openPdfViewerModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en').toUpperCase(); window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_' + lang + '.pdf'); }" class="hover:text-black dark:hover:text-white transition-colors flex items-center space-x-1 cursor-pointer" id="nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">`;
  code = code.replace(oldDesktopWp, newDesktopWp);

  const oldMobileWp = `<a href="javascript:void(0)" onclick="event.preventDefault(); if (typeof window.closeMobileMenu === 'function') { window.closeMobileMenu(); } window.openPdfViewerModal && window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_' + ((window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en')).toUpperCase() + '.pdf');" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" id="mobile-nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">`;
  const newMobileWp = `<a href="/HAICHAIN_WHITEPAPER_V1.0_EN.pdf" target="_blank" onclick="if (typeof window.closeMobileMenu === 'function') { window.closeMobileMenu(); } if (window.openPdfViewerModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en').toUpperCase(); window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_' + lang + '.pdf'); }" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white flex items-center justify-between transition-colors" id="mobile-nav-whitepaper-link" data-open-whitepaper="true" data-pdf-whitepaper="true">`;
  code = code.replace(oldMobileWp, newMobileWp);

  const oldFooterWp = `<a href="javascript:void(0)" onclick="event.preventDefault(); window.openPdfViewerModal && window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_' + ((window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en')).toUpperCase() + '.pdf');" class="hover:text-black dark:hover:text-white transition-colors cursor-pointer" data-open-whitepaper="true">`;
  const newFooterWp = `<a href="/HAICHAIN_WHITEPAPER_V1.0_EN.pdf" target="_blank" onclick="if (window.openPdfViewerModal) { event.preventDefault(); const lang = (window.haichainI18n && window.haichainI18n.getLanguage ? window.haichainI18n.getLanguage() : localStorage.getItem('haichain_lang') || 'en').toUpperCase(); window.openPdfViewerModal('/HAICHAIN_WHITEPAPER_V1.0_' + lang + '.pdf'); }" class="hover:text-black dark:hover:text-white transition-colors cursor-pointer" data-open-whitepaper="true">`;
  code = code.replace(oldFooterWp, newFooterWp);

  // 3. Proof of transaction latency
  code = code.replace(
    '<div class="text-[10px] text-neutral-500 font-mono" data-i18n="pot.txSettled">0.14ms &bull; Settled</div>',
    '<div class="text-[10px] text-neutral-500 font-mono" data-i18n="pot.txSettled">0.14ms Netting &bull; On-Chain Queued</div>'
  );

  // 4. Comparison table headers
  code = code.replace(
    '<th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[18%]" data-i18n="comp.colTao">Bittensor ($TAO)</th>',
    '<th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[18%]" data-i18n="comp.colTao">Coinbase AgentKit (x402)</th>'
  );
  code = code.replace(
    '<th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[18%]" data-i18n="comp.colRender">Render / io.net</th>',
    '<th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[18%]" data-i18n="comp.colRender">Skyfire Protocol</th>'
  );
  code = code.replace(
    '<th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[20%]" data-i18n="comp.colEliza">ElizaOS / Virtuals</th>',
    '<th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[20%]" data-i18n="comp.colEliza">Stripe / Legacy Rails</th>'
  );

  // 5. Comparison table rows fallback content
  code = code.replace(
    '<td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row2Hai">< 400 milliseconds (Sub-slot speed matching LLM reasoning ticks)</td>',
    '<td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row2Hai">In-Memory Netting: 0.14ms | Solana Settlement: <400ms</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Tao">Decentralized AI model ranking & subnet evaluation network</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Tao">EVM smart contract wallet SDK for AI agents on Base/Ethereum</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Render">Distributed raw GPU compute and rendering power marketplace</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Render">B2B custodial payment API wrapping USDC on Base/Polygon</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Eliza">Social agent meme tokenization & virtual character speculation</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Eliza">Legacy human credit card merchant gateway with high fixed fees</td>'
  );

  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Tao">12 - 60 seconds (Infeasible for real-time per-query API payments)</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Tao">2 - 12 seconds (Base/EVM block times; no in-memory netting)</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Render">Minutes to hours (Batch settlement per render job)</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Render">2 - 5+ seconds (API verification + EVM transaction confirmation)</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Eliza">12 - 15 seconds (Constrained by underlying EVM/Base block times)</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Eliza">2 - 3 business days (T+2 legacy bank interchange clearing)</td>'
  );

  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Tao">Prohibitive subnet costs ($10k - $100k+), no sub-cent payments</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Tao">$0.01 - $0.08 Base gas fee (prohibitive for per-query streaming)</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Render">Tens of dollars per job. Not designed for micro-transactions</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Render">$0.02 - $0.10+ per payment call; batch invoicing required</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Eliza">$0.02 - $0.15 EVM gas fees (economically unfeasible for $0.001 calls)</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Eliza">$0.30 fixed swipe fee + 2.9% (30,000% overhead on a $0.001 query)</td>'
  );

  code = code.replace(
    '<td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row4Hai">100% Cryptographic Immunity: Merkle PDA bounds + Panic Kill-Switch</td>',
    '<td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row4Hai">Deterministic Sub-PDA Spending Bounds + Instant Panic Kill-Switch Circuit</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Tao">No financial capability boundary enforcement for autonomous agents</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Tao">Application-level MPC key policies; vulnerable if agent logic is compromised</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Render">Not applicable (Bare compute resource renting only)</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Render">Centralized API quota limits managed on corporate web portal</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Eliza">Severe risk: Agent wallets can be drained by prompt injection or infinite loops</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Eliza">Must freeze corporate card and file chargeback disputes taking 30-60 days</td>'
  );

  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Tao">Extremely complex, strictly for AI researchers and GPU miners</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Tao">Developer CDP API keys and complex EVM smart wallet infrastructure</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Render">Technical portal for infrastructure providers and 3D artists</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Render">Web2 enterprise API keys linked to corporate deposit accounts</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Eliza">Requires Web3 wallet (Metamask), managing 12-word seed phrases</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Eliza">Manual credit card entry, exposed PII, vulnerable to identity theft</td>'
  );

  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Tao">Inflationary block reward emissions distributed to subnet validators</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Tao">Zero native token; sequencer revenue accrues solely to Base / Coinbase</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Render">Utility token burns/payments for compute cycles</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Render">Proprietary corporate margin; closed-source corporate equity capture</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Eliza">Speculative token trading on individual agent bonding curves</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Eliza">100% merchant interchange revenue retained by Stripe Inc. shareholders</td>'
  );

  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Tao">Zero human involvement. Pure machine-weighted subnet validation; incapable of resolving AI hallucinations or blind spots with human domain experts.</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Tao">No native reverse bounty rail; developers must manually architect custom human escalation mechanisms.</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Render">Raw compute renting only. No cognitive intelligence layer, human moderation, or blind spot auditing mechanism.</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Render">Enterprise support tickets and manual customer service intervention; no sub-second agent bounties.</td>'
  );
  code = code.replace(
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Eliza">Unsupervised autonomous bot loops. No programmatic escrow to hire human oversight, leading to unchecked bot hallucinations and manipulation risks.</td>',
    '<td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Eliza">30 - 90 day credit card chargeback arbitration with high dispute penalties.</td>'
  );

  // 6. Investor future description (50x - 140x removed)
  code = code.replace(
    '<p class="text-neutral-600 dark:text-neutral-400 leading-relaxed" data-i18n="aud.investorFutureDesc">Target 50x - 140x appreciation as $HAI transitions 1:1 into Native Gas Coin of the independent Sovereign AI L1 ($1B - $5B+ FDV).</p>',
    '<p class="text-neutral-600 dark:text-neutral-400 leading-relaxed" data-i18n="aud.investorFutureDesc">Long-term protocol value accrual: 1:1 transition into Native Gas Asset upon dedicated App-Chain and Sovereign L1 scaling, capturing network fee velocity across the autonomous agent economy.</p>'
  );

  // 7. Tech done 2 (15/15 tests & scheduled audit)
  code = code.replace(
    '<span data-i18n="tech.done2">Passed 15/15 automated forensic security tests (defending against historic $800M+ Wormhole, Nomad, Euler, Mango exploits).</span>',
    '<span data-i18n="tech.done2">Passed 15/15 automated forensic test vectors (simulating historic $800M+ Wormhole, Nomad, Euler exploits). Independent external audit scheduled prior to Mainnet TGE.</span>'
  );

  // 8. Roadmap ARR
  code = code.replace(
    '<span data-i18n="roadmap.stage1Item3">Target: 100,000+ Active Agents & $15.9M ARR</span>',
    '<span data-i18n="roadmap.stage1Item3">Milestone: 100,000+ Connected Agents & 50M+ Monthly Micro-Settlements</span>'
  );

  // 9. Footer compliance
  code = code.replace(
    '<span data-i18n="footer.compliance">Non-Custodial FinCEN Exempt &bull; EU MiCA Compliant &bull; 100% Exploit Immune</span>',
    '<span data-i18n="footer.compliance">Non-Custodial Architecture &bull; EU MiCA / FinCEN Utility Standards &bull; Formally Verified Sub-PDA Invariants</span>'
  );

  fs.writeFileSync(filePath, code, 'utf8');
  console.log(`Updated ${filePath} successfully.`);
}

function updateDashboardHtml(filePath) {
  if (!fs.existsSync(filePath)) return;
  let code = fs.readFileSync(filePath, 'utf8');

  // Replace 100% exploit immune / capital safety
  code = code.replace(
    '<span class="text-[10px] text-neutral-500" data-i18n="aiHub.webFeature2Desc">Hard budget limits, 100% capital safety</span>',
    '<span class="text-[10px] text-neutral-500" data-i18n="aiHub.webFeature2Desc">Hard budget limits, cryptographic blast-radius capping</span>'
  );
  code = code.replace(
    '<span class="text-[10px] text-neutral-500" data-i18n="aiHub.webFeature3Desc">Reclaim 100% funds to wallet in 380ms</span>',
    '<span class="text-[10px] text-neutral-500" data-i18n="aiHub.webFeature3Desc">Reclaim unspent funds to wallet in ~380ms</span>'
  );

  // Clarify 0.14ms table latency
  code = code.replace(
    '<td class="py-3 px-4 text-neutral-400">0.14ms</td>',
    '<td class="py-3 px-4 text-neutral-400">0.14ms (Netting)</td>'
  );

  fs.writeFileSync(filePath, code, 'utf8');
  console.log(`Updated ${filePath} successfully.`);
}

updateIndexHtml('index.html');
updateIndexHtml('app/index.html');
updateDashboardHtml('dashboard.html');
updateDashboardHtml('app/dashboard.html');
