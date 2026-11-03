import re

for path in ['dashboard.html', 'app/dashboard.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add providerUrl to GLOBAL_MARKET_AGENTS
    content = content.replace(
        "provider: 'Smithery MCP Registry',",
        "provider: 'Smithery MCP Registry',\n        providerUrl: 'https://smithery.ai',"
    )
    content = content.replace(
        "provider: 'Fetch.ai Almanac Network',",
        "provider: 'Fetch.ai Almanac Network',\n        providerUrl: 'https://agentverse.ai',"
    )
    content = content.replace(
        "provider: 'Glama Security Network',",
        "provider: 'Glama Security Network',\n        providerUrl: 'https://glama.ai/mcp/servers',"
    )
    content = content.replace(
        "provider: 'Fetch.ai uAgents Protocol',",
        "provider: 'Fetch.ai uAgents Protocol',\n        providerUrl: 'https://agentverse.ai',"
    )

    # 2. Update card provider rendering in renderGlobalAgentMarketplace
    old_badge_span = """              <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate max-w-[170px]">
                ${agent.provider}
              </span>"""

    new_badge_link = """              ${agent.providerUrl ? `
                <a href="${agent.providerUrl}" target="_blank" class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate hover:text-black dark:hover:text-white flex items-center space-x-1">
                  <span>${agent.provider}</span>
                  <i data-lucide="external-link" class="w-2.5 h-2.5 inline-block"></i>
                </a>
              ` : `
                <span class="text-[9px] font-mono px-2 py-0.5 rounded-full bg-neutral-200 dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 font-semibold truncate">
                  ${agent.provider}
                </span>
              `}"""

    if old_badge_span in content:
        content = content.replace(old_badge_span, new_badge_link)
        print(f"Updated badge rendering in {path}")
    else:
        print(f"Notice: old badge span not found in {path}")

    # 3. Ensure icons re-render in renderGlobalAgentMarketplace
    icon_hook = "grid.innerHTML = filtered.map(agent => `"
    if icon_hook in content and "safeCreateIcons()" not in content[content.find(icon_hook):content.find(icon_hook)+4000]:
        old_render_end = "hireBtns.forEach(btn => {"
        new_render_end = "if (typeof safeCreateIcons === 'function') safeCreateIcons(); else if (window.lucide) window.lucide.createIcons();\n\n      hireBtns.forEach(btn => {"
        if old_render_end in content:
            content = content.replace(old_render_end, new_render_end, 1)
            print(f"Added safeCreateIcons call in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Finished {path}")

print("Done!")
