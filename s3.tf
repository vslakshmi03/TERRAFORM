resource "aws_s3_bucket" "b" {
bucket = "my1234-test2-bucket"
acl = "private"
tags = {
Name = "my1234-test2-bucket"
Environment = "Dev"
 }
}

