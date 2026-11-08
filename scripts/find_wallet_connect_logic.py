import re

def search_wallet_triggers():
    targets = ['dashboard.html', 'index.html', 'sale-controller.js', 'app/sale-controller.js']
    for t in targets:
        print(f"=== {t} ===")
        with open(t, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find buttons with "connect" or "wallet"
        btn_matches = re.findall(r'<button[^>]+(?:wallet|phantom|metamask|solflare|connect)[^>]*>.*?</button>', content, re.IGNORECASE | re.DOTALL)
        for b in btn_matches[:10]:
            clean_b = re.sub(r'\s+', ' ', b)[:150]
            print("  BUTTON:", clean_b)

        # Find event listeners for wallet connection
        listener_matches = re.findall(r'(?:addEventListener\([\'"]click[\'"]|\.onclick\s*=).*?(?:phantom|metamask|solana|ethereum|wallet)', content, re.IGNORECASE)
        for l in listener_matches[:10]:
            clean_l = re.sub(r'\s+', ' ', l)[:120]
            print("  LISTENER:", clean_l)

if __name__ == '__main__':
    search_wallet_triggers()
