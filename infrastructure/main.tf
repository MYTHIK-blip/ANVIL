# Terraform configuration for deploying Anvil infrastructure
# e.g., VPS, Database, Storage Bucket

provider "google" {
  project = "your-gcp-project-id"
  region  = "australia-southeast1"
}

resource "google_compute_instance" "anvil_vps" {
  name         = "anvil-server"
  machine_type = "e2-medium"
  # ... further configuration needed
}
