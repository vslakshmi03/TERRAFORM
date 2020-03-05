provider "aws" {
region = "${var.region}"
}

# Create EC2 Instance resource
resource "aws_instance" "newventures_instance"{
count = 1
iam_instance_profile = "newventures-simplr-ecs"
ami = "${var.ami}"
instance_type = "m5.large"
key_name = "${var.pem_key}"
subnet_id = "${var.subnet}"
vpc_security_group_ids = ["${var.sg}"]

# user data
user_data = <<EOF
#!/bin/bash
ADMINUSERS="swarnalakshmi.vedal, harsh.tomar, illana.stanley, william.macdonald, aaron.mednick, saurabh.malviya, scefali, bilal.muzaffar, damien.thioulouse, long.chen, jack.seabolt"
#SKIP_PKG_UPDATE=True    ### (Optional) Uncomment this line to skip the package update, i.e. yum/apt-get update, use at your own discretion
###### step 1: create a computer object in the HQDOMAIN domain for this instance so that the record starts propagation sooner.
curl -o /tmp/realm_join.sh -k -L -H "x-api-key: 52m1l3h3RX6ZGOuxY6Mty4wsnGCfLsy57IOZaeJQ" "https://linux-auth.gov.prd.aws.asurion.net/cg-linux-alt/realm-join?OS_ID=register"
source /tmp/realm_join.sh > /tmp/realm_join_step1.log 2>&1
echo ECS_CLUSTER=${var.cluster_name} >> /etc/ecs/ecs.config
###### step 2: join the HQDOMAIN domain with the newly created computer object, add access restrictions to your AD groups/users, and install Amazon Inspector Agents
curl -o /tmp/realm_join.sh -k -L -H "x-api-key: 52m1l3h3RX6ZGOuxY6Mty4wsnGCfLsy57IOZaeJQ" "https://linux-auth.gov.prd.aws.asurion.net/cg-linux-alt/realm-join?OS_ID=realm-join"
source /tmp/realm_join.sh > /tmp/realm_join_step2.log 2>&1
rm -f /tmp/realm_join.sh

sudo yum install java-1.8.0 -y 
sudo yum install python34-pip -y
sudo pip-3.4 install awscli
/usr/local/bin/aws --version
echo ECS_CLUSTER=${var.cluster_name} >> /etc/ecs/ecs.config

sudo curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.7.1-x86_64.rpm
sudo yum install filebeat-6.7.1-x86_64.rpm -y

echo "---
filebeat.inputs:
  -

    paths:
      - /var/lib/docker/containers/*/*.log
    type: log
output.logstash:
  hosts:
    - "localhost:5400"
processors:
  -
    add_host_metadata: ~
  -
    add_cloud_metadata: ~
  -
    add_docker_metadata: ~ " > filebeat.yml

sudo service filebeat start


curl -O https://d1wk0tztpsntt1.cloudfront.net/linux/latest/install && sudo bash install && sudo /etc/init.d/awsagent start
 
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
cd /etc/yum.repos.d/
echo " [logstash-6.x]
name=Elastic repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md " > logstash.repo
echo 'Install logstash'
sudo yum install logstash -y
echo "Pulling logstash config files from s3"
/usr/local/bin/aws s3 cp s3://newventures-simplr-tfstatefiles/logstash_conf_files /etc/logstash/conf.d/ --recursive
echo "Done with Pulling logstash config files from s3"
cd /etc/logrotate.d/
echo " /var/log/logstash/*.log /var/log/logstash-stderr.log /var/log/logstash-stdout.log {
daily
rotate 4
copytruncate
compress
delaycompress
missingok
notifempty
} " > logstash
initctl start logstash

EOF

root_block_device {
volume_type = "gp2"
volume_size = "8"
delete_on_termination = "true"
}

ebs_block_device {
device_name = "/dev/xvda"
volume_size = "100"
volume_type = "gp2"
delete_on_termination = "true"
}

ebs_block_device {
device_name = "/dev/xvdcz"
volume_size = "22"
volume_type = "gp2"
delete_on_termination = "true"
}


}
    terraform {
  backend "s3" {}
}
