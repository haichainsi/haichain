@echo off
echo =======================================================
echo   HAICHAIN - ONE-CLICK AUTO SYNC (LOCAL -> GITHUB -> CLOUDFLARE)
echo =======================================================
echo.
echo [1/3] Staging all local updates...
git add .

echo [2/3] Committing changes...
git commit -m "update: sync local changes to production"

echo [3/3] Pushing to GitHub (origin main)...
git push origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =======================================================
    echo   SUCCESS! PUSH COMPLETED TO GITHUB!
    echo   Cloudflare Pages is now auto-deploying to your domain.
    echo =======================================================
) else (
    echo.
    echo [ERROR] Push failed. Please verify your GitHub login via 'gh auth login'.
)
pause
