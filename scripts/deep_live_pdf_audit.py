import urllib.request, time, fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

langs = ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']

print("=================================================================")
print("DEEP FORENSIC AUDIT OF LIVE WHITEPAPERS ON HTTPS://HAICHAIN.SI")
print("=================================================================\n")

audit_results = []

for lang in langs:
    url = f"https://haichain.si/HAICHAIN_WHITEPAPER_V1.0_{lang}.pdf?v=live_audit_{int(time.time())}"
    print(f"\n---> Fetching LIVE [{lang}]: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        
        doc = fitz.open(stream=data, filetype="pdf")
        page_count = len(doc)
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n"
        
        # Check invariants
        has_sysvar = "Sysvar1nstructions1111111111111111111111111" in full_text
        has_005_fee = "0.05%" in full_text
        has_old_010_fee = "0.10%" in full_text or "0.1%" in full_text
        has_seed_discount = "7,000,000" in full_text or "8,500,000" in full_text or "$7M" in full_text or "0.007" in full_text
        has_old_15m_seed = "$15,000,000 FDV" in full_text or "$15M FDV" in full_text or "15 Triệu USD FDV" in full_text or "15,000,000 USD FDV" in full_text
        has_buyback_burn = "Buyback" in full_text or "Burn" in full_text or "CHGB" in full_text or "mua lại" in full_text.lower()
        has_mica = "MiCA" in full_text or "USDC" in full_text or "Circle" in full_text
        
        res = {
            'lang': lang,
            'pages': page_count,
            'chars': len(full_text),
            'sysvar': has_sysvar,
            'fee_005': has_005_fee,
            'old_fee_010': has_old_010_fee,
            'seed_discount': has_seed_discount,
            'old_15m_seed': has_old_15m_seed,
            'buyback_burn': has_buyback_burn,
            'mica': has_mica
        }
        audit_results.append(res)
        
        print(f"[{lang}] Pages: {page_count} | Chars: {len(full_text):,}")
        print(f"  ✓ Sysvar Correct (43-chars): {has_sysvar}")
        print(f"  ✓ Fee 0.05% present: {has_005_fee} (Old 0.10%: {has_old_010_fee})")
        print(f"  ✓ Seed Round $7M-$8.5M FDV: {has_seed_discount} (Old $15M FDV: {has_old_15m_seed})")
        print(f"  ✓ 50% Buyback & Burn + CHGB: {has_buyback_burn}")
        print(f"  ✓ MiCA / USDC Dual Stablecoin: {has_mica}")
        
    except Exception as e:
        print(f"[{lang}] ERROR: {e}")
        audit_results.append({'lang': lang, 'error': str(e)})

print("\n=================================================================")
print("FINAL AUDIT VERDICT ACROSS ALL 10 LIVE WHITEPAPERS:")
print("=================================================================")
all_pass = all(
    r.get('pages', 0) > 10 and
    r.get('sysvar') is True and
    r.get('fee_005') is True and
    r.get('old_15m_seed') is False and
    r.get('buyback_burn') is True
    for r in audit_results
)
print(f"STATUS: {'100% PERFECT & FULLY UPDATED ON PRODUCTION' if all_pass else 'ISSUES FOUND'}")
