import sys
sys.stdout.reconfigure(encoding='utf-8')

for s in ['scripts/patch_worker_saft.py', 'scripts/add_resend_to_worker.py']:
    print('=== ' + s + ' ===')
    try:
        with open(s, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(e)
