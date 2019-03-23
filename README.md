# cisc5550
Test the app on Google Cloud

Test the demo web application locally
Get the code for this simple app using Python/Flask here
It include three files: a python file, a html under the directory called templates, and a file called todolist.db for its backend database.
You need to download the three files and put them in any directory and make sure index.html is under templates subdirectory. Or you can download a zip file and unzip anywhere on your computer.
It is a simple to-do list system. Start it (by python todolist.py in the directory where you put those files) and try from a browser. It should be self-explanatory what it does.
Create a VM on Google Cloud Platform

#Prepare:
Redeem the coupon. This will create a 'billing account'. Or decide to use a different billing account that you set up any other ways.
Create a new project. Call it "cisc5550" or something like that to make it easy to identify from other projects you may aleady have.
Link this project to the above mentioned 'billing account'. Remember to check the "Billing" part of the console occasionally to get familiar with how your project is charged.
All the other activities, e.g. create VM etc should be within this project.
For the first step, look at this quick start. Remember to have the "Allow HTTP traffic" checkbox checked.
Always remember to shutdwn the VM if you do not want to have unncessary cost.
Copy the files for the app to Google Cloud
What about Python and Flask? Are they already there? If not, what do you need to do? (Hint: If you start with the default Debian image, you can use sudo apt install python3-pip to install pip for python 3; then use pip3 install flask to install flask module, assuming that you choose to use python3 instead of python, which are both pre-installed.)
Test the app on Google Cloud
You probably can test it locally on VM, say, using curl, but cannot access it from the browser through VM's external IP first. That is because the port number (default 5000 in flask) is not open outside the network of VM. You need to use one of the two following ways to make it accessible: (You only need to use ONE of two approaches. I suggest use the second approach.)

#Because port 80 is set as open, you can make the app run on 80 instead of 5000. To do this, you need to change the last line of todolist.py, app.run() to app.run("0.0.0.0", port=80). Furthermore, you need to run the app with sudo, like sudo python3 todolist.py & because port 80 needs more permissions. That would have required you install packages like flask also with sudo.
Change the network setting of the VM properly by adding a firewall rule. Go to the cloud console, open the page for VM instance you are using. Find the network section, click the network name, which is 'default' by default, to 'open NPC network' page. Then select 'Firewall rules' and click 'CREATE FIREWALL RULE' on the top of the page. Enter an arbitrary name you choose for this rule, enter the tag that the VM is tagged by ('http-server' by default), and enter 'tcp:5000' for Protocols/ports. The last step is the key. Obviously, the port number 5000, the particular tag names, etc. are up to your choice, not necessarily exactly the same as I describe here.
Stop (probably delete) the VM
Automate the above procedure with gcloud script as much as you can. Submit the script for the homework. (Shutting down the instance probably should not be in the same script of setting up and starting the app.)
In case you are not sure where to look at first, try the 'quick-start' according to your local system: Linux, or Mac, or Windows.

#Do not get confused with Cloud Shell, which is similar in many ways, but it is not what you should use for this assignemnt.
