import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

def show_handler(name, max_len=2000):
    pos = text.find(name)
    print(f"\n==================== {name} (pos: {pos}) ====================")
    if pos != -1:
        print(text[pos:pos+max_len])
    else:
        print("NOT FOUND")

show_handler('dashConfirmWithdrawBtn.addEventListener')
show_handler('headerPanicBtn.addEventListener')
show_handler('playgroundExecuteBtn.addEventListener')
show_handler('confirmIssueTicketBtn')
