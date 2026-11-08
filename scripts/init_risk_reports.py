import os
import shutil

# Read the base English report
with open('docs/HAICHAIN_INSTITUTIONAL_RISK_DUE_DILIGENCE_REPORT.md', 'r', encoding='utf-8') as f:
    en_content = f.read()

# Save as HAICHAIN_RISK_REPORT_EN.md
with open('HAICHAIN_RISK_REPORT_EN.md', 'w', encoding='utf-8') as f:
    f.write(en_content)
print("Saved HAICHAIN_RISK_REPORT_EN.md")
