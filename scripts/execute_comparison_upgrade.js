const fs = require('fs');

// 1. Backup
fs.copyFileSync('i18n.js', 'i18n.js.bak');
fs.copyFileSync('index.html', 'index.html.bak');
console.log('✅ Backed up i18n.js and index.html');

// 2. Read python translation dict or load directly
const pyScript = fs.readFileSync('scripts/apply_benchmark_revamp.py', 'utf8');
const match = pyScript.match(/UPDATED_DATA\s*=\s*(\{[\s\S]*?\n\})/);
if (!match) {
  console.error('❌ Could not find UPDATED_DATA in apply_benchmark_revamp.py');
  process.exit(1);
}

// Parse Python dict to JS object safely
let dataStr = match[1];
// Replace boolean/None if any
const updatedData = eval('(' + dataStr + ')');
console.log('Loaded updated translations for languages:', Object.keys(updatedData));

// 3. Load i18n.js
const i18nContent = fs.readFileSync('i18n.js', 'utf8');
const startTag = 'const TRANSLATIONS = {';
const endTag = 'function getInitialLanguage()';
const startIdx = i18nContent.indexOf(startTag);
const endIdx = i18nContent.indexOf(endTag);

if (startIdx === -1 || endIdx === -1) {
  console.error('❌ Could not locate TRANSLATIONS markers in i18n.js');
  process.exit(1);
}

let code = i18nContent.slice(startIdx, endIdx).trim();
if (code.endsWith(';')) code = code.slice(0, -1);
code = code.replace('const TRANSLATIONS =', 'global.TRANSLATIONS =');
eval(code);

const currentTranslations = global.TRANSLATIONS;

// 4. Update keys for each language
for (const lang of Object.keys(updatedData)) {
  if (!currentTranslations[lang]) {
    console.warn(`Warning: Language ${lang} not found in TRANSLATIONS`);
    continue;
  }
  const dict = updatedData[lang];
  for (const [key, val] of Object.entries(dict)) {
    currentTranslations[lang][key] = val;
  }
  console.log(`Updated ${Object.keys(dict).length} keys for [${lang}]`);
}

// Serialize TRANSLATIONS back
const newTranslationsCode = 'const TRANSLATIONS = ' + JSON.stringify(currentTranslations, null, 2) + ';\n\n  ';
const newI18nContent = i18nContent.slice(0, startIdx) + newTranslationsCode + i18nContent.slice(endIdx);
fs.writeFileSync('i18n.js', newI18nContent, 'utf8');
console.log('✅ Successfully rewritten i18n.js');

// 5. Update index.html
let htmlContent = fs.readFileSync('index.html', 'utf8');

const tableSearchStart = '<!-- ======================== SECTION: BENCHMARK COMPARISON MATRIX ======================== -->';
const tableSearchEnd = '</section>';
const secStart = htmlContent.indexOf(tableSearchStart);
const secEnd = htmlContent.indexOf(tableSearchEnd, secStart);

if (secStart === -1 || secEnd === -1) {
  console.error('❌ Could not locate comparison section in index.html');
  process.exit(1);
}

const updatedSectionHtml = `<!-- ======================== SECTION: BENCHMARK COMPARISON MATRIX ======================== -->

  <section id="comparison" class="py-16 sm:py-20 border-t border-brand-lightBorder dark:border-brand-border bg-neutral-50/50 dark:bg-neutral-950/60 relative">

    <div class="max-w-7xl mx-auto px-4 sm:px-6">

      <div class="text-center max-w-3xl mx-auto mb-12">

        <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full border border-neutral-300 dark:border-neutral-800 bg-white dark:bg-neutral-900 text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs">

          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>

          <span data-i18n="comp.badge">ARCHITECTURAL COMPARISON &bull; TECHNICAL FOUNDATION</span>

        </div>

        <h2 class="text-3xl sm:text-4xl font-bold tracking-tight text-black dark:text-white" data-i18n="comp.title">

          Architectural Trade-offs: Autonomous Agent Financial Rails

        </h2>

        <p class="text-sm sm:text-base text-neutral-600 dark:text-neutral-400 mt-4 leading-relaxed font-light" data-i18n="comp.subtitle">

          A rigorous comparison of settlement layers, latency boundaries, containment security, and operational trade-offs.

        </p>

      </div>

      <!-- Comparison Table Card with Horizontal Scroll -->

      <div class="rounded-3xl border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-brand-card shadow-sm overflow-hidden">

        <div class="overflow-x-auto">

          <table class="w-full text-left text-xs font-sans border-collapse min-w-[760px]">

            <thead>

              <tr class="border-b border-neutral-200 dark:border-neutral-800 bg-neutral-100/70 dark:bg-neutral-900/80">

                <th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[20%]" data-i18n="comp.colFeature">Architectural Dimension</th>

                <th class="py-4 px-5 font-bold uppercase tracking-wider text-black dark:text-white font-mono bg-neutral-200/60 dark:bg-neutral-800/80 w-[24%]" data-i18n="comp.colHai">HAICHAIN (HAI²)</th>

                <th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[18%]" data-i18n="comp.colTao">Coinbase AgentKit (x402)</th>

                <th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[18%]" data-i18n="comp.colRender">Skyfire Protocol</th>

                <th class="py-4 px-5 font-bold uppercase tracking-wider text-neutral-600 dark:text-neutral-400 font-mono w-[20%]" data-i18n="comp.colEliza">Stripe / Legacy Rails</th>

              </tr>

            </thead>

            <tbody class="divide-y divide-neutral-100 dark:divide-neutral-900 leading-relaxed">

              <!-- Row 1: Core Architectural Layer -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row1Name">Core Architectural Layer</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row1Hai">Agentic Micro-Payment OS & Settlement Engine (Solana-native, Sub-PDA bounded)</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Tao">Smart contract wallet SDK for AI agents on Base/Ethereum (x402 enabled)</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Render">B2B custodial payment API wrapping USDC on Base/Polygon</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row1Eliza">Centralized fiat payment gateway & acquiring network designed for human checkouts</td>

              </tr>

              <!-- Row 2: Latency Profile & Settlement -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row2Name">Latency & Settlement Profile</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row2Hai">Hybrid: In-Memory Netting ~0.14ms | Solana Block ~400ms (Optimistic confirmation)</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Tao">On-chain Base block: ~2s soft confirmation (L1 finality ~15 mins)</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Render">API round-trip: 1 - 3s + EVM batch settlement confirmation</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row2Eliza">2 - 3 business days (T+2 banking interchange clearing & batch settlement)</td>

              </tr>

              <!-- Row 3: Transaction Cost & Granularity -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row3Name">Transaction Cost & Granularity</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row3Hai">Sub-cent viable (< $0.0002 on-chain, fraction of nano-cent via netting). Native $0.0001 per call</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Tao">~$0.001 - $0.005 Base gas fee (Post-Dencun L2 blobs; requires batching for micro-streams)</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Render">$0.01 - $0.05+ per payment call API markup; corporate batch invoicing</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row3Eliza">$0.30 fixed swipe fee + 2.9% (30,000% overhead on a $0.001 API query)</td>

              </tr>

              <!-- Row 4: Agent Threat Model & Blast Radius -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row4Name">Agent Threat Model & Blast Radius</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row4Hai">Blast-Radius Containment: Sub-PDA programmatic spending bounds + Instant Panic Kill-Switch</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Tao">Application-level MPC key policies; vulnerable to bounded drain if agent logic is tricked</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Render">Centralized SaaS quota limits managed on corporate web console</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row4Eliza">Post-loss remediation: Must freeze corporate card & file dispute taking 30-60 days</td>

              </tr>

              <!-- Row 5: Integration & User Experience -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row5Name">Integration & User Experience</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row5Hai">Invisible Web3: Biometric Passkey, instant fiat onramp & native Model Context Protocol (MCP)</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Tao">Developer CDP API keys, wallet management SDKs, EVM contract infrastructure</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Render">Web2 enterprise API keys linked to corporate deposit accounts</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row5Eliza">Manual credit card checkout forms, exposed PII, subject to payment fraud</td>

              </tr>

              <!-- Row 6: Custody & Trust Model -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row6Name">Custody & Trust Model</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row6Hai">Non-Custodial: Smart contract state invariants on Solana; real yield protocol fee utility</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Tao">Non-Custodial / Hybrid: User-held MPC keys; zero native token (Base sequencer value)</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Render">Custodial: Funds deposited in corporate account; closed-source margin capture</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row6Eliza">Fully Custodial: Banking rails & card network escrow with centralized fund withholding</td>

              </tr>

              <!-- Row 7: Human-in-the-Loop & Escalation -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors border-t border-neutral-100 dark:border-neutral-900">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row7Name">Human-in-the-Loop & Escalation</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row7Hai">Native Reverse x402: Sub-second programmatic escrow dispatch with async human verification SLA</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Tao">No native bounty rail; developers must manually architect custom escalation webhooks</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Render">Enterprise support tickets and manual customer service intervention queues</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row7Eliza">30 - 90 day credit card chargeback arbitration with strict dispute penalties</td>

              </tr>

              <!-- Row 8: Ecosystem Maturity & Fiat Rails (Trade-off Balance) -->

              <tr class="hover:bg-neutral-50/50 dark:hover:bg-neutral-900/30 transition-colors border-t border-neutral-100 dark:border-neutral-900">

                <td class="py-4 px-5 font-semibold text-neutral-800 dark:text-neutral-200" data-i18n="comp.row8Name">Ecosystem Maturity & Fiat Rails</td>

                <td class="py-4 px-5 font-semibold text-black dark:text-white bg-neutral-50/80 dark:bg-neutral-900/40" data-i18n="comp.row8Hai">Emerging Specialist: Purpose-built for high-throughput autonomous agent micro-economies</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row8Tao">High: Deep EVM ecosystem, extensive developer tooling & native Coinbase fiat ramps</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row8Render">Moderate: Expanding enterprise B2B partner network & vendor agent integrations</td>

                <td class="py-4 px-5 text-neutral-600 dark:text-neutral-400" data-i18n="comp.row8Eliza">Global Dominance: Trillions in annual volume across 135+ currencies and banking rails</td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

    </div>

  `;

htmlContent = htmlContent.slice(0, secStart) + updatedSectionHtml + htmlContent.slice(secEnd);
fs.writeFileSync('index.html', htmlContent, 'utf8');
console.log('✅ Successfully rewritten index.html');
