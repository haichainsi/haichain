import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

alert_replacements = [
    "alert(getDashNotice('faucetClaimed') + '\\n\\n+' + added.toFixed(2) + ' USDT (Solana Devnet)');",
    "alert(getDashNotice('metaMaskInsufficientEth'));",
    "alert(getDashNotice('metaMaskDepositSuccess'));",
    "alert(getDashNotice('noWeb3DetectedFaucetGuide'));",
    "alert(getDashNotice('insufficientSolGaslessGuide'));",
    "alert(getDashNotice('web3DepositConfirmedDevnet'));",
    "alert(getDashNotice('fiatSandboxNotice'));",
    "alert(getDashNotice('invalidSolanaAddress'));",
    "alert(getDashNotice('withdrawSuccessNotice'));",
]

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace 9 alerts in reverse order of appearance
    alert_matches = list(re.finditer(r'alert\(isVi\s*\?[\s\S]*?\);', text))
    if len(alert_matches) == 9:
        for m, repl in zip(reversed(alert_matches), reversed(alert_replacements)):
            text = text[:m.start()] + repl + text[m.end():]
        print(f'{filepath}: Replaced all 9 alerts successfully!')
    else:
        print(f'{filepath}: Expected 9 alerts, found {len(alert_matches)}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

patch_file('dashboard.html')
patch_file('app/dashboard.html')
