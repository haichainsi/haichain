import os
import json
import re

print("=== 1. Updating i18n.js & app/i18n.js ===")
translations_map = [
    ('    "nav.sovereignL1": "Егемен L1",', '    "nav.sovereignL1": "Егемен L1",\n    "nav.developers": "Әзірлеушілер",'),
    ('    "nav.sovereignL1": "Sovereign L1",\n    "nav.whitepaper": "Whitepaper",', '    "nav.sovereignL1": "Sovereign L1",\n    "nav.developers": "Developers",\n    "nav.whitepaper": "Whitepaper",'),
    ('    "nav.sovereignL1": "主权 L1",', '    "nav.sovereignL1": "主权 L1",\n    "nav.developers": "开发者",'),
    ('    "nav.sovereignL1": "L1 Souverain",', '    "nav.sovereignL1": "L1 Souverain",\n    "nav.developers": "Développeurs",'),
    ('    "nav.sovereignL1": "소버린 L1",', '    "nav.sovereignL1": "소버린 L1",\n    "nav.developers": "개발자",'),
    ('    "nav.sovereignL1": "L1 Soberana",', '    "nav.sovereignL1": "L1 Soberana",\n    "nav.developers": "Desarrolladores",'),
    ('    "nav.sovereignL1": "Суверенный L1",', '    "nav.sovereignL1": "Суверенный L1",\n    "nav.developers": "Разработчикам",'),
    ('    "nav.sovereignL1": "Sovereign L1",\n    "nav.whitepaper": "Sách Trắng",', '    "nav.sovereignL1": "Sovereign L1",\n    "nav.developers": "Lập trình viên",\n    "nav.whitepaper": "Sách Trắng",'),
    ('    "nav.sovereignL1": "सॉवरेन L1",', '    "nav.sovereignL1": "सॉवरेन L1",\n    "nav.developers": "डेवलपर्स",'),
    ('    "nav.sovereignL1": "L1 ריבוני",', '    "nav.sovereignL1": "L1 ריבוני",\n    "nav.developers": "מפתחים",'),
]

for filepath in ['i18n.js', 'app/i18n.js']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '"nav.developers":' not in content:
        for old, new in translations_map:
            content = content.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath} with nav.developers")
    else:
        print(f"{filepath} already has nav.developers")

print("\n=== 2. Updating index.html & app/index.html Navbar & Mobile Drawer & Footer ===")
nav_desktop_old = '<a href="#endgame" class="hover:text-black dark:hover:text-white transition-colors" data-i18n="nav.sovereignL1">Sovereign L1</a>'
nav_desktop_new = '<a href="#endgame" class="hover:text-black dark:hover:text-white transition-colors" data-i18n="nav.sovereignL1">Sovereign L1</a>\n\n        <a href="/dashboard?tab=mcp" class="hover:text-black dark:hover:text-white transition-colors" data-i18n="nav.developers">Developers</a>'

nav_mobile_old = '<a href="#endgame" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white transition-colors" data-i18n="nav.sovereignL1">Sovereign L1 Roadmap</a>'
nav_mobile_new = '<a href="#endgame" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white transition-colors" data-i18n="nav.sovereignL1">Sovereign L1 Roadmap</a>\n      <a href="/dashboard?tab=mcp" class="mobile-nav-link block py-2.5 cursor-pointer touch-manipulation text-neutral-800 dark:text-neutral-200 hover:text-black dark:hover:text-white transition-colors" data-i18n="nav.developers">Developers</a>'

footer_old = '<a href="#endgame" class="hover:text-black dark:hover:text-white transition-colors" data-i18n="nav.sovereignL1">Sovereign L1</a>'
# For footer, we can replace the occurrence inside <footer>
for filepath in ['index.html', 'app/index.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'href="/dashboard?tab=mcp"' not in html:
        # replace desktop nav
        html = html.replace(nav_desktop_old, nav_desktop_new, 1)
        # replace mobile nav
        html = html.replace(nav_mobile_old, nav_mobile_new, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath} with Developers links")
    else:
        print(f"{filepath} already has Developers links")

print("\n=== 3. Updating dashboard.html & app/dashboard.html MCP snippets ===")
clean_json_snippet = '''{
  "mcpServers": {
    "haichain": {
      "command": "npx",
      "args": ["-y", "@haichain/mcp-server"],
      "env": {
        "SOLANA_RPC_URL": "https://api.devnet.solana.com",
        "HAICHAIN_PROGRAM_ID": "DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk"
      }
    }
  }
}'''

clean_json_copy_str = '{\\n  "mcpServers": {\\n    "haichain": {\\n      "command": "npx",\\n      "args": ["-y", "@haichain/mcp-server"],\\n      "env": {\\n        "SOLANA_RPC_URL": "https://api.devnet.solana.com",\\n        "HAICHAIN_PROGRAM_ID": "DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk"\\n      }\\n    }\\n  }\\n}'

for filepath in ['dashboard.html', 'app/dashboard.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        dash = f.read()
    
    # 1. Replace hardcoded path in tab-mcp pre block
    dash = re.sub(
        r'("command":\s*"node",\s*"args":\s*\[\s*")[^"]*mcp-server/dist/index\.js("\s*\])',
        r'"command": "npx",\n      "args": [\n        "-y",\n        "@haichain/mcp-server"\n      ]',
        dash
    )
    
    # 2. Replace hardcoded path in mcp-json-snippet pre block
    dash = re.sub(
        r'("command":\s*"node",\s*"args":\s*\[")[^"]*mcp-server/dist/index\.js("\])',
        r'"command": "npx",\n      "args": ["-y", "@haichain/mcp-server"]',
        dash
    )

    # 3. Replace claudeConfigJson in javascript
    dash = re.sub(
        r'"command":\s*"node",\s*"args":\s*\["[^"]*mcp-server/dist/index\.js"\]',
        r'"command": "npx",\n          "args": ["-y", "@haichain/mcp-server"]',
        dash
    )

    # 4. Replace copyMcpCodeBtn string
    dash = dash.replace(
        '"command": "node",\\n      "args": ["@haichain/mcp-server/dist/index.js"]',
        '"command": "npx",\\n      "args": ["-y", "@haichain/mcp-server"]'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(dash)
    print(f"Updated {filepath} MCP snippets")

print("\n=== 4. Updating claude_desktop_config.json ===")
config_data = {
    "mcpServers": {
        "haichain": {
            "command": "npx",
            "args": ["-y", "@haichain/mcp-server"],
            "env": {
                "SOLANA_RPC_URL": "https://api.devnet.solana.com",
                "HAICHAIN_PROGRAM_ID": "DK4QA3WK49SWR86GsqDRQSVNhoVRe1MMQGYZ7hKJw4xk"
            }
        }
    }
}

os.makedirs('download', exist_ok=True)
os.makedirs('app/download', exist_ok=True)

with open('claude_desktop_config.json', 'w', encoding='utf-8') as f:
    json.dump(config_data, f, indent=2)
with open('app/claude_desktop_config.json', 'w', encoding='utf-8') as f:
    json.dump(config_data, f, indent=2)
with open('download/claude_desktop_config.json', 'w', encoding='utf-8') as f:
    json.dump(config_data, f, indent=2)
with open('app/download/claude_desktop_config.json', 'w', encoding='utf-8') as f:
    json.dump(config_data, f, indent=2)

print("Saved claude_desktop_config.json to root, app/, download/, and app/download/")
