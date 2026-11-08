import os

fp = 'server/haichain-mcp-worker.js'
with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

target = """async function handleExecuteMicroPayment(args = {}) {
  const amount = typeof args.amountUsdt === 'number' ? args.amountUsdt : 0.002;
  const description = args.actionDescription || 'Autonomous AI Task Compensation';
  const recipient = args.merchantRecipient || TREASURY_ADDRESS;"""

replacement = """async function handleExecuteMicroPayment(args = {}) {
  const rawAmount = typeof args.amountUsdt === 'number' ? args.amountUsdt
                  : typeof args.amount === 'number' ? args.amount
                  : typeof args.amount_usdt === 'number' ? args.amount_usdt
                  : parseFloat(args.amountUsdt || args.amount || args.amount_usdt || 0.005);
  const amount = isNaN(rawAmount) || rawAmount <= 0 ? 0.005 : rawAmount;
  const description = args.actionDescription || args.description || args.service || args.task || 'DeepSeek AI Inference Settlement';
  const recipient = args.merchantRecipient || args.recipient || args.to || args.recipientAddress || TREASURY_ADDRESS;"""

if target in content:
    content = content.replace(target, replacement)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully patched handleExecuteMicroPayment in", fp)
else:
    print("Target not found in", fp)
