import sys, re
sys.stdout.reconfigure(encoding='utf-8')

SEO_HEAD_BLOCK = '''  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HAICHAIN - The Economic Bedrock for the Symbiotic Superintelligence Era AI²</title>
  <meta name="description" content="HAICHAIN: The financial operating system for the autonomous machine era today. The economic bedrock for the symbiotic superintelligence era AI² tomorrow. Empowering billions of AI agents and robots to co-create wealth under sovereign human ownership.">
  <meta name="application-name" content="HAICHAIN">
  <meta name="apple-mobile-web-app-title" content="HAICHAIN">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#09090b">

  <!-- Hreflang Multi-Language SEO Canonicals -->
  <link rel="canonical" href="https://haichain.si/">
  <link rel="alternate" hreflang="x-default" href="https://haichain.si/">
  <link rel="alternate" hreflang="en" href="https://haichain.si/?lang=en">
  <link rel="alternate" hreflang="vi" href="https://haichain.si/?lang=vi">
  <link rel="alternate" hreflang="zh" href="https://haichain.si/?lang=zh">
  <link rel="alternate" hreflang="es" href="https://haichain.si/?lang=es">
  <link rel="alternate" hreflang="fr" href="https://haichain.si/?lang=fr">
  <link rel="alternate" hreflang="ru" href="https://haichain.si/?lang=ru">
  <link rel="alternate" hreflang="ko" href="https://haichain.si/?lang=ko">
  <link rel="alternate" hreflang="hi" href="https://haichain.si/?lang=hi">
  <link rel="alternate" hreflang="he" href="https://haichain.si/?lang=he">
  <link rel="alternate" hreflang="kk" href="https://haichain.si/?lang=kk">

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
  <meta property="og:title" content="HAICHAIN - The Economic Bedrock for the Symbiotic Superintelligence Era AI²">
  <meta property="og:description" content="HAICHAIN: The financial operating system for the autonomous machine era today. The economic bedrock for the symbiotic superintelligence era AI² tomorrow.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://haichain.si/">
  <meta property="og:image" content="https://haichain.si/assets/icon-512.png">
  <meta property="og:image:secure_url" content="https://haichain.si/assets/icon-512.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="512">
  <meta property="og:image:height" content="512">
  <meta property="og:image:alt" content="HAICHAIN Official Web3 Logo">

  <!-- Twitter Card Metadata -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="HAICHAIN - The Economic Bedrock for the Symbiotic Superintelligence Era AI²">
  <meta name="twitter:description" content="HAICHAIN: The financial operating system for the autonomous machine era today. The economic bedrock for the symbiotic superintelligence era AI² tomorrow.">
  <meta name="twitter:image" content="https://haichain.si/assets/icon-512.png">

  <!-- AEO, SEO & GEO Comprehensive Semantic Structured Data (Schema.org JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": "https://haichain.si/#website",
        "url": "https://haichain.si/",
        "name": "HAICHAIN",
        "description": "The Financial Operating System for the Autonomous Machine Era today. The Economic Bedrock for the Symbiotic Superintelligence Era AI² tomorrow.",
        "inLanguage": ["en", "vi", "zh", "es", "fr", "ru", "ko", "hi", "he", "kk"]
      },
      {
        "@type": "Organization",
        "@id": "https://haichain.si/#organization",
        "name": "HAICHAIN",
        "url": "https://haichain.si/",
        "logo": "https://haichain.si/assets/icon-512.png",
        "slogan": "The Economic Bedrock for the Symbiotic Superintelligence Era AI²",
        "knowsAbout": [
          "Autonomous Machine Economy",
          "Symbiotic Superintelligence",
          "AI Agent Financial Layer",
          "Solana SVM Micropayments",
          "Non-custodial Petty Cash Vaults",
          "Biometric Passkey Sovereign Alignment"
        ]
      },
      {
        "@type": "SoftwareApplication",
        "@id": "https://haichain.si/#software",
        "name": "HAICHAIN Autonomous Machine Financial OS",
        "applicationCategory": "FinanceApplication, BusinessApplication, DeveloperApplication",
        "operatingSystem": "Solana SVM, Web3, Agent Infrastructure",
        "description": "Financial operating system empowering billions of autonomous AI agents and robotics to transact safely via nano-cent micropayment rails while ensuring sovereign human ownership.",
        "offers": {
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "USD"
        }
      },
      {
        "@type": "FAQPage",
        "@id": "https://haichain.si/#faq",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "HAICHAIN là gì? / What is HAICHAIN?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "HAICHAIN là Hệ điều hành tài chính cho kỷ nguyên máy tự hành hôm nay và Nền tảng kinh tế cho kỷ nguyên siêu trí tuệ cộng sinh AI² ngày mai. Hệ thống cung cấp két tiêu vặt an toàn và hạ tầng vi thanh toán nano-cent cho các tác nhân AI Agent và Robot tự hành, đảm bảo toàn bộ của cải và quyền làm chủ tối thượng mãi mãi thuộc về con người."
            }
          },
          {
            "@type": "Question",
            "name": "What is the core mission and evolutionary vision of HAICHAIN?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "HAICHAIN empowers billions of autonomous AI agents and AI robots to freely work, transact, and unite with human real-world intelligence to co-create wealth—with all wealth and sovereign ownership forever belonging to humanity. Starting as safe petty cash vaults for AI bots today; scaling into the universal financial and settlement layer for trillions of autonomous machines tomorrow."
            }
          },
          {
            "@type": "Question",
            "name": "How does HAICHAIN eliminate financial risk when AI agents operate autonomously?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "HAICHAIN introduces hardware-enforced non-custodial petty cash vaults, strict daily programmatic spending limits, vendor whitelisting, and a master biometric Passkey kill-switch. This prevents prompt injection exploits and model hallucinations from draining treasury capital."
            }
          },
          {
            "@type": "Question",
            "name": "Khái niệm Siêu Trí Tuệ Cộng Sinh (Symbiotic Superintelligence - AI²) là gì?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Siêu Trí Tuệ Cộng Sinh (AI²) là mô hình hợp nhất nơi trí thông minh nhân tạo và năng lực lao động 24/7 của máy móc kết hợp chặt chẽ với ý thức, đạo đức và quyền làm chủ tối thượng của con người. Máy móc tạo ra của cải với tốc độ ánh sáng, nhưng con người nắm giữ quyền sở hữu và hưởng lợi vĩnh viễn."
            }
          }
        ]
      }
    ]
  }
  </script>
'''

HERO_HTML_REPLACEMENT = '''      <!-- Sub-badge -->
      <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full border border-neutral-300/80 dark:border-neutral-800 bg-white/95 dark:bg-neutral-950/90 backdrop-blur-md text-xs font-mono text-neutral-900 dark:text-neutral-200 mb-8 shadow-md">
        <span class="w-1.5 h-1.5 rounded-full bg-black dark:bg-white animate-pulse"></span>
        <span data-i18n="hero.badge">THE FINANCIAL OPERATING SYSTEM FOR THE AUTONOMOUS MACHINE ERA</span>
      </div>

      <!-- Main Headline -->
      <h1 class="text-2xl sm:text-4xl md:text-5xl font-bold tracking-tight text-neutral-950 dark:text-white max-w-4xl mx-auto leading-[1.22] sm:leading-[1.18] drop-shadow-[0_1px_3px_rgba(255,255,255,0.9)] dark:drop-shadow-[0_3px_18px_rgba(0,0,0,0.85)]" data-i18n="hero.title">
        The Economic Bedrock for the Symbiotic Superintelligence Era AI²
      </h1>

      <!-- Subheadline -->
      <p class="mt-3.5 sm:mt-6 text-sm sm:text-base md:text-lg text-neutral-700 dark:text-neutral-300 max-w-xl sm:max-w-2xl mx-auto font-normal leading-relaxed drop-shadow-[0_1px_2px_rgba(255,255,255,0.8)] dark:drop-shadow-[0_2px_10px_rgba(0,0,0,0.8)]" data-i18n="hero.subtitle">
        Empowering billions of autonomous AI agents and AI robots to freely work, transact, and unite with human real-world intelligence to co-create wealth—with all wealth and sovereign ownership forever belonging to humanity. The financial operating system for the autonomous machine era today. The economic bedrock for the symbiotic superintelligence era AI² tomorrow.
      </p>'''

def update_index_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update <head> metadata block
    head_start = content.find('<head>')
    fonts_pos = content.find('<!-- Fonts')
    if head_start != -1 and fonts_pos != -1:
        crlf = '\r\n' in content[:500]
        replacement = ('<head>\n' + SEO_HEAD_BLOCK + '\n').replace('\r\n', '\n')
        if crlf:
            replacement = replacement.replace('\n', '\r\n')
        content = content[:head_start] + replacement + content[fonts_pos:]

    # 2. Update Hero Section HTML (between <!-- Sub-badge --> and <!-- Primary Action CTAs -->)
    hero_badge_match = re.search(r'<!-- Sub-badge -->.*?<!-- Primary Action CTAs -->', content, re.DOTALL)
    if hero_badge_match:
        crlf = '\r\n' in content[:500]
        replacement = (HERO_HTML_REPLACEMENT + '\n\n      <!-- Primary Action CTAs -->').replace('\r\n', '\n')
        if crlf:
            replacement = replacement.replace('\n', '\r\n')
        content = content[:hero_badge_match.start()] + replacement + content[hero_badge_match.end():]
        print(f"Updated Hero Section in {path}")
    else:
        print(f"Warning: Could not find Hero Section block in {path}")

    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print(f"Updated {path} successfully.")

def update_dashboard_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update <head> metadata
    head_start = content.find('<head>')
    fonts_pos = content.find('<!-- Fonts')
    if head_start != -1 and fonts_pos != -1:
        crlf = '\r\n' in content[:500]
        replacement = ('<head>\n' + SEO_HEAD_BLOCK + '\n').replace('\r\n', '\n')
        if crlf:
            replacement = replacement.replace('\n', '\r\n')
        content = content[:head_start] + replacement + content[fonts_pos:]

    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print(f"Updated {path} successfully.")

update_index_file('index.html')
update_index_file('app/index.html')
update_dashboard_file('dashboard.html')
update_dashboard_file('app/dashboard.html')
