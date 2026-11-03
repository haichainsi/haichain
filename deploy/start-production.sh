#!/usr/bin/env bash
# ==============================================================================
# HAIChain Production Linux Startup Script (Ubuntu/Debian)
# ==============================================================================
set -e

echo "=== [HAIChain Production Launcher] ==="

# 1. Check Node.js
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed. Please install Node.js 18+."
    exit 1
fi
echo "[OK] Node.js version: $(node -v)"

# 2. Check PM2
if ! command -v pm2 &> /dev/null; then
    echo "Installing PM2 globally..."
    npm install -g pm2
fi

# 3. Create logs directory
mkdir -p logs

# 4. Start with PM2
echo "Starting HAIChain Gateway with PM2..."
pm2 start ecosystem.config.js

# 5. Verify status
pm2 status haichain-gateway

echo ""
echo "=== [HAIChain Gateway is ONLINE on port 8080] ==="
echo "Check health: curl http://127.0.0.1:8080/status"
