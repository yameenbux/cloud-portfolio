# Check-AzureLogin.ps1
# Checks if you're logged into Azure CLI

$account = az account show 2>$null

if ($?) {
    Write-Host "✅ You are logged into Azure as: $($account | ConvertFrom-Json).user.name"
} else {
    Write-Warning "❌ You are not logged in. Run 'az login' to sign in."
}
