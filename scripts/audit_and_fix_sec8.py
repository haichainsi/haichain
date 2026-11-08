import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
    path = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Let's inspect where $$ appears near 50,000,000 or 25,000 or 100,000
    # Specifically:
    # **$$\n\n50,000,000\text{ USD}$** -> **$50,000,000 USD**
    # $$25,000\text{ USD}$** -> **$25,000 USD**
    # $$50,000\text{ USD}$ -> $50,000 USD
    # $10,000\text{ agents}$ -> 10,000 agents
    # $100,000\text{ } $HAISI$ -> 100,000 $HAISI

    orig = text

    # Fix pattern 1: **$$\n\n50,000,000\text{ USD}$**
    text = re.sub(r'\*\*\$\$\s*\n+\s*50[.,]000[.,]000(?:\\text\{\s*USD\s*\})?\$?\*\*', r'**$50,000,000 USD**', text)
    # Fix pattern 2: **\n\n$$25,000\text{ USD}$**
    text = re.sub(r'\*\*\s*\n+\s*\$\$25[.,]000(?:\\text\{\s*USD\s*\})?\$?\*\*', r'**$25,000 USD**', text)
    # Fix pattern 3: on $$\n\n50,000,000\text{ USD}$ volume
    text = re.sub(r'on\s*\$\$\s*\n+\s*50[.,]000[.,]000(?:\\text\{\s*USD\s*\})?\$?\s*volume', r'on $50,000,000 USD volume', text)
    # Fix pattern 4: $$50,000\text{ USD}$
    text = re.sub(r'\$\$50[.,]000(?:\\text\{\s*USD\s*\})?\$', r'$50,000 USD', text)
    # Fix pattern 5: $10,000\text{ agents}$ or $10.000\text{ agents}$
    text = re.sub(r'\$10[.,]000\\text\{\s*(?:agents|tác tử|智能体|에이전트|agentes|агентов)\s*\}\$', r'10,000 agents', text)
    # Fix pattern 6: $100,000\text{ } $HAISI$ or variations
    text = re.sub(r'\$100[.,]000\\text\{\s*\}\s*\$HAISI\$', r'100,000 $HAISI', text)
    text = re.sub(r'\$100[.,]000\s*\$HAISI\$', r'100,000 $HAISI', text)

    # In Vietnamese / other languages:
    # **$$\n\n50.000.000\text{ USD}$**
    text = re.sub(r'\*\*\$\$\s*\n+\s*50\.000\.000(?:\\text\{\s*USD\s*\})?\$?\*\*', r'**$50.000.000 USD**', text)
    text = re.sub(r'\*\*\s*\n+\s*\$\$25\.000(?:\\text\{\s*USD\s*\})?\$?\*\*', r'**$25.000 USD**', text)
    text = re.sub(r'khối lượng\s*\$\$\s*\n+\s*50\.000\.000(?:\\text\{\s*USD\s*\})?\$?', r'khối lượng $50.000.000 USD', text)
    text = re.sub(r'\$\$50\.000(?:\\text\{\s*USD\s*\})?\$', r'$50.000 USD', text)

    # Also in Daily Transaction Allowance:
    # \text{Daily Transaction Allowance} = k \cdot \sqrt{\text{Staked } $HAISI \times \text{Lock Duration}}
    # Inside LaTeX math mode, $HAISI should be \text{\$HAISI}
    text = text.replace(r'\text{Staked } $HAISI', r'\text{Staked \$HAISI}')
    text = text.replace(r'\text{Staked } \$HAISI', r'\text{Staked \$HAISI}')
    text = text.replace(r'$HAISI \times', r'\$HAISI \times')

    # Also check:
    # WAN latencies: Wide-Area Networks (WAN) operate with $20\text{ ms} - 120\text{ ms}$
    # In math mode, that's fine as long as $20 isn't replaced with &#36;20!

    if text != orig:
        print(f"[{lang}] Section 8 fixes applied.")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        app_path = os.path.join('app', path)
        with open(app_path, 'w', encoding='utf-8') as f:
            f.write(text)
    else:
        print(f"[{lang}] No changes needed.")
