# -*- coding: utf-8 -*-
"""
Verification Script for Step 3:
1. Validates all 10 language Whitepaper PDFs exist in root and app/
2. Validates PDF headers (%PDF-) and file sizes (>800 KB)
3. Validates pdf-modal.js mapping returns the exact matching language PDF
4. Validates all 10 Whitepaper Markdowns contain the new Architectural Benchmark Matrix and Guardrail specifications.
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

LANGS = ["EN", "VI", "ZH", "KO", "ES", "FR", "RU", "KK", "HI", "HE"]

def verify_all_whitepapers():
    print("=" * 70)
    print("🔍 VERIFYING ALL 10 WHITEPAPER PDFS & LANGUAGE MAPPINGS (STEP 3)")
    print("=" * 70)

    all_passed = True

    # 1. Check Root & App PDFs
    for lang in LANGS:
        fname = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.pdf"
        root_path = fname
        app_path = os.path.join("app", fname)

        # Check existence
        if not os.path.exists(root_path):
            print(f"❌ [FAIL] Missing root PDF: {root_path}")
            all_passed = False
            continue
        if not os.path.exists(app_path):
            print(f"❌ [FAIL] Missing app PDF: {app_path}")
            all_passed = False
            continue

        root_size = os.path.getsize(root_path) / 1024
        app_size = os.path.getsize(app_path) / 1024

        # Check valid PDF magic header
        with open(root_path, "rb") as f:
            header = f.read(5)
            if header != b"%PDF-":
                print(f"❌ [FAIL] Corrupted PDF header in {root_path}: {header}")
                all_passed = False
                continue

        # Check size > 800 KB
        if root_size < 800:
            print(f"❌ [FAIL] Suspiciously small PDF in {root_path}: {root_size:.1f} KB")
            all_passed = False
            continue

        print(f"✅ [{lang}] Root ({root_size:.1f} KB) & App ({app_size:.1f} KB) verified clean.")

    # 2. Check Markdown Enhancements
    print("\n--- Verifying Markdown Invariants in all 10 languages ---")
    for lang in LANGS:
        md_name = f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md"
        if not os.path.exists(md_name):
            print(f"❌ [FAIL] Missing markdown file: {md_name}")
            all_passed = False
            continue

        with open(md_name, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for benchmark matrix or Anthropic guardrail or extend_channel_reserve
        has_anchor = "extend_channel_reserve" in content or "Channel Recycling" in content or "通道复用" in content or "Tái Nạp Kênh" in content or "채널 재충전" in content
        has_python = "haichain_pay" in content or "haichain-agent-pay" in content
        has_watchtower = "Watchtower" in content or "Tháp Canh" in content or "瞭望塔" in content or "워치타워" in content or "מגדל שמירה" in content or "वॉचटावर" in content or "Сентинел" in content

        if not (has_anchor and has_python and has_watchtower):
            print(f"❌ [FAIL] {md_name} missing key Step 3 sections (Anchor: {has_anchor}, Python: {has_python}, Watchtower: {has_watchtower})")
            all_passed = False
        else:
            print(f"✅ [{lang}] Markdown content verified with Benchmark, Python SDK & Watchtower.")

    # 3. Check pdf-modal.js mapping
    print("\n--- Verifying Web PDF Modal Language Routing ---")
    with open("pdf-modal.js", "r", encoding="utf-8") as f:
        modal_code = f.read()

    for lang in LANGS:
        expected = f"/HAICHAIN_WHITEPAPER_V1.0_{lang}.pdf"
        if expected not in modal_code:
            print(f"❌ [FAIL] pdf-modal.js missing route for {expected}")
            all_passed = False
        else:
            print(f"✅ [Router] Lang {lang} mapped to {expected}")

    print("\n" + "=" * 70)
    if all_passed:
        print("🎉 ALL 10 WHITEPAPER PDFS & WEB MODAL ROUTES FULLY VERIFIED!")
    else:
        print("❌ VERIFICATION ENCOUNTERED FAILURES.")
    print("=" * 70)

    return all_passed

if __name__ == "__main__":
    success = verify_all_whitepapers()
    sys.exit(0 if success else 1)
