# -*- coding: utf-8 -*-
import urllib.request, time

url = 'https://haichain.si/?v=test_' + str(int(time.time()))
for attempt in range(15):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content_type = resp.headers.get('content-type', '')
            body = resp.read().decode('utf-8', errors='ignore')
            if 'text/html' in content_type and '<!DOCTYPE html>' in body and 'HAICHAIN' in body:
                print(f'Attempt {attempt+1}: SUCCESS! haichain.si is serving HTML website!')
                idx = body.find('<title>')
                if idx != -1:
                    print(body[idx:idx+100])
                break
            else:
                print(f'Attempt {attempt+1}: Content-Type: {content_type}, waiting 5s...')
    except Exception as e:
        print(f'Attempt {attempt+1}: Error {e}')
    time.sleep(5)
