provider "aws" {
region = "us-west-2"
}

# Create EC2 Instance resource
resource "aws_instance" "test1" {
count = 1
ami = "ami-0ce21b51cb31a48b8"
instance_type = "t2.micro"
key_name = "test2"

}
