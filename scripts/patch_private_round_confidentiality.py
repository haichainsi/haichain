# -*- coding: utf-8 -*-
import os, sys

def patch_sale_controller(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Expand ACCESS_KEYS
    old_keys = "ACCESS_KEYS: ['haichainsi2030st'],"
    new_keys = "ACCESS_KEYS: ['haichainsi2030st', 'early-backer-2026', 'haichain2026', 'hai-angel', 'vip', 'preseed', 'angel', 'investor'],"
    if old_keys in content:
        content = content.replace(old_keys, new_keys, 1)
        print(f'Expanded ACCESS_KEYS in {filepath}')
    else:
        print(f'Warning: old_keys not found in {filepath}')

    # 2. Fix hardcoded true in window.renderPreseedSalePage (2 occurrences)
    old_func = """    window.renderPreseedSalePage = function() {
      let c = document.getElementById('tab-preseed');
      if (c) {
        renderTerminalContent(c, true);
      }
    };"""

    new_func = """    window.renderPreseedSalePage = function() {
      let c = document.getElementById('tab-preseed');
      if (c) {
        const isAuth = checkAccessPermission();
        renderTerminalContent(c, isAuth);
      }
    };"""

    if old_func in content:
        content = content.replace(old_func, new_func)
        print(f'Replaced renderPreseedSalePage in {filepath}')
    else:
        print(f'Warning: old_func not found in {filepath}')

    # 3. Enhance VIP Gatekeeper UI with Institutional Whitelist Request & Back Button
    old_gate_ui = """          <div class="space-y-3 pt-2">
            <div class="relative">
              <input type="text" id="vip-gatekeeper-input" placeholder="${getI18nText('accessPlaceholder')}" class="w-full px-4 py-3.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white placeholder-neutral-400 text-xs sm:text-sm font-mono focus:outline-hidden focus:border-black dark:focus:border-white transition-all text-center tracking-wider font-semibold">
            </div>
            <button type="button" id="vip-gatekeeper-submit" class="w-full py-3.5 rounded-xl bg-black dark:bg-white text-white dark:text-black font-bold text-xs sm:text-sm font-mono transition-all hover:opacity-90 active:scale-98 shadow-sm cursor-pointer flex items-center justify-center space-x-2">
              <i data-lucide="key" class="w-4 h-4"></i>
              <span>${getI18nText('unlockBtn')}</span>
            </button>
            <p id="vip-gatekeeper-err" class="text-xs font-mono text-rose-500 hidden pt-1"></p>
          </div>
        </div>"""

    new_gate_ui = """          <div class="space-y-3 pt-2">
            <div class="relative">
              <input type="text" id="vip-gatekeeper-input" placeholder="${getI18nText('accessPlaceholder')}" class="w-full px-4 py-3.5 rounded-xl border border-neutral-300 dark:border-neutral-700 bg-neutral-50 dark:bg-neutral-900 text-black dark:text-white placeholder-neutral-400 text-xs sm:text-sm font-mono focus:outline-hidden focus:border-black dark:focus:border-white transition-all text-center tracking-wider font-semibold">
            </div>
            <button type="button" id="vip-gatekeeper-submit" class="w-full py-3.5 rounded-xl bg-black dark:bg-white text-white dark:text-black font-bold text-xs sm:text-sm font-mono transition-all hover:opacity-90 active:scale-98 shadow-sm cursor-pointer flex items-center justify-center space-x-2">
              <i data-lucide="key" class="w-4 h-4"></i>
              <span>${getI18nText('unlockBtn')}</span>
            </button>
            <p id="vip-gatekeeper-err" class="text-xs font-mono text-rose-500 hidden pt-1"></p>
          </div>
          <div class="pt-4 border-t border-neutral-100 dark:border-neutral-800/80 space-y-3">
            <p class="text-xs text-neutral-500 dark:text-neutral-400 leading-relaxed font-sans">
              ${getActiveLang() === 'vi' 
                ? 'Bạn là Quỹ đầu tư hoặc Đối tác chiến lược chưa có mã mời?' 
                : 'Are you an Institutional VC or Strategic Partner without an invitation key?'}
              <br>
              <a href="mailto:investor@haichain.si?subject=HAICHAIN%20Institutional%20Allocation%20Request" class="font-medium text-black dark:text-white underline underline-offset-4 hover:opacity-80 inline-flex items-center space-x-1 mt-1.5">
                <span>${getActiveLang() === 'vi' ? 'Gửi yêu cầu thẩm định cấp quyền đối tác' : 'Request Institutional Clearance'}</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3"></i>
              </a>
            </p>
            <div class="pt-1">
              <button type="button" onclick="window.switchTab('tab-vesting')" class="text-xs font-mono text-neutral-400 hover:text-black dark:hover:text-white transition-colors cursor-pointer inline-flex items-center space-x-1.5">
                <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
                <span>${getActiveLang() === 'vi' ? 'Quay lại Vesting Vault' : 'Back to Vesting Vault'}</span>
              </button>
            </div>
          </div>
        </div>"""

    if old_gate_ui in content:
        content = content.replace(old_gate_ui, new_gate_ui, 1)
        print(f'Enhanced VIP Gatekeeper UI in {filepath}')
    else:
        print(f'Warning: old_gate_ui not found in {filepath}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def patch_dashboard(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for VESTING_I18N
    replaces = [
        ('"subscribeSaftBtn": "Private SAFT Раундына Жазылу",', '"subscribeSaftBtn": "VIP Қолжетімділік Кілтін Енгізу",'),
        ('"subscribeDiscountBtn": "Private SAFT Раундына Жазылу (30% Жеңілдік)",', '"subscribeDiscountBtn": "Институционалдық Үлесті Сұрау (VIP Кілт)",'),
        
        ('"subscribeSaftBtn": "Subscribe to Private SAFT",', '"subscribeSaftBtn": "Enter VIP Access Key",'),
        ('"subscribeDiscountBtn": "Subscribe to Private SAFT (30% Discount)",', '"subscribeDiscountBtn": "Request Institutional Allocation (VIP Key)",'),
        
        ('"subscribeSaftBtn": "认购私募 SAFT 份额",', '"subscribeSaftBtn": "输入专属 VIP 密钥",'),
        ('"subscribeDiscountBtn": "认购私募 SAFT 份额 (享 30% 优惠折扣)",', '"subscribeDiscountBtn": "申请机构专属配额 (需邀请码)",'),
        
        ('"subscribeSaftBtn": "Đăng Ký Vòng Private SAFT",', '"subscribeSaftBtn": "Mã Mời Phân Bổ VIP",'),
        ('"subscribeDiscountBtn": "Đăng Ký Vòng Private SAFT (Chiết Khấu 30%)",', '"subscribeDiscountBtn": "Yêu Cầu Cấp Quyền Nội Bộ (Cần Mã Mời)",'),
        
        ('"subscribeSaftBtn": "프라이빗 SAFT 청약 신청",', '"subscribeSaftBtn": "VIP 액세스 키 입력",'),
        ('"subscribeDiscountBtn": "프라이빗 SAFT 청약 (30% 할인)",', '"subscribeDiscountBtn": "기관 전용 배정 요청 (초대 코드 필요)",'),
        
        ('"subscribeSaftBtn": "Souscrire au SAFT Privé",', '"subscribeSaftBtn": "Saisir la Clé d\'Accès VIP",'),
        ('"subscribeDiscountBtn": "Souscrire au SAFT Privé (-30% de Réduction)",', '"subscribeDiscountBtn": "Demander une Allocation Institutionnelle (Clé VIP)",'),
        
        ('"subscribeSaftBtn": "Suscribirse al SAFT Privado",', '"subscribeSaftBtn": "Ingresar Clave de Acceso VIP",'),
        ('"subscribeDiscountBtn": "Suscribirse al SAFT Privado (30% de Descuento)",', '"subscribeDiscountBtn": "Solicitar Asignación Institucional (Clave VIP)",'),
        
        ('"subscribeSaftBtn": "Подписаться на Приватный SAFT",', '"subscribeSaftBtn": "Ввести VIP-ключ доступа",'),
        ('"subscribeDiscountBtn": "Подписаться на Приватный SAFT (Скидка 30%)",', '"subscribeDiscountBtn": "Запросить институциональную аллокацию (VIP-код)",'),
        
        ('"subscribeSaftBtn": "प्राइवेट SAFT के लिए सदस्यता लें",', '"subscribeSaftBtn": "VIP एक्सेस कुंजी दर्ज करें",'),
        ('"subscribeDiscountBtn": "प्राइवेट SAFT के लिए सदस्यता लें (30% छूट)",', '"subscribeDiscountBtn": "संस्थागत आवंटन का अनुरोध करें (VIP कुंजी आवश्यक)",'),
        
        ('"subscribeSaftBtn": "הרשמה ל-SAFT פרטי",', '"subscribeSaftBtn": "הזן מפתח גישה ל-VIP",'),
        ('"subscribeDiscountBtn": "הרשמה ל-SAFT פרטי (30% הנחה)",', '"subscribeDiscountBtn": "בקש הקצאה מוסדית (נדרש מפתח VIP)",')
    ]

    for old_s, new_s in replaces:
        if old_s in content:
            content = content.replace(old_s, new_s, 1)
        else:
            print(f'Warning: {old_s[:40]} not found in {filepath}')

    # Add key icon to state 1 button
    old_btn_state1 = """                <button onclick="window.switchTab('tab-preseed')" class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all">
                  ${getVestingText('subscribeSaftBtn', lang)}
                </button>"""
    new_btn_state1 = """                <button onclick="window.switchTab('tab-preseed')" class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-neutral-300 dark:border-neutral-700 hover:border-black dark:hover:border-white font-mono text-xs text-neutral-700 dark:text-neutral-300 transition-all flex items-center justify-center space-x-1.5 cursor-pointer">
                  <i data-lucide="key" class="w-3.5 h-3.5 shrink-0"></i>
                  <span>${getVestingText('subscribeSaftBtn', lang)}</span>
                </button>"""
    if old_btn_state1 in content:
        content = content.replace(old_btn_state1, new_btn_state1, 1)
        print(f'Updated State 1 button in {filepath}')
    else:
        print(f'Warning: old_btn_state1 not found in {filepath}')

    # Add shield-check icon to state 2 button
    old_btn_state2 = """                <button onclick="window.switchTab('tab-preseed')" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs transition-all shadow-sm">
                  ${getVestingText('subscribeDiscountBtn', lang)}
                </button>"""
    new_btn_state2 = """                <button onclick="window.switchTab('tab-preseed')" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-black text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200 font-semibold text-xs transition-all shadow-sm flex items-center justify-center space-x-1.5 cursor-pointer">
                  <i data-lucide="shield-check" class="w-3.5 h-3.5 shrink-0"></i>
                  <span>${getVestingText('subscribeDiscountBtn', lang)}</span>
                </button>"""
    if old_btn_state2 in content:
        content = content.replace(old_btn_state2, new_btn_state2, 1)
        print(f'Updated State 2 button in {filepath}')
    else:
        print(f'Warning: old_btn_state2 not found in {filepath}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

patch_sale_controller('sale-controller.js')
patch_sale_controller('app/sale-controller.js')
patch_dashboard('dashboard.html')
patch_dashboard('app/dashboard.html')
print('All patches applied successfully!')
