import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find sections with So sánh, Bittensor, Render, Stripe, Eliza, etc.
matches = re.findall(r'(#+.*?(?:so sánh|đối chiếu|bittensor|stripe|eliza|render|đối thủ|toàn cảnh).*?\n[\s\S]*?)(?=\n#+ |\Z)', text, re.IGNORECASE)
for m in matches[:5]:
    print("--- FOUND SECTION ---")
    print(m[:1500])
