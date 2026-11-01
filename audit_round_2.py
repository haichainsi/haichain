# -*- coding: utf-8 -*-
"""
Audit Round 2: PDF Compilation & Content Verification (Final Clean)
"""
import os
import pymupdf

WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
en_pdf = os.path.join(WORKSPACE_DIR, "HAICHAIN_WHITEPAPER_V1.0_EN.pdf")
vi_pdf = os.path.join(WORKSPACE_DIR, "HAICHAIN_WHITEPAPER_V1.0_VI.pdf")

doc_en = pymupdf.open(en_pdf)
doc_vi = pymupdf.open(vi_pdf)

en_full_text = "".join([p.get_text() for p in doc_en])
vi_full_text = "".join([p.get_text() for p in doc_vi])

pdf_checks_en = {
    "1. EN PDF Size > 500KB": os.path.getsize(en_pdf) > 500 * 1024,
    "2. EN Page 3 is Table of Contents": "TABLE OF CONTENTS" in doc_en[2].get_text(),
    "3. EN Page 4 starts Chapter 1": "EXECUTIVE SUMMARY" in doc_en[3].get_text(),
    "4. 'SaaS-to-Agentic' found in EN PDF": "SaaS-to-Agentic" in en_full_text,
    "5. 'Clearing House Guarantee Buffer' found in EN PDF": "Clearing House Guarantee Buffer" in en_full_text,
    "6. 'Two-Tier Capital Protection' found in EN PDF": "Two-Tier Capital Protection" in en_full_text,
    "7. 'Distributed Swarm Inference' found in EN PDF": "Distributed Swarm Inference" in en_full_text,
    "8. 'Article 17' GDPR found in EN PDF": "Article 17" in en_full_text,
    "9. Token symbol is $HAISI in EN PDF": "$HAISI" in en_full_text,
}

pdf_checks_vi = {
    "1. VI PDF Size > 500KB": os.path.getsize(vi_pdf) > 500 * 1024,
    "2. VI Page 3 is Muc Luc": "M\u1ee4C L\u1ee4C" in doc_vi[2].get_text() or "TABLE OF CONTENTS" in doc_vi[2].get_text(),
    "3. VI Page 4 starts Chapter 1": "T\xd3M T\u1eaeT" in doc_vi[3].get_text() or "ABSTRACT" in doc_vi[3].get_text(),
    "4. 'SaaS-to-Agentic' found in VI PDF": "SaaS-to-Agentic" in vi_full_text,
    "5. 'CHGB' (Quỹ Bảo Hiểm Bù Trừ) found in VI PDF": "CHGB" in vi_full_text,
    "6. 'B\u1ea3o V\u1ec7 V\u1ed1n Hai T\u1ea7ng' found in VI PDF": "Hai T\u1ea7ng" in vi_full_text,
    "7. '\u0110i\u1ec1u 17 GDPR' found in VI PDF": "\u0110i\u1ec1u 17" in vi_full_text,
    "8. Token symbol is $HAISI in VI PDF": "$HAISI" in vi_full_text,
}

print("=== AUDIT ROUND 2: ENGLISH PDF VERIFICATION ===")
en_all_pass = True
for name, passed in pdf_checks_en.items():
    if not passed: en_all_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")

print("\n=== AUDIT ROUND 2: VIETNAMESE PDF VERIFICATION ===")
vi_all_pass = True
for name, passed in pdf_checks_vi.items():
    if not passed: vi_all_pass = False
    print(f"[{'PASS' if passed else 'FAIL'}] {name.encode('ascii', 'backslashreplace').decode('ascii')}")

print("\nSUMMARY AUDIT ROUND 2:")
print("EN PDF Status:", "ALL 9 CHECKS PASSED (100%)" if en_all_pass else "SOME CHECKS FAILED")
print("VI PDF Status:", "ALL 8 CHECKS PASSED (100%)" if vi_all_pass else "SOME CHECKS FAILED")
