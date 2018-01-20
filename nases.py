#!/usr/bin/python
# -*- coding: latin-1 -*-


import time
import sys
import os
import socket

print(" ---- CONFIGURACION DE CLUSTER DE ALMACENAMIENTO ----")
#Instalacion gluster 
os.system("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 10.1.4.22")
time.sleep(3)

os.system("sudo lxc-attach --clear-env -n nas1 -- gluster peer probe 10.1.4.23")
time.sleep(3)

os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume create nas replica 3 10.1.4.21:/nas 10.1.4.22:/nas 10.1.4.23:/nas force")
time.sleep(3)

os.system("sudo lxc-attach --clear-env -n nas1 -- gluster volume start nas")
time.sleep(3)


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

