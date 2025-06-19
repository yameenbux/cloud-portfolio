# This script fetches and lists all Azure resource groups in your subscription

# Get all resource groups and select specific properties to display
Get-AzResourceGroup | Select-Object ResourceGroupName, Location

## Get-AzResourceGroup → Retrieves all resource groups.

## Select-Object → Filters the output to show only the Name and Location.