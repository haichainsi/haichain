import os

print("Listing packages/agent-pay-python:")
for root, dirs, files in os.walk('packages/agent-pay-python'):
    print(root, dirs, files)

with open('packages/agent-pay-python/pyproject.toml', 'r', encoding='utf-8') as f:
    print("\npyproject.toml content:")
    print(f.read())
