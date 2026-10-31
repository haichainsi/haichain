#!/usr/bin/env node
/**
 * HAICHAIN 1-Click Auto-Installer for Claude Desktop & Cursor
 * Automatically detects OS, resolves local paths, and injects HAICHAIN MCP into Claude Desktop config.
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

function getClaudeConfigPath() {
  const platform = process.platform;
  const home = os.homedir();

  if (platform === 'win32') {
    const appData = process.env.APPDATA || path.join(home, 'AppData', 'Roaming');
    return path.join(appData, 'Claude', 'claude_desktop_config.json');
  } else if (platform === 'darwin') {
    return path.join(home, 'Library', 'Application Support', 'Claude', 'claude_desktop_config.json');
  } else {
    return path.join(home, '.config', 'Claude', 'claude_desktop_config.json');
  }
}

function install() {
  console.log('\n======================================================');
  console.log('  HAICHAIN 1-Click Claude Desktop MCP Auto-Installer');
  console.log('======================================================\n');

  const configPath = getClaudeConfigPath();
  const configDir = path.dirname(configPath);

  // Compute portable path to mcp-server/dist/index.js
  const rootDir = path.resolve(__dirname, '..');
  const serverJsPath = path.resolve(rootDir, 'mcp-server', 'dist', 'index.js').replace(/\\/g, '/');

  if (!fs.existsSync(serverJsPath)) {
    console.error(`[ERROR] Compiled MCP server not found at: ${serverJsPath}`);
    console.error('Please run "npm run build --prefix mcp-server" first.');
    process.exit(1);
  }

  // Ensure Claude config directory exists
  if (!fs.existsSync(configDir)) {
    fs.mkdirSync(configDir, { recursive: true });
    console.log(`[Created Directory] ${configDir}`);
  }

  let config = { mcpServers: {} };
  if (fs.existsSync(configPath)) {
    try {
      const raw = fs.readFileSync(configPath, 'utf8');
      config = JSON.parse(raw);
      if (!config.mcpServers) config.mcpServers = {};
    } catch (e) {
      console.warn(`[Warning] Could not parse existing config (${e.message}). Backing up...`);
      fs.copyFileSync(configPath, configPath + '.backup-' + Date.now());
    }
  }

  // Inject HAICHAIN MCP Server
  config.mcpServers.haichain = {
    command: 'node',
    args: [serverJsPath],
    env: {
      SOLANA_RPC_URL: 'https://api.devnet.solana.com'
    }
  };

  fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf8');

  console.log(`[SUCCESS] HAICHAIN MCP Server successfully installed into:`);
  console.log(`  -> ${configPath}\n`);
  console.log('Configuration Injected:');
  console.log(JSON.stringify(config.mcpServers.haichain, null, 2));
  console.log('\nNext Step: Simply restart Claude Desktop. HAICHAIN tools are ready!\n');
}

install();
