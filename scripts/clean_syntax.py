import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    # Fix lines around getCurrentLang
    target = '''    const docLang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase();
    return SAFT_DRAWER_I18N[docLang] ? docLang : 'en';
  }
    return localStorage.getItem('haichain_lang') || document.documentElement.getAttribute('lang') || 'en';
  }'''

    replacement = '''    const docLang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase();
    return (typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N[docLang]) ? docLang : 'en';
  }'''

    code = code.replace(target, replacement)
    
    # Also in getCurrentLang, ensure safe checks for SAFT_DRAWER_I18N
    code = code.replace("SAFT_DRAWER_I18N[urlLang.toLowerCase()]", "(typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N[urlLang.toLowerCase()])")
    code = code.replace("SAFT_DRAWER_I18N[l.toLowerCase()]", "(typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N[l.toLowerCase()])")
    code = code.replace("SAFT_DRAWER_I18N[saved.toLowerCase()]", "(typeof SAFT_DRAWER_I18N !== 'undefined' && SAFT_DRAWER_I18N[saved.toLowerCase()])")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Cleaned {filepath}")

clean_file('app/pdf-modal.js')
clean_file('pdf-modal.js')
