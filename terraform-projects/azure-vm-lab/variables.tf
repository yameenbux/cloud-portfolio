variable "resource_group_name" {
  description = "Name of the Resource Group"
  type        = string
  default     = "lab-rg"
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "UK South"
}

variable "admin_username" {
  description = "Admin username for the VM"
  type        = string
  default     = "azureuser"
}

variable "admin_password" {
  description = "Admin password for the VM"
  type        = string
  sensitive   = true
}
