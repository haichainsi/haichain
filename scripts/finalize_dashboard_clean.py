import re

reset_btns = {
    'en': {'confirmResetBtn': 'Reset', 'cancelBtn': 'Cancel'},
    'vi': {'confirmResetBtn': 'Đặt lại', 'cancelBtn': 'Huỷ'},
    'zh': {'confirmResetBtn': '重置', 'cancelBtn': '取消'},
    'ko': {'confirmResetBtn': '재설정', 'cancelBtn': '취소'},
    'fr': {'confirmResetBtn': 'Réinitialiser', 'cancelBtn': 'Annuler'},
    'es': {'confirmResetBtn': 'Restablecer', 'cancelBtn': 'Cancelar'},
    'ru': {'confirmResetBtn': 'Сброс', 'cancelBtn': 'Отмена'},
    'kk': {'confirmResetBtn': 'Қалпына келтіру', 'cancelBtn': 'Бас тарту'},
    'hi': {'confirmResetBtn': 'रीसेट करें', 'cancelBtn': 'रद्द करें'},
    'he': {'confirmResetBtn': 'איפוס', 'cancelBtn': 'ביטול'}
}

def finalize_patch(file_path):
    print(f"Finalizing patch in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Add confirmResetBtn & cancelBtn to DASH_NOTICES_I18N
    d_start = content.find('const DASH_NOTICES_I18N = {')
    d_end = content.find('function getDashNotice(key) {')
    if d_start != -1 and d_end != -1:
        dash_block = content[d_start:d_end]
        for lang, btns in reset_btns.items():
            if f'"{lang}":' in dash_block and '"confirmResetBtn"' not in dash_block:
                m = re.search(rf'"{lang}":\s*\{{\s*\n', dash_block)
                if m:
                    pos = m.end()
                    injection = f'    "confirmResetBtn": "{btns["confirmResetBtn"]}",\n    "cancelBtn": "{btns["cancelBtn"]}",\n'
                    dash_block = dash_block[:pos] + injection + dash_block[pos:]
        content = content[:d_start] + dash_block + content[d_end:]
        print("  Added confirmResetBtn & cancelBtn to DASH_NOTICES_I18N")

    # Replace confirmText & cancelText in clearUserAllocation
    old_reset = """            confirmText: isVi ? 'Đặt lại' : 'Reset',
            cancelText: isVi ? 'Huỷ' : 'Cancel'"""
    new_reset = """            confirmText: getDashNotice('confirmResetBtn'),
            cancelText: getDashNotice('cancelBtn')"""
    if old_reset in content:
        content = content.replace(old_reset, new_reset)
        print("  Replaced confirmText/cancelText with getDashNotice")

    # Replace line 6417 AI Playground toast
    old_toast = 'showToast({ title: "AI Playground", message: "Trải nghiệm suy luận AI trực tiếp qua Web3", icon: "zap" });'
    new_toast = "showToast({ title: 'AI Playground', message: getDashNotice('aiPlaygroundToast'), icon: 'zap' });"
    if old_toast in content:
        content = content.replace(old_toast, new_toast)
        print("  Replaced AI Playground toast with getDashNotice")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

finalize_patch('dashboard.html')
finalize_patch('app/dashboard.html')
