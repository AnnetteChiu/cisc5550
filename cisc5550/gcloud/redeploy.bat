rem project name, e.g. 'cisc5550-demo' is up to you
call gcloud compute instances create cisc5550-project --project cisc5550-demo --machine-type n1-standard-1 --image-family debian-9 --image-project debian-cloud --tags http-server --metadata-from-file startup-script=./startup.sh
call gcloud compute firewall-rules create rule-allow-tcp-5000 --project cisc5550-demo --source-ranges 0.0.0.0/0 --target-tags http-server --allow tcp:5000
