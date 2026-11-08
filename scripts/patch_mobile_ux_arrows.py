# -*- coding: utf-8 -*-
import sys

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content

    # 1. Hero Sub-badge (Screenshot 3)
    old_hero_badge = '''            <!-- Sub-badge -->
      <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full border border-neutral-300/80 dark:border-neutral-800 bg-white/95 dark:bg-neutral-950/90 backdrop-blur-md text-xs font-mono text-neutral-900 dark:text-neutral-200 mb-8 shadow-md">
        <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
        <span data-i18n="hero.badge">THE FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE ERA</span>
      </div>'''

    new_hero_badge = '''            <!-- Sub-badge -->
      <div class="inline-flex items-center justify-center gap-1.5 sm:gap-2 px-3 py-1.5 sm:px-4 sm:py-1.5 rounded-full border border-neutral-300/80 dark:border-neutral-800 bg-white/95 dark:bg-neutral-950/90 backdrop-blur-md text-[10px] sm:text-xs font-mono text-neutral-900 dark:text-neutral-200 mb-6 sm:mb-8 shadow-md max-w-[94vw] sm:max-w-none mx-auto">
        <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>
        <span class="leading-tight sm:leading-normal text-center whitespace-normal" data-i18n="hero.badge">THE FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE ERA</span>
      </div>'''

    if old_hero_badge in content:
        content = content.replace(old_hero_badge, new_hero_badge)
        print(f"[{filepath}] Replaced hero badge")
    else:
        print(f"[{filepath}] Hero badge pattern not found directly, checking flexible match...")

    # 2. AI2 Paradigm Badge (Screenshot 2)
    old_ai2_badge = '''        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full border border-neutral-300 dark:border-neutral-700 bg-neutral-100 dark:bg-neutral-800/80 text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs">

          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>

          <span data-i18n="ai2.badge">CORE PARADIGM &bull; HUMAN + MACHINE SYMBIOSIS (AI²)</span>

        </div>'''

    new_ai2_badge = '''        <div class="inline-flex items-center justify-center gap-1.5 sm:gap-2 px-3 py-1 sm:px-3.5 sm:py-1 rounded-full border border-neutral-300 dark:border-neutral-700 bg-neutral-100 dark:bg-neutral-800/80 text-[10px] sm:text-xs font-mono text-neutral-800 dark:text-neutral-200 mb-4 shadow-xs max-w-[94vw] sm:max-w-none mx-auto">
          <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse shrink-0"></span>
          <span class="leading-tight sm:leading-normal text-center whitespace-normal" data-i18n="ai2.badge">CORE PARADIGM &bull; HUMAN + MACHINE SYMBIOSIS (AI²)</span>
        </div>'''

    if old_ai2_badge in content:
        content = content.replace(old_ai2_badge, new_ai2_badge)
        print(f"[{filepath}] Replaced AI2 badge")
    else:
        print(f"[{filepath}] AI2 badge pattern not found directly")

    # 3. Live AI Agent Escrow Playground Card (Screenshot 1)
    old_playground = '''        <div class="rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-brand-lightCard dark:bg-brand-card p-6 sm:p-8 shadow-sm relative overflow-hidden" id="live-playground">

          <div class="flex items-center justify-between pb-4 border-b border-neutral-100 dark:border-neutral-900">

            <div class="flex items-center space-x-3">

              <div class="w-10 h-10 rounded-2xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-sm shadow-sm">

                AI

              </div>

              <div>

                <h3 class="font-semibold text-sm tracking-tight text-black dark:text-white flex items-center space-x-2">

                  <span data-i18n="home.playgroundTitle">Live AI Agent Escrow Playground</span>

                  <span class="px-2 py-0.5 rounded-full text-[10px] font-mono bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700" data-i18n="home.playgroundBadge">Devnet Live</span>

                </h3>

                <p class="text-xs text-neutral-500" data-i18n="home.playgroundSubtitle">Test autonomous sub-cent micro-payments on Solana with zero credit card fees.</p>

              </div>

            </div>

            <span class="text-xs font-mono text-neutral-400 hidden sm:inline" data-i18n="home.playgroundSvmFee">SVM &bull; 0.05% Fee</span>

          </div>



          <!-- Prompt & Model Selector -->

          <div class="mt-5 space-y-3">

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono">

              <button class="model-select-btn p-2.5 rounded-xl border border-black dark:border-white bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white font-semibold transition-all text-left" data-model="Claude 3.5 Sonnet" data-cost="0.0020">

                <div class="text-[11px] font-bold">Claude 3.5</div>

                <div class="text-[10px] text-neutral-500">$0.0020/call</div>

              </button>

              <button class="model-select-btn p-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400 hover:border-black dark:hover:border-white transition-all text-left" data-model="DeepSeek R1" data-cost="0.0008">

                <div class="text-[11px] font-bold">DeepSeek R1</div>

                <div class="text-[10px] text-neutral-500">$0.0008/call</div>

              </button>

              <button class="model-select-btn p-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400 hover:border-black dark:hover:border-white transition-all text-left" data-model="Perplexity Pro" data-cost="0.0015">

                <div class="text-[11px] font-bold">Perplexity</div>

                <div class="text-[10px] text-neutral-500">$0.0015/call</div>

              </button>

              <button class="model-select-btn p-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 text-neutral-600 dark:text-neutral-400 hover:border-black dark:hover:border-white transition-all text-left" data-model="Optimus Robot" data-cost="0.0035">

                <div class="text-[11px] font-bold">Optimus Edge</div>

                <div class="text-[10px] text-neutral-500">$0.0035/call</div>

              </button>

            </div>



            <!-- Query Input -->

            <div class="flex gap-2">

              <input type="text" id="ai-task-input" value="Summarize HAICHAIN tokenomics & sub-cent settlement speed" placeholder="Enter task for autonomous AI agent..." data-i18n-placeholder="hero.taskPlaceholder" class="flex-1 px-4 py-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white text-xs font-mono focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white">

              <button id="run-ai-task-btn" class="px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs transition-all flex items-center space-x-2 shrink-0 shadow-sm">

                <i data-lucide="zap" class="w-3.5 h-3.5"></i>

                <span data-i18n="home.playgroundExecute">Execute & Settle</span>

              </button>

            </div>'''

    new_playground = '''        <div class="rounded-2xl sm:rounded-3xl border border-brand-lightBorder dark:border-brand-border bg-brand-lightCard dark:bg-brand-card p-4 sm:p-8 shadow-sm relative overflow-hidden" id="live-playground">

          <div class="flex items-center justify-between pb-3 sm:pb-4 border-b border-neutral-100 dark:border-neutral-900 gap-2">

            <div class="flex items-start sm:items-center space-x-2.5 sm:space-x-3 min-w-0">

              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl bg-black text-white dark:bg-white dark:text-black flex items-center justify-center font-bold text-xs sm:text-sm shadow-sm shrink-0 mt-0.5 sm:mt-0">

                AI

              </div>

              <div class="min-w-0 flex-1">

                <div class="flex flex-wrap items-center gap-1.5 sm:gap-2">

                  <h3 class="font-semibold text-xs sm:text-sm tracking-tight text-black dark:text-white" data-i18n="home.playgroundTitle">Live AI Agent Escrow Playground</h3>

                  <span class="px-2 py-0.5 rounded-full text-[9px] sm:text-[10px] font-mono bg-neutral-100 text-black dark:bg-neutral-900 dark:text-white border border-neutral-300 dark:border-neutral-700 whitespace-nowrap shrink-0 inline-block" data-i18n="home.playgroundBadge">Devnet Live</span>

                </div>

                <p class="text-[11px] sm:text-xs text-neutral-500 mt-0.5 leading-snug" data-i18n="home.playgroundSubtitle">Test autonomous sub-cent micro-payments on Solana with zero credit card fees.</p>

              </div>

            </div>

            <span class="text-xs font-mono text-neutral-400 hidden sm:inline shrink-0" data-i18n="home.playgroundSvmFee">SVM &bull; 0.05% Fee</span>

          </div>



          <!-- Prompt & Model Selector -->

          <div class="mt-4 sm:mt-5 space-y-3">

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono">

              <button class="model-select-btn p-2 sm:p-2.5 rounded-xl border border-black dark:border-white bg-neutral-100 dark:bg-neutral-800 text-black dark:text-white font-semibold transition-all text-left shadow-xs" data-model="Claude 3.5 Sonnet" data-cost="0.0020">

                <div class="text-[11px] font-bold">Claude 3.5</div>

                <div class="text-[10px] text-neutral-500">$0.0020/call</div>

              </button>

              <button class="model-select-btn p-2 sm:p-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700/80 bg-neutral-50/50 dark:bg-neutral-900/50 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white transition-all text-left" data-model="DeepSeek R1" data-cost="0.0008">

                <div class="text-[11px] font-bold">DeepSeek R1</div>

                <div class="text-[10px] text-neutral-500">$0.0008/call</div>

              </button>

              <button class="model-select-btn p-2 sm:p-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700/80 bg-neutral-50/50 dark:bg-neutral-900/50 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white transition-all text-left" data-model="Perplexity Pro" data-cost="0.0015">

                <div class="text-[11px] font-bold">Perplexity</div>

                <div class="text-[10px] text-neutral-500">$0.0015/call</div>

              </button>

              <button class="model-select-btn p-2 sm:p-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700/80 bg-neutral-50/50 dark:bg-neutral-900/50 text-neutral-700 dark:text-neutral-300 hover:border-black dark:hover:border-white transition-all text-left" data-model="Optimus Robot" data-cost="0.0035">

                <div class="text-[11px] font-bold">Optimus Edge</div>

                <div class="text-[10px] text-neutral-500">$0.0035/call</div>

              </button>

            </div>



            <!-- Query Input & Action Button: Full width stack on mobile, inline on desktop -->

            <div class="flex flex-col sm:flex-row gap-2">

              <input type="text" id="ai-task-input" value="Summarize HAICHAIN tokenomics & sub-cent settlement speed" placeholder="Enter task for autonomous AI agent..." data-i18n-placeholder="hero.taskPlaceholder" class="w-full sm:flex-1 px-3.5 py-2.5 rounded-xl border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white text-xs font-mono focus:outline-none focus:ring-1 focus:ring-black dark:focus:ring-white">

              <button id="run-ai-task-btn" class="w-full sm:w-auto px-4 sm:px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs transition-all flex items-center justify-center space-x-2 shrink-0 shadow-sm cursor-pointer active:scale-98">

                <i data-lucide="zap" class="w-3.5 h-3.5"></i>

                <span data-i18n="home.playgroundExecute">Execute & Settle</span>

              </button>

            </div>'''

    if old_playground in content:
        content = content.replace(old_playground, new_playground)
        print(f"[{filepath}] Replaced Playground card")
    else:
        print(f"[{filepath}] Playground pattern not found directly")

    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[{filepath}] Successfully updated!")
    else:
        print(f"[{filepath}] No changes made.")

if __name__ == '__main__':
    patch_file('index.html')
    patch_file('app/index.html')
