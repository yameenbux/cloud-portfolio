# This script shows Azure usage costs from the last 30 days

# Fetch usage details and cost
Get-AzConsumptionUsageDetail `
    -StartDate (Get-Date).AddDays(-30) `
    -EndDate (Get-Date) `
| Select-Object InstanceName, MeterCategory, UsageStart, PretaxCost


## Get-AzConsumptionUsageDetail → Gets Azure billing/usage data.

## Get-Date → Gets today’s date.

## AddDays(-30) → Goes back 30 days.

## Select-Object → Shows key cost breakdown info like cost, start date, resource name.