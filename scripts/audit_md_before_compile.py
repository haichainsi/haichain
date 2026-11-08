import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

langs = ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']

print("=== AUDITING ALL 10 MARKDOWN WHITEPAPERS BEFORE COMPILATION ===")

issues = 0

for lang in langs:
    f_path = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Sysvar check
    has_exact_sysvar = "Sysvar1nstructions1111111111111111111111111" in content
    bad_sysvar = re.findall(r'Sysvar1nstructions[1a-zA-Z0-9]*', content)
    bad_sysvars = [s for s in bad_sysvar if s != "Sysvar1nstructions1111111111111111111111111"]
    
    # 2. Protocol fee check
    # We want 0.05%
    bad_fees = re.findall(r'0\.10%|0\.1%', content)
    
    # 3. Valuation check
    bad_seeds = re.findall(r'\$15[,\.]?000[,\.]?000\s*USD\s*FDV|\$15M\s*FDV|15\s*Triệu\s*USD\s*FDV', content, re.I)
    
    print(f"\n[{lang}] {f_path}:")
    print(f"  Sysvar Correct: {has_exact_sysvar} (Bad: {bad_sysvars})")
    print(f"  Has 0.05%: {'0.05%' in content}")
    print(f"  Old 0.10% count: {len(bad_fees)}")
    print(f"  Old $15M FDV count: {len(bad_seeds)}")
    
    if bad_sysvars or bad_fees or bad_seeds:
        issues += 1

print(f"\nTOTAL FILES WITH ISSUES: {issues}")
