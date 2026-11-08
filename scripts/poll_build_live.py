import urllib.request, time, fitz, hashlib

print("Polling Cloudflare Pages until commit 27ea7e6 is deployed live...")

for attempt in range(24):
    ts = int(time.time())
    url = f"https://haichain.si/HAICHAIN_WHITEPAPER_V1.0_FR.pdf?nocache={ts}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache, no-store'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        
        md5_live = hashlib.md5(data).hexdigest()
        local_data = open('HAICHAIN_WHITEPAPER_V1.0_FR.pdf', 'rb').read()
        md5_local = hashlib.md5(local_data).hexdigest()
        
        doc = fitz.open(stream=data, filetype="pdf")
        text = ""
        for p in doc:
            text += p.get_text() + "\n"
        
        has_sys = "Sysvar1nstructions1111111111111111111111111" in text
        has_005 = "0.05%" in text
        
        print(f"[{attempt+1}/24] LIVE FR.pdf len={len(data)} (local={len(local_data)}), match_hash={md5_live == md5_local}, sysvar={has_sys}, fee0.05={has_005}")
        
        if md5_live == md5_local and has_sys and has_005:
            print("\n>>> CLOUDFLARE PAGES BUILD IS DEPLOYED & LIVE! <<<")
            break
    except Exception as e:
        print(f"[{attempt+1}] Error: {e}")
    
    time.sleep(10)
