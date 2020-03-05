variable "region" {
description = "Region to create EC2 instance"
default = "us-east-1a"
}
variable "role_name" {
description = "IAM Role to be used"
}

variable "ami" {
description = "AWS AMI to be used"
}

variable "subnet" {
description = "Subnet to use"
#default = "subnet-51082b26"
}

variable "sg" {
description = "Security group to use"
#default = "sg-0529771a4b0732c91"
}

variable "cluster_name" {
description = "Cluster name to add as part of its user_data"
#default = "newventures-simplr-dev"
}

variable "pem_key" {
description = "Pem key to be associated"
#default = "newventures-simplr-dev"
}
variable "environment" {
description = "Which environment you want instance to be created"
#default = "newventures-simplr-dev"
}

variable "name" {
description = "Name of EC2 instance"
#default = "newventures-simplr-dev"
}
