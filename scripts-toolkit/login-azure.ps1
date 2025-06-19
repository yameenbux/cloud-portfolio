# This script logs you into Azure and sets your active subscription

# Connect to Azure account interactively
Connect-AzAccount

# Set the default subscription to use
Set-AzContext -SubscriptionId "<your-subscription-id>"

## Connect-AzAccount → Opens a login prompt for Azure.

## Set-AzContext → Sets the Azure subscription you'll run all future commands against.