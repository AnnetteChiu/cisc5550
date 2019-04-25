#!/bin/bash 

apt-get update -y
apt-get upgrade -y
apt-get install -y python3-pip
pip3 install --upgrade flask

# download the app code
wget -P templates http://storm.cis.fordham.edu/ji/cisc5550/homework3/templates/index.html
wget http://storm.cis.fordham.edu/ji/cisc5550/homework3/todolist.py
wget http://storm.cis.fordham.edu/ji/cisc5550/homework3/todolist.db

python3 todolist.py
