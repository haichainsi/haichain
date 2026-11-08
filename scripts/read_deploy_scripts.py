for s in ['scripts/check_deployment.py', 'scripts/poll_live_deploy.py']:
    print('=== ' + s + ' ===')
    try:
        with open(s, 'r', encoding='utf-8') as f:
            print(f.read()[:600])
    except Exception as e:
        print(e)
