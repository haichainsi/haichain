import json, os

manifest_content = {
  "name": "HAICHAIN - The Economic Bedrock for the Symbiotic Superintelligence Era AI²",
  "short_name": "HAICHAIN",
  "description": "The Economic Bedrock for the Symbiotic Superintelligence Era AI². Empowering billions of autonomous AI agents and robots to co-create wealth under sovereign human ownership.",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#09090b",
  "theme_color": "#09090b",
  "icons": [
    {
      "src": "/assets/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/assets/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/assets/icon-maskable-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable"
    },
    {
      "src": "/assets/icon-maskable-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    },
    {
      "src": "/apple-touch-icon.png",
      "sizes": "180x180",
      "type": "image/png",
      "purpose": "any"
    }
  ],
  "categories": ["finance", "utilities", "productivity"]
}

formatted = json.dumps(manifest_content, indent=2, ensure_ascii=False) + "\n"

targets = ['manifest.json', 'site.webmanifest', 'app/manifest.json', 'app/site.webmanifest']

for t in targets:
    with open(t, 'w', encoding='utf-8') as f:
        f.write(formatted)
    print(f"Updated {t}")
