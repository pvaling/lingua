terraform {
  backend "remote" {
    organization = "LinguaHub"

    workspaces {
      name = "lingua_hub"
    }
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = var.region
}

resource "aws_instance" "example" {
  ami           = "ami-009b16df9fcaac611"
  instance_type = "t2.nano"
}

output "ami" {
  value = aws_instance.example.ami
}
