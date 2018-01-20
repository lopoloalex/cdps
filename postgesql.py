

#!/usr/bin/python
# -*- coding: latin-1 -*-


import sys
import os

os.system("apt update")
os.system("apt -y install postgresql")
os.system("echo \"listen_addresses='10.1.4.31'\" >> /etc/postgresql/9.6/main/postgresql.conf")
os.system("echo \"host all all 10.1.4.0/24 trust\" >> /etc/postgresql/9.6/main/pg_hba.conf")


os.system("echo \"CREATE USER crm with PASSWORD 'pene';\" | psql")
os.system("echo \"CREATE DATABASE crm;\" | psql")
os.system("echo \"GRANT ALL PRIVILEGES ON DATABASE crm to crm;\" | sudo -u postgres psql")
os.system("systemctl restart postgresql")


