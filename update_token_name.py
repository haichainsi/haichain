# -*- coding: utf-8 -*-
import re
import os

FILES_TO_UPDATE = [
    "HAICHAIN_WHITEPAPER_V1.0_EN.md",
    "HAICHAIN_WHITEPAPER_V1.0_VI.md",
    "HAICHAIN_TECHNICAL_ARCHITECTURE_SPECIFICATION.md"
]

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename} (not found)")
        return
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    
    # 1. $HAI -> $HAISI
    content = re.sub(r'\$HAI\b', '$HAISI', content)
    
    # 2. veHAI -> veHAISI
    content = re.sub(r'\bveHAI\b', 'veHAISI', content)
    
    # 3. HAI Token / Token HAI -> HAISI Token / Token HAISI
    content = re.sub(r'\bHAI Token\b', 'HAISI Token', content)
    content = re.sub(r'\bHAI token\b', 'HAISI token', content)
    content = re.sub(r'\btoken HAI\b', 'token HAISI', content)
    content = re.sub(r'\bđồng HAI\b', 'đồng HAISI', content)
    content = re.sub(r'\bSPL Token HAI\b', 'SPL Token HAISI', content)
    content = re.sub(r'\bSPL Token \$HAI\b', 'SPL Token $HAISI', content)
    
    # 4. Table of Contents anchors: replace #8-dual-asset-cryptoeconomics-cash-flow-flywheel--hai-tokenomics
    content = content.replace("--hai-tokenomics", "--haisi-tokenomics")
    content = content.replace("-hai-tokenomics", "-haisi-tokenomics")
    content = content.replace("tokenomics-hai", "tokenomics-haisi")
    content = content.replace("spl-to-native-hai-teleport", "spl-to-native-haisi-teleport")
    content = content.replace("spl-sang-native-hai-teleport", "spl-sang-native-haisi-teleport")
    
    if content != original:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Updated token name in {filename}")
    else:
        print(f"[-] No changes needed in {filename}")

if __name__ == "__main__":
    for fn in FILES_TO_UPDATE:
        update_file(fn)
