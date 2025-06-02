provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-portfolio-demo"
  location = "UK South"
}
