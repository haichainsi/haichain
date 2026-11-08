import re

with open("dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

tabs = re.findall(r'id=["\']tab-[^"\']+["\']', content)
print("Tabs:", set(tabs))

# Check for keywords like velocity, heartbeat, invariant, or where stats are displayed
matches = re.findall(r'<div[^>]+id=["\']([^"\']*(?:stat|metric|vault|pot|cap|agent)[^"\']*)["\']', content, re.IGNORECASE)
print("Relevant IDs:", set(matches[:25]))

# Look for tabs navigation
nav_tabs = re.findall(r'data-tab=["\']([^"\']+)["\']', content)
print("Data tabs:", set(nav_tabs))
