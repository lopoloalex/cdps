#!/usr/bin/python
# -*- coding: latin-1 -*-


import time
import sys
import os
import socket






os.system("sudo apt-get update")

if (os.path.isdir("PracticaFinal")):
	os.system("sudo rm -rf PracticaFinal")

print(" ---- CREANDO CARPETA ----")

os.system("mkdir PracticaFinal")
os.chdir("PracticaFinal")

print(" ---- DESCARGA DE LA MAQUINA ----")

os.system("wget http://idefix.dit.upm.es/cdps/pfinal/pfinal.tgz")
os.system("sudo vnx --unpack pfinal.tgz")
os.chdir("pfinal")

print(" ---- MAQUINA CREADA ----")

# Comprueba si es un ordenador del laboratorio o no.
#if (socket.gethostname().match("/(l[0-9]{3})/")):
#	os.system("bin/prepare-pfinal-labo")
#else:
os.system("./bin/prepare-pfinal-vm")

os.system("sudo vnx -f pfinal.xml -v --destroy")
os.system("sudo vnx -f pfinal.xml -v --create")

print(" ---- ESCENARIO DESPLEGADO ----")

print(" ---- CONFIGURACION DE FIREWALL ----")
#Configuración de FW desde la carpeta PracticaFinal 
#os.system("scp ../fw.fw root@fw:~/")
#os.system("sudo lxc-attach --clear-env -n fw -- /root/fw.fw")
print(" ---- FIN DE CONFIGURACION DE FIREWALL ----")

print(" ---- CONFIGURACION DE CLUSTER DE ALMACENAMIENTO ----")
#Instalacion gluster 
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 10.1.4.22")
time.sleep(4)

os.system("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 10.1.4.23")
time.sleep(4)

os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume create nas replica 3 10.1.4.21:/nas 10.1.4.22:/nas 10.1.4.23:/nas force")
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume start nas")
time.sleep(7)


os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume set nas network.ping-timeout 5")
os.system("sudo lxc-attach --clear-env -n nas2 -- gluster volume set nas network.ping-timeout 5")
os.system("sudo lxc-attach --clear-env -n nas3 -- gluster volume set nas network.ping-timeout 5")

#Configuracion del sistema de ficheros NAS en servidores
n=3 
while (n > 0):
	os.system("sudo lxc-attach --clear-env -n s" +str(n)+ " -- mkdir /mnt/nas")
	os.system("sudo lxc-attach --clear-env -n s" +str(n)+ " -- mount -t glusterfs 10.1.4.2" +str(n)+ ":/nas /mnt/nas")
	print(" ---- directorio mnt/nas creado en s" +str(n)+ " ----")
	n=n-1


print(" ---- FINAL CONFIGURACION DE CLUSTER DE ALMACENAMIENTO ----")

print(" ---- CONFIGURACION DE SERVIDOR BASE DE DATOS ----")

os.system("sudo lxc-attach --clear-env -n bbdd -- apt-get update")
os.system("sudo lxc-attach --clear-env -n bbdd -- apt-get -y install postgresql")
os.system("sudo lxc-attach --clear-env -n bbdd -- echo \"listen_addresses='10.1.4.31'\" >> /etc/postgresql/9.6/main/postgresql.conf")
os.system("sudo lxc-attach --clear-env -n bbdd -- echo \"host all all 10.1.4.0/24 trust\" >> /etc/postgresql/9.6/main/pg_hba.conf")

os.system("sudo lxc-attach --clear-env -n bbdd -- echo \"CREATE USER crm with PASSWORD 'xxxx';\" | sudo -u postgres psql")
os.system("sudo lxc-attach --clear-env -n bbdd -- echo \"CREATE DATABASE crm;\" | sudo -u postgres psql")
os.system("sudo lxc-attach --clear-env -n bbdd -- echo \"GRANT ALL PRIVILEGES ON DATABASE crm to crm;\" | sudo -u postgres psql")
os.system("sudo lxc-attach --clear-env -n bbdd -- systemctl restart postgresql")

print(" ---- FINAL CONFIGURACION DE SERVIDOR BASE DE DATOS ----")

print(" ---- CONFIGURACION DE BALANCEADOR DE TRAFICO ----")

#Configuracion de lb 
os.system("xterm -hold -e 'sudo lxc-attach --clear-env -n lb -- xr --verbose --server tcp:0:80 -dr --backend 10.1.3.11:80 --backend 10.1.3.12:80 --backend 10.1.3.13:80 --web-interface 0:8001' &")

print(" ---- FINAL CONFIGURACION DE BALANCEADOR DE TRAFICO ----")

