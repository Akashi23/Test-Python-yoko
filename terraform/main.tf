terraform {
  backend "s3" {
    endpoint                = "fra1.digitaloceanspaces.com"
    key                     = "yokotest/terraform.tfstate"
    bucket                  = "terraformstatesaves"
    region                  = "us-west-1"
    skip_requesting_account_id = true
    skip_credentials_validation = true
    skip_get_ec2_platforms = true
    skip_metadata_api_check = true
  }
}
