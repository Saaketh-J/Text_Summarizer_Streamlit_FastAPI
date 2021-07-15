terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "api_server" {
  ami           = "ami-0dd76f917833aac4b"
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.fastapi_8000.id]


  tags = {
    Name = "ApiServerInstance"
  }
}

resource "aws_eip" "ip" {
    vpc = true
    instance = aws_instance.api_server.id
}

resource "aws_security_group" "fastapi_8000" {
    name = "fastapi"
    ingress {
        from_port = 0
        to_port = 8000
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
