import os

standard_head = '''<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HAICHAIN - Decentralized Superintelligence Operating System</title>
  <meta name="description" content="HAICHAIN: Universal Autonomous Machine Financial & Cognitive Operating System - The Bedrock for Decentralized Superintelligence.">
  <meta name="application-name" content="HAICHAIN">
  <meta name="apple-mobile-web-app-title" content="HAICHAIN">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#09090b">

  <!-- Primary Favicon & Web3 Wallet Icons (Phantom, Solflare, Mobile Scrapers) -->
  <link rel="icon" type="image/x-icon" href="https://haichain.si/favicon.ico">
  <link rel="shortcut icon" href="https://haichain.si/favicon.ico">
  <link rel="icon" type="image/png" sizes="512x512" href="https://haichain.si/assets/icon-512.png">
  <link rel="icon" type="image/png" sizes="192x192" href="https://haichain.si/assets/icon-192.png">
  <link rel="icon" type="image/png" sizes="48x48" href="https://haichain.si/assets/favicon-48x48.png">
  <link rel="icon" type="image/png" sizes="32x32" href="https://haichain.si/assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="https://haichain.si/assets/favicon-16x16.png">
  <link rel="icon" type="image/png" href="https://haichain.si/favicon.png">
  <link rel="apple-touch-icon" href="https://haichain.si/apple-touch-icon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="https://haichain.si/apple-touch-icon.png">
  <link rel="apple-touch-icon" sizes="192x192" href="https://haichain.si/assets/icon-192.png">
  <link rel="apple-touch-icon" sizes="512x512" href="https://haichain.si/assets/icon-512.png">
  <link rel="apple-touch-icon-precomposed" href="https://haichain.si/apple-touch-icon.png">
  <link rel="manifest" href="https://haichain.si/manifest.json">

  <!-- Standard OpenGraph Metadata (Crawled by Phantom, Solflare, Twitter, Telegram, Discord) -->
  <meta property="og:site_name" content="HAICHAIN">
  <meta property="og:title" content="HAICHAIN - Decentralized Superintelligence Operating System">
  <meta property="og:description" content="HAICHAIN: Universal Autonomous Machine Financial & Cognitive Operating System - The Bedrock for Decentralized Superintelligence.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://haichain.si/">
  <meta property="og:image" content="https://haichain.si/assets/icon-512.png">
  <meta property="og:image:secure_url" content="https://haichain.si/assets/icon-512.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="512">
  <meta property="og:image:height" content="512">
  <meta property="og:image:alt" content="HAICHAIN Official Web3 Logo">

  <!-- Twitter Card Metadata -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="HAICHAIN - Decentralized Superintelligence Operating System">
  <meta name="twitter:description" content="HAICHAIN: Universal Autonomous Machine Financial & Cognitive Operating System.">
  <meta name="twitter:image" content="https://haichain.si/assets/icon-512.png">

  '''

for path in ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html']:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    head_idx = content.find('<head>')
    fonts_idx = content.find('<!-- Fonts')
    if head_idx != -1 and fonts_idx != -1:
        crlf = '\r\n' in content[:500]
        replacement = standard_head.replace('\r\n', '\n')
        if crlf:
            replacement = replacement.replace('\n', '\r\n')
        
        new_content = content[:head_idx] + replacement + content[fonts_idx:]
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(new_content)
        print('Successfully updated head in:', path)
    else:
        print('Could not find tags in:', path)
