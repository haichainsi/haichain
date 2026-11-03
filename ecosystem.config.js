/**
 * ==============================================================================
 * HAIChain Production PM2 Process Manager Configuration
 * ==============================================================================
 * Usage:
 *   pm2 start ecosystem.config.js
 *   pm2 save
 *   pm2 startup
 */

module.exports = {
  apps: [
    {
      name: 'haichain-gateway',
      script: './server/production-agent-relayer.js',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '500M',
      env: {
        PORT: 8080,
        NODE_ENV: 'production',
        SOLANA_CLUSTER: 'devnet',
        SOLANA_RPC_URL: 'https://api.devnet.solana.com'
      },
      error_file: './logs/gateway-err.log',
      out_file: './logs/gateway-out.log',
      log_file: './logs/gateway-combined.log',
      time: true
    }
  ]
};
