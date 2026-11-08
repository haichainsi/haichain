def patch_i18n(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update setLanguage
    target_set = """  function setLanguage(langCode) {
    if (!TRANSLATIONS[langCode]) return;
    currentLang = langCode;
    try {
      localStorage.setItem('haichain-lang', langCode);
    } catch (_) {}"""

    replace_set = """  function setLanguage(langCode) {
    if (!TRANSLATIONS[langCode]) return;
    currentLang = langCode;
    try {
      localStorage.setItem('haichain-lang', langCode);
      localStorage.setItem('haichain_lang', langCode);
    } catch (_) {}"""

    assert target_set in text, f"target_set not found in {path}"
    text = text.replace(target_set, replace_set)

    # 2. Update getInitialLanguage
    target_init = """  function getInitialLanguage() {
    try {
      const urlLang = new URLSearchParams(window.location.search).get('lang');
      if (urlLang && TRANSLATIONS[urlLang]) return urlLang;
      const saved = localStorage.getItem('haichain-lang');
      if (saved && TRANSLATIONS[saved]) return saved;
    } catch (_) {}
    return 'en';
  }"""

    replace_init = """  function getInitialLanguage() {
    try {
      const urlLang = new URLSearchParams(window.location.search).get('lang');
      if (urlLang && TRANSLATIONS[urlLang]) return urlLang;
      const saved = localStorage.getItem('haichain-lang') || localStorage.getItem('haichain_lang');
      if (saved && TRANSLATIONS[saved]) return saved;
    } catch (_) {}
    return 'en';
  }"""

    assert target_init in text, f"target_init not found in {path}"
    text = text.replace(target_init, replace_init)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Successfully patched {path}")

patch_i18n("app/i18n.js")
patch_i18n("i18n.js")
