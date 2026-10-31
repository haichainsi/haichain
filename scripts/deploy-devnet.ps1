# scripts/deploy-devnet.ps1
# HAICHAIN v6.9.3: Automated Solana Devnet Deployment & Setup Helper

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "            HAICHAIN: 1-CLICK SOLANA DEVNET ORCHESTRATION SCRIPT                " -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Run Node/TS Deployment Orchestrator
Write-Host "[*] Executing TypeScript Devnet Orchestrator..." -ForegroundColor Yellow
cmd.exe /c "npx ts-node scripts/deploy-devnet.ts"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[-] Failed to run TypeScript orchestrator." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[+] Pre-deployment configuration verified." -ForegroundColor Green
Write-Host "[*] Check 'devnet-deployment.json' and '.env.devnet' for generated program and wallet keys." -ForegroundColor White
Write-Host ""
