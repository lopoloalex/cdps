import sys
import os
import time
import socket

os.system("apt update")
os.system("curl -sL https://deb.nodesource.com/setup_8.x | sudo bash -")
os.system("apt-get install nodejs")

os.system("git clone https://github.com/CORE-UPM/CRM_2017.git")

os.chdir("CRM_2017")
os.system("npm install")
os.system("npm install forever")

os.system("export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm")

# SOLO EN S1
if socket.gethostname() == "s1":
	os.system("npm run-script migrate_local")
	os.system("npm run-script seed_local")

os.system("./node_modules/forever/bin/forever start ./bin/www")