import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sale-controller.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add i18n keys to SALE_I18N.en
en_target = "refBonusTag: '(+5% Ref Bonus)'"
en_replacement = """refBonusTag: '(+5% Ref Bonus)',
      refAnalyticsTitle: 'Traffic & Click Analytics',
      refAnalyticsSubtitle: 'Real-time telemetry of your referral link hits, traffic sources, and conversion rate.',
      refTotalClicks: 'Total Clicks',
      refUniqueClicks: 'Unique Visitors',
      refConversionRate: 'Conversion Rate',
      refTopSource: 'Top Traffic Channel',
      refSourceBreakdown: 'Traffic Channel Distribution',
      refTaggedLinksTitle: 'Pre-Tagged Channel Links (UTM)',
      refRecentClicks: 'Recent Click Activity',
      refNoClicksYet: 'No link clicks recorded yet. Share your link to start tracking!'"""

content = content.replace(en_target, en_replacement, 1)

# 2. Add i18n keys to SALE_I18N.vi
vi_target = "refBonusTag: '(+5% Thưởng Ref)'"
vi_replacement = """refBonusTag: '(+5% Thưởng Ref)',
      refAnalyticsTitle: 'Báo Cáo Lượt Click & Nguồn Truy Cập',
      refAnalyticsSubtitle: 'Phân tích thời gian thực lượt nhấp link, nguồn mạng xã hội và tỷ lệ chuyển đổi.',
      refTotalClicks: 'Tổng Lượt Click',
      refUniqueClicks: 'Khách Độc Nhất',
      refConversionRate: 'Tỷ Lệ Chuyển Đổi',
      refTopSource: 'Kênh Dẫn Đầu',
      refSourceBreakdown: 'Phân Bổ Kênh Truy Cập',
      refTaggedLinksTitle: 'Bộ Tạo Link Theo Kênh (Đính Kèm UTM)',
      refRecentClicks: 'Nhật Ký Truy Cập Gần Đây',
      refNoClicksYet: 'Chưa có lượt click nào được ghi nhận. Hãy chia sẻ link để bắt đầu theo dõi!'"""

content = content.replace(vi_target, vi_replacement, 1)

# 3. Add fetchReferralClickStats & loadAndRenderClickAnalytics
analytics_code = """
  // ==========================================
  // REFERRAL CLICK TELEMETRY & ANALYTICS ENGINE
  // ==========================================
  async function fetchReferralClickStats(walletAddr) {
    if (!walletAddr) {
      return {
        ref: '',
        totalClicks: 0,
        uniqueClicks: 0,
        sources: {},
        devices: { Mobile: 0, Desktop: 0 },
        countries: {},
        recentClicks: []
      };
    }

    let stats = null;
    try {
      const res = await fetch(`/api/referral/stats?ref=${encodeURIComponent(walletAddr)}`);
      if (res.ok) {
        stats = await res.json();
      }
    } catch (_) {}

    // Fallback & Merge with local cache
    const localClicks = (function() {
      try {
        const raw = JSON.parse(localStorage.getItem('haichain_referral_clicks') || '[]');
        return raw.filter(c => c.ref && c.ref.toLowerCase() === walletAddr.toLowerCase());
      } catch (_) { return []; }
    })();

    if (!stats || (stats.totalClicks === 0 && localClicks.length > 0)) {
      const sourcesMap = {};
      const devicesMap = { Mobile: 0, Desktop: 0 };
      const countriesMap = {};
      localClicks.forEach(c => {
        const s = c.source || 'Direct / Private Chat';
        const d = c.device || 'Desktop';
        sourcesMap[s] = (sourcesMap[s] || 0) + 1;
        devicesMap[d] = (devicesMap[d] || 0) + 1;
      });
      stats = {
        ref: walletAddr,
        totalClicks: localClicks.length,
        uniqueClicks: localClicks.filter(c => c.isUnique).length || localClicks.length,
        sources: sourcesMap,
        devices: devicesMap,
        countries: countriesMap,
        recentClicks: localClicks.slice(0, 20)
      };
    }

    return stats;
  }

  async function loadAndRenderClickAnalytics(walletAddr, container) {
    if (!container) return;
    const statsContainer = container.querySelector('#referral-analytics-section');
    if (!statsContainer) return;

    if (!walletAddr) {
      const barsContainer = container.querySelector('#ref-sources-bars-container');
      if (barsContainer) {
        barsContainer.innerHTML = `
          <div class="text-center py-4 text-xs text-neutral-400 font-sans">
            ${getActiveLang() === 'vi' ? 'Kết nối ví Web3 để xem phân tích nguồn truy cập.' : 'Connect Web3 wallet to inspect referral traffic sources.'}
          </div>
        `;
      }
      return;
    }

    const stats = await fetchReferralClickStats(walletAddr);
    const totalClicks = stats.totalClicks || 0;
    const uniqueClicks = stats.uniqueClicks || 0;
    const refDepositStats = getReferralStats(walletAddr);
    const totalDepositors = refDepositStats.count || 0;

    const convRate = uniqueClicks > 0
      ? ((totalDepositors / uniqueClicks) * 100).toFixed(1) + '%'
      : (totalClicks > 0 ? ((totalDepositors / totalClicks) * 100).toFixed(1) + '%' : '0.0%');

    let topSource = getActiveLang() === 'vi' ? 'Chưa có' : 'None yet';
    let topCount = 0;
    const sourcesEntries = Object.entries(stats.sources || {});
    sourcesEntries.forEach(([src, count]) => {
      if (count > topCount) {
        topCount = count;
        topSource = src;
      }
    });
    const topPercentage = totalClicks > 0 ? Math.round((topCount / totalClicks) * 100) : 0;

    const totalEl = container.querySelector('#ref-stat-total-clicks');
    if (totalEl) totalEl.textContent = totalClicks.toLocaleString();

    const uniqueEl = container.querySelector('#ref-stat-unique-clicks');
    if (uniqueEl) uniqueEl.textContent = uniqueClicks.toLocaleString();

    const uniqueRatioEl = container.querySelector('#ref-stat-unique-ratio');
    if (uniqueRatioEl) {
      const uRatio = totalClicks > 0 ? Math.round((uniqueClicks / totalClicks) * 100) : 100;
      uniqueRatioEl.textContent = `${uRatio}% ${getActiveLang() === 'vi' ? 'khách độc nhất' : 'unique'}`;
    }

    const convEl = container.querySelector('#ref-stat-conv-rate');
    if (convEl) convEl.textContent = convRate;

    const topSourceEl = container.querySelector('#ref-stat-top-source');
    if (topSourceEl) {
      topSourceEl.textContent = topCount > 0 ? `${topSource} (${topPercentage}%)` : (getActiveLang() === 'vi' ? 'Chưa có dữ liệu' : 'No data yet');
    }

    const barsContainer = container.querySelector('#ref-sources-bars-container');
    if (barsContainer) {
      if (sourcesEntries.length === 0) {
        barsContainer.innerHTML = `
          <div class="text-center py-4 text-xs text-neutral-400 font-sans">
            ${getI18nText('refNoClicksYet')}
          </div>
        `;
      } else {
        sourcesEntries.sort((a, b) => b[1] - a[1]);
        const htmlBars = sourcesEntries.map(([src, count]) => {
          const pct = Math.max(2, Math.round((count / Math.max(1, totalClicks)) * 100));
          return `
            <div class="space-y-1">
              <div class="flex items-center justify-between text-[11px] font-mono">
                <span class="text-black dark:text-neutral-200 font-semibold truncate flex items-center space-x-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white shrink-0"></span>
                  <span class="truncate">${src}</span>
                </span>
                <span class="text-neutral-500 font-bold shrink-0 ml-2">${count} <span class="text-[10px] text-neutral-400 font-normal">(${pct}%)</span></span>
              </div>
              <div class="w-full h-2 rounded-full bg-neutral-200/80 dark:bg-neutral-800 overflow-hidden">
                <div class="h-full rounded-full bg-black dark:bg-white transition-all duration-500" style="width: ${pct}%"></div>
              </div>
            </div>
          `;
        }).join('');
        barsContainer.innerHTML = htmlBars;
      }
    }

    const devInd = container.querySelector('#ref-device-indicator');
    if (devInd && stats.devices) {
      const mob = stats.devices.Mobile || 0;
      const dsk = stats.devices.Desktop || 0;
      const devTotal = mob + dsk;
      if (devTotal > 0) {
        const mobPct = Math.round((mob / devTotal) * 100);
        const dskPct = 100 - mobPct;
        devInd.textContent = `📱 Mobile ${mobPct}% • 💻 Desktop ${dskPct}%`;
      }
    }

    const recentListEl = container.querySelector('#ref-recent-clicks-list');
    const recentCountLabel = container.querySelector('#ref-click-count-label');
    const recentClicks = stats.recentClicks || [];
    if (recentCountLabel) {
      recentCountLabel.textContent = `${recentClicks.length} ${getActiveLang() === 'vi' ? 'lượt gần nhất' : 'recent events'}`;
    }
    if (recentListEl) {
      if (recentClicks.length === 0) {
        recentListEl.innerHTML = `
          <div class="p-3 rounded-xl bg-neutral-100/60 dark:bg-neutral-900/40 text-center text-[11px] text-neutral-400 font-sans">
            ${getActiveLang() === 'vi' ? 'Chưa có lượt click nào được ghi nhận cho ví của bạn.' : 'No click events recorded yet for your referral link.'}
          </div>
        `;
      } else {
        recentListEl.innerHTML = recentClicks.map(item => {
          const dateObj = new Date(item.timestamp);
          const timeStr = dateObj.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false });
          const dateStr = dateObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
          const isMobileDevice = (item.device || '').toLowerCase() === 'mobile';
          return `
            <div class="p-2 sm:p-2.5 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200/60 dark:border-neutral-800 flex items-center justify-between gap-2 text-xs font-mono">
              <div class="flex items-center space-x-2 min-w-0">
                <span class="px-2 py-0.5 rounded-md bg-neutral-100 dark:bg-neutral-900 text-[10px] font-bold text-black dark:text-white shrink-0">
                  ${item.source || 'Direct'}
                </span>
                <span class="text-neutral-400 text-[11px] truncate flex items-center space-x-1">
                  <span>${isMobileDevice ? '📱' : '💻'}</span>
                  <span>${item.device || 'Desktop'}</span>
                </span>
              </div>
              <div class="flex items-center space-x-2 shrink-0 text-[10px] text-neutral-400">
                <span>${item.country || 'Global'}</span>
                <span>•</span>
                <span>${timeStr} ${dateStr}</span>
              </div>
            </div>
          `;
        }).join('');
      }
    }

    if (window.lucide) {
      window.lucide.createIcons();
    }
  }
"""

# Insert analytics_code right before setupCalculatorLogic
calc_marker = "  // 7. CALCULATOR LOGIC\n  function setupCalculatorLogic(container) {"
content = content.replace(calc_marker, analytics_code + "\n" + calc_marker, 1)

# 4. Insert the HTML for Referral Click Analytics section inside saft-referral-hub
analytics_html = """
        <!-- 4. REFERRAL CLICK TELEMETRY & TRAFFIC SOURCES REPORT -->
        <div id="referral-analytics-section" class="pt-2 border-t border-neutral-100 dark:border-neutral-800/80">
          <div class="p-4 sm:p-5 rounded-2xl bg-neutral-50 dark:bg-neutral-900/60 border border-neutral-200 dark:border-neutral-800 space-y-4">
            
            <!-- Section Header -->
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 pb-2 border-b border-neutral-200/60 dark:border-neutral-800/60">
              <div class="flex items-center space-x-2.5">
                <div class="w-7 h-7 rounded-lg bg-neutral-200 dark:bg-neutral-800 flex items-center justify-center shrink-0">
                  <i data-lucide="bar-chart-3" class="w-4 h-4 text-emerald-500"></i>
                </div>
                <div>
                  <div class="flex items-center space-x-2">
                    <h4 class="text-xs sm:text-sm font-bold text-black dark:text-white uppercase tracking-wider font-mono">
                      ${getI18nText('refAnalyticsTitle')}
                    </h4>
                    <span class="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[9px] font-mono bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-bold border border-emerald-500/20">
                      <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                      <span>Live Telemetry</span>
                    </span>
                  </div>
                  <p class="text-[11px] text-neutral-500 dark:text-neutral-400 font-sans">
                    ${getI18nText('refAnalyticsSubtitle')}
                  </p>
                </div>
              </div>

              <div class="flex items-center space-x-2 self-start sm:self-auto">
                <button type="button" id="btn-refresh-click-stats" class="min-h-[32px] px-3 py-1 rounded-lg border border-neutral-200 dark:border-neutral-700 bg-white dark:bg-neutral-950 text-neutral-600 dark:text-neutral-300 hover:text-black dark:hover:text-white font-mono text-[11px] flex items-center space-x-1.5 cursor-pointer transition-colors active:scale-95 shadow-2xs">
                  <i data-lucide="rotate-cw" class="w-3 h-3"></i>
                  <span>${getActiveLang() === 'vi' ? 'Làm mới' : 'Refresh'}</span>
                </button>
              </div>
            </div>

            <!-- 4 Click Analytics KPI Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center">
              <div class="p-3 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800 shadow-2xs">
                <span class="text-[10px] text-neutral-400 font-sans block truncate">${getI18nText('refTotalClicks')}</span>
                <strong id="ref-stat-total-clicks" class="text-base sm:text-lg font-black text-black dark:text-white block mt-0.5">0</strong>
                <span class="text-[9px] text-neutral-400 font-mono block">${getActiveLang() === 'vi' ? 'Lượt click ghi nhận' : 'Total link hits'}</span>
              </div>
              <div class="p-3 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800 shadow-2xs">
                <span class="text-[10px] text-neutral-400 font-sans block truncate">${getI18nText('refUniqueClicks')}</span>
                <strong id="ref-stat-unique-clicks" class="text-base sm:text-lg font-black text-black dark:text-white block mt-0.5">0</strong>
                <span id="ref-stat-unique-ratio" class="text-[9px] text-neutral-400 font-mono block">100% ${getActiveLang() === 'vi' ? 'độc nhất' : 'unique'}</span>
              </div>
              <div class="p-3 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800 shadow-2xs">
                <span class="text-[10px] text-neutral-400 font-sans block truncate">${getI18nText('refConversionRate')}</span>
                <strong id="ref-stat-conv-rate" class="text-base sm:text-lg font-black text-emerald-600 dark:text-emerald-400 block mt-0.5">0.0%</strong>
                <span class="text-[9px] text-neutral-400 font-mono block">${getActiveLang() === 'vi' ? 'Ví nạp / Lượt click' : 'Referees / Clicks'}</span>
              </div>
              <div class="p-3 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200/80 dark:border-neutral-800 shadow-2xs">
                <span class="text-[10px] text-neutral-400 font-sans block truncate">${getI18nText('refTopSource')}</span>
                <strong id="ref-stat-top-source" class="text-xs sm:text-sm font-bold text-black dark:text-white block mt-1 truncate">--</strong>
                <span class="text-[9px] text-neutral-400 font-mono block">${getActiveLang() === 'vi' ? 'Kênh kéo khách tốt nhất' : 'Leading channel'}</span>
              </div>
            </div>

            <!-- Two-Column Breakdown: Sources Breakdown & 1-Click Tracked Link Generator -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 pt-1">
              <!-- Left: Traffic Sources Progress Breakdown (7 Cols) -->
              <div class="lg:col-span-7 p-3.5 sm:p-4 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-3">
                <div class="flex items-center justify-between text-xs font-mono">
                  <span class="font-bold text-black dark:text-white flex items-center space-x-1.5">
                    <i data-lucide="pie-chart" class="w-3.5 h-3.5 text-neutral-500"></i>
                    <span>${getI18nText('refSourceBreakdown')}</span>
                  </span>
                  <span id="ref-device-indicator" class="text-[10px] text-neutral-400 font-mono">📱 Mobile --% • 💻 Desktop --%</span>
                </div>

                <div id="ref-sources-bars-container" class="space-y-2.5 pt-1">
                  <div class="text-center py-4 text-xs text-neutral-400 font-sans">
                    ${getI18nText('refNoClicksYet')}
                  </div>
                </div>
              </div>

              <!-- Right: 1-Click Channel Link Generator (5 Cols) -->
              <div class="lg:col-span-5 p-3.5 sm:p-4 rounded-xl bg-white dark:bg-neutral-950 border border-neutral-200 dark:border-neutral-800 space-y-3 flex flex-col justify-between">
                <div>
                  <div class="flex items-center space-x-1.5 text-xs font-mono font-bold text-black dark:text-white">
                    <i data-lucide="link-2" class="w-3.5 h-3.5 text-neutral-500"></i>
                    <span>${getI18nText('refTaggedLinksTitle')}</span>
                  </div>
                  <p class="text-[11px] text-neutral-400 font-sans mt-1">
                    ${getActiveLang() === 'vi' ? 'Chọn kênh để sao chép link đính kèm mã theo dõi tự động:' : 'Select channel to copy pre-tagged tracking link:'}
                  </p>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-1 font-mono text-xs">
                  <button type="button" data-utm-channel="twitter" class="btn-copy-channel-link min-h-[40px] px-2.5 py-1.5 rounded-lg border border-neutral-200 dark:border-neutral-800 hover:border-black dark:hover:border-white text-black dark:text-white flex items-center justify-center space-x-1.5 transition-all active:scale-95 cursor-pointer bg-white dark:bg-neutral-900">
                    <i data-lucide="twitter" class="w-3.5 h-3.5 shrink-0"></i>
                    <span class="text-[11px] font-bold">X / Twitter</span>
                  </button>
                  <button type="button" data-utm-channel="telegram" class="btn-copy-channel-link min-h-[40px] px-2.5 py-1.5 rounded-lg border border-neutral-200 dark:border-neutral-800 hover:border-black dark:hover:border-white text-black dark:text-white flex items-center justify-center space-x-1.5 transition-all active:scale-95 cursor-pointer bg-white dark:bg-neutral-900">
                    <i data-lucide="send" class="w-3.5 h-3.5 shrink-0"></i>
                    <span class="text-[11px] font-bold">Telegram</span>
                  </button>
                  <button type="button" data-utm-channel="facebook" class="btn-copy-channel-link min-h-[40px] px-2.5 py-1.5 rounded-lg border border-neutral-200 dark:border-neutral-800 hover:border-black dark:hover:border-white text-black dark:text-white flex items-center justify-center space-x-1.5 transition-all active:scale-95 cursor-pointer bg-white dark:bg-neutral-900">
                    <i data-lucide="share-2" class="w-3.5 h-3.5 shrink-0"></i>
                    <span class="text-[11px] font-bold">Facebook</span>
                  </button>
                  <button type="button" data-utm-channel="direct" class="btn-copy-channel-link min-h-[40px] px-2.5 py-1.5 rounded-lg border border-neutral-200 dark:border-neutral-800 hover:border-black dark:hover:border-white text-black dark:text-white flex items-center justify-center space-x-1.5 transition-all active:scale-95 cursor-pointer bg-white dark:bg-neutral-900">
                    <i data-lucide="message-square" class="w-3.5 h-3.5 shrink-0"></i>
                    <span class="text-[11px] font-bold">Chat / DM</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Recent Clicks Activity Feed -->
            <div class="pt-2">
              <div class="flex items-center justify-between text-xs font-mono pb-2">
                <span class="text-neutral-500 font-bold flex items-center space-x-1.5">
                  <i data-lucide="activity" class="w-3.5 h-3.5 text-neutral-400"></i>
                  <span>${getI18nText('refRecentClicks')}</span>
                </span>
                <span id="ref-click-count-label" class="text-[10px] text-neutral-400">0 ${getActiveLang() === 'vi' ? 'lượt gần nhất' : 'recent events'}</span>
              </div>
              <div id="ref-recent-clicks-list" class="space-y-1.5 max-h-48 overflow-y-auto pr-1">
                <div class="p-3 rounded-xl bg-neutral-100/60 dark:bg-neutral-900/40 text-center text-[11px] text-neutral-400 font-sans">
                  ${getActiveLang() === 'vi' ? 'Chưa có lượt click nào được ghi nhận cho ví của bạn.' : 'No click events recorded yet for your referral link.'}
                </div>
              </div>
            </div>

          </div>
        </div>
"""

hub_close_target = """              </div>
              `;
            })()}
          </div>
        </div>
      </div>
    `;"""

hub_close_replacement = """              </div>
              `;
            })()}
          </div>
        </div>
""" + analytics_html + """      </div>
    `;"""

content = content.replace(hub_close_target, hub_close_replacement, 1)

# 5. Connect handlers inside setupCalculatorLogic
setup_logic_target = """    // Document PDF Online Viewer Triggers (Fully Multilingual & Responsive to Current Language)"""
setup_logic_replacement = """    // Referral Channel UTM Links & Telemetry Refresh Triggers
    const channelBtns = container.querySelectorAll('.btn-copy-channel-link');
    channelBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const channel = btn.getAttribute('data-utm-channel');
        const origin = window.location.origin;
        const connectedWallet = (JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}')).address || '';
        if (!connectedWallet) {
          if (typeof showToast === 'function') {
            showToast({ title: 'Wallet Required', message: getI18nText('refConnectToGenerate'), icon: 'alert-triangle' });
          } else {
            alert(getI18nText('refConnectToGenerate'));
          }
          return;
        }
        let link = `${origin}/?ref=${connectedWallet}`;
        if (channel && channel !== 'direct') {
          link += `&utm_source=${channel}`;
        }
        navigator.clipboard.writeText(link).then(() => {
          const originalHTML = btn.innerHTML;
          btn.innerHTML = `<span class="text-emerald-500 font-bold text-[11px]">✓ ${getActiveLang() === 'vi' ? 'Đã Chép' : 'Copied'}</span>`;
          if (typeof showToast === 'function') {
            showToast({
              title: getActiveLang() === 'vi' ? 'Đã Sao Chép Link' : 'Link Copied',
              message: `${getActiveLang() === 'vi' ? 'Đã tạo link có mã theo dõi cho' : 'Tracked link copied for'} ${channel.toUpperCase()}`,
              icon: 'check-circle'
            });
          }
          setTimeout(() => {
            btn.innerHTML = originalHTML;
            if (window.lucide) window.lucide.createIcons();
          }, 2000);
        });
      });
    });

    const btnRefreshClickStats = container.querySelector('#btn-refresh-click-stats');
    if (btnRefreshClickStats) {
      btnRefreshClickStats.addEventListener('click', (e) => {
        e.preventDefault();
        const connectedWallet = (JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}')).address || '';
        loadAndRenderClickAnalytics(connectedWallet, container);
      });
    }

    // Trigger initial click analytics render
    const currentConnectedWallet = (JSON.parse(localStorage.getItem('haichain-connected-wallet') || '{}')).address || '';
    loadAndRenderClickAnalytics(currentConnectedWallet, container);

    // Document PDF Online Viewer Triggers (Fully Multilingual & Responsive to Current Language)"""

content = content.replace(setup_logic_target, setup_logic_replacement, 1)

# Write to sale-controller.js and app/sale-controller.js
with open('sale-controller.js', 'w', encoding='utf-8') as f:
    f.write(content)

with open('app/sale-controller.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated sale-controller.js and app/sale-controller.js!")
