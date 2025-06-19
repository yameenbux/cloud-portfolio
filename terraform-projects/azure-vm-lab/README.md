# 💻 Azure VM Terraform Lab

This lab demonstrates how to provision a basic Virtual Machine on Microsoft Azure using Terraform.

## 📦 Project Structure

- `main.tf` – Core infrastructure definition
- `variables.tf` – Input variables
- `terraform.tfvars` – Variable values
- `outputs.tf` – Outputs like public IP, VM name, etc.

## ✅ What This Deploys

- A new Resource Group
- Virtual Network & Subnet
- Network Interface
- Public IP Address
- Virtual Machine (Ubuntu or your selected image)
- Network Security Group with SSH access

## 🚀 Getting Started

1. **Navigate to the directory:**

   ```bash
   cd terraform-projects/azure-vm-lab
