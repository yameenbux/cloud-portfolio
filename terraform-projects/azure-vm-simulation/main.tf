provider "azurerm" {
  features {}
 subscription_id = "00000000-0000-0000-0000-000000000000" # fake UUID
}

resource "azurerm_resource_group" "rg" {
  name     = "demo-rg"
  location = "UK South"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "demo-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}
