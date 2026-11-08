const fs = require('fs');

let content = fs.readFileSync('i18n.js', 'utf8');

const start = content.indexOf('const TRANSLATIONS = {');
const end = content.indexOf('function getInitialLanguage()');
let code = content.slice(start, end).trim();
if (code.endsWith(';')) code = code.slice(0, -1);
code = code.replace('const TRANSLATIONS =', 'global.TRANSLATIONS =');
eval(code);

const TRANSLATIONS = global.TRANSLATIONS;
const langs = Object.keys(TRANSLATIONS);

// Keys that MUST strictly remain in English across all languages to preserve standard developer conventions
const enforceEnglishKeys = {
  'dev.pyStep1': 'Step 1: Install official Python SDK',
  'dev.pyStep2': 'Step 2: Add @haichain_paywall decorator to your FastAPI / MCP Agent',
  'dev.pyStep3': 'Step 3: Call paid AI agents with Python HaichainClient',
  'dev.step1Label': 'Step 1: Install package',
  'dev.step2Label': 'Step 2: Add 5 lines of code to your Express server',
  'mcp.sdkTitle': 'TypeScript SDK Integration',
  'mcp.sdkDesc': 'Issue capability tickets and programmatically execute micro-escrows via @haichainsi/sdk:',
  'btn.copyCode': 'Copy Code',
  'mcp.copyJson': 'Copy JSON',
  'mcp.copied': 'Copied!',
  'dev.btnGithub': 'GitHub Repository',
  'dev.cardProgramId': 'Program ID (Anchor)',
  'dev.cardVaultPda': 'Master Vault PDA',
  'dev.cardRecycle': 'Channel Recycling Instruction (extend_channel_reserve)',
  'dev.watchtowerPort': 'Port 8080 / Express Relayer',
  'dev.watchtowerEndpoints': 'Watchtower Daemon Sentinel Endpoints',
  'dev.watchtowerBadge': '● Watchtower Daemon Active (Devnet)'
};

langs.forEach(lang => {
  if (TRANSLATIONS[lang]) {
    for (const [key, val] of Object.entries(enforceEnglishKeys)) {
      TRANSLATIONS[lang][key] = val;
    }
  }
});

// Serialize back cleanly
const newTranslationsCode = 'const TRANSLATIONS = ' + JSON.stringify(TRANSLATIONS, null, 2) + ';\n\n';
const newContent = content.slice(0, start) + newTranslationsCode + content.slice(end);

fs.writeFileSync('i18n.js', newContent, 'utf8');
console.log('Successfully updated i18n.js with canonical English developer programming steps!');
