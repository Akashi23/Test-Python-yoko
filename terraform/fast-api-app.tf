resource "digitalocean_app" "yoko-test-api" {
  spec {
    name   = "yoko-test-api"
    region = "fra1"
    
    domain {
      name = "yoko.akashi23.me"
      type = "PRIMARY"
      zone = "akashi23.me"
    }

    env {
      key   = "POSTGRES_SERVER"
      value =  "${digitalocean_database_cluster.postgres-cluster.host}:${digitalocean_database_cluster.postgres-cluster.port}"
    }

    env {
      key   = "POSTGRES_USER"
      value = digitalocean_database_cluster.postgres-cluster.user
    }

    env {
      key   = "POSTGRES_PASSWORD"
      value = digitalocean_database_cluster.postgres-cluster.password
    }

    env {
      key   = "POSTGRES_DB"
      value = digitalocean_database_cluster.postgres-cluster.database
    }

    env {
      key   = "FIRST_SUPERUSER"
      value = "admin@admin.com"
    }

    env {
      key   = "FIRST_SUPERUSER_PASSWORD"
      value = "postgres"
    }

    service {
      name               = "yoko-test-api"
      instance_count     = 1
      instance_size_slug = "basic-xxs"
      http_port          = 8080

      routes {
        path = "/api"
      }

      image {
        registry_type = "DOCR"
        repository    = "yoko-test-api"
        tag           = "latest"
      }
    }
  }
}
