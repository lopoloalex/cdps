
#!/usr/bin/python
# -*- coding: latin-1 -*-


import time
import sys
import os
import socket


print(" ---- FINAL CONFIGURACION DE CLUSTER DE ALMACENAMIENTO ----")

print(" ---- CONFIGURACION DE SERVIDOR BASE DE DATOS ----")
os.system("sudo lxc-attach --clear-env -n bbdd -- apt update")


os.system("sudo lxc-attach --clear-env -n bbdd -- apt -y install postgresql")

 

os.system("sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo \"listen_addresses='10.1.4.31'\" >> /etc/postgresql/9.6/main/postgresql.conf\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo \"host all all 10.1.4.0/24 trust\"  >> /etc/postgresql/9.6/main/pg_hba.conf\"")


os.system("sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo \"CREATE USER crm with PASSWORD 'xxxx';\" | sudo -u postgres psql\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo \"CREATE DATABASE crm;\" | sudo -u postgres psql\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo \"GRANT ALL PRIVILEGES ON DATABASE crm to crm;\" | sudo -u postgres psql\"")
os.system("sudo lxc-attach --clear-env -n bbdd -- systemctl restart postgresql")




print(" ---- FINAL CONFIGURACION DE SERVIDOR BASE DE DATOS ----")


