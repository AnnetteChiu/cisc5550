#! /bin/bash

gcloud compute instances create homework3 --tags http-server --metadata startup-script='#! /bin/bash
wget -nc https://storm.cis.fordham.edu/ji/cisc5550/todolist.zip
sudo apt-get install unzip
sudo unzip todolist.zip -d todolist
sudo apt install python3-pip
sudo pip3 install flask
gcloud compute firewall-rules create firewall-5000 --allow tcp:5000 --target-tags http-server
cd todolist
sudo python3 todolist.py'

