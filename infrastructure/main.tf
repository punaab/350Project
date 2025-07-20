provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Update to latest Amazon Linux 2 AMI
  instance_type = "t2.micro"
  security_groups = [aws_security_group.app_sg.name]
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y docker
              service docker start
              usermod -a -G docker ec2-user
              docker pull punaab/350finalproject:latest
              docker run -d -p 80:5000 punaab/350finalproject:latest
              EOF
  tags = {
    Name = "350FinalProject"
  }
}

resource "aws_security_group" "app_sg" {
  name = "app_sg"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "instance_public_ip" {
  value = aws_instance.app_server.public_ip
} 