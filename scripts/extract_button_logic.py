import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the main script block
scripts = re.findall(r'<script.*?>([\s\S]*?)<\/script>', text)
main_script = scripts[-1]

key_features = [
    'dash-confirm-deposit-btn',
    'dash-confirm-withdraw-btn',
    'confirm-issue-ticket-btn',
    'playground-execute-btn',
    'header-panic-btn',
    'export-ledger-btn',
    'activate-gateway-btn',
    'save-byok-btn',
    'wallet-provider-btn',
    'deposit-connect-btn'
]

results = {}
for feat in key_features:
    idx = main_script.find(feat)
    if idx != -1:
        # get snippet of 500 chars after
        snippet = main_script[idx:idx+1200]
        results[feat] = snippet
    else:
        results[feat] = "NOT FOUND"

with open('scripts/audit_features_output.txt', 'w', encoding='utf-8') as out:
    for k, v in results.items():
        out.write(f"\n==================== {k} ====================\n")
        out.write(v + "\n")

print("Audit analysis written to scripts/audit_features_output.txt")
