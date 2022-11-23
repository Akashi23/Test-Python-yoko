terraform {
  backend "s3" {
    endpoint                = "fra1.digitaloceanspaces.com"
    key                     = "terraform.tfstate"
    bucket                  = "terraformstatesaves"
    region                  = "us-west-1"
    skip_requesting_account_id = true
    skip_credentials_validation = true
    skip_get_ec2_platforms = true
    skip_metadata_api_check = true
  }
}

resource "digitalocean_app" "yoko-test-api" {
  spec {
    name   = "yoko-test-api"
    region = "fra"
    
    domain {
      name = "yoko.akashi23.me"
      type = "PRIMARY"
      zone = "akashi23.me"
    }

    env {
      key   = "PORT"
      value = "8080"
    }

    routes {
        path = "/api"
      }

    service {
      name               = "yoko-test-api"
      instance_count     = 1
      instance_size_slug = "basic-xxs"
      http_port          = 8080

      image {
        registry_type = "DOCR"
        repository    = "yoko-test-api"
        tag           = "latest"
      }
    }
  }
}
