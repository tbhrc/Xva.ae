# PowerShell script to start the API server
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Starting API Server for Lead Capture" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Server will run on http://localhost:5000" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Change to the iaiv3 directory
Set-Location -Path "$PSScriptRoot\iaiv3"

# Start the API server
python api_server.py
