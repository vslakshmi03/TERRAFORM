provider "aws" {
region = "us-west-2"
}

module "ecs_ec2_instances_main" {
  source                 = "terraform-aws-modules/ec2-instance/aws"
  version                = "~> 2.0"
  name                   = "ec2-test"
  instance_count         =  1
  ami                    = "ami-0ce21b51cb31a48b8"
  instance_type          = "t2.micro"
  subnet_id              = "subnet-40850524"
  key_name               = "test2"



}
