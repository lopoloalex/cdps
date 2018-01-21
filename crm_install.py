import sys
import os
import socket

print(" ---- ACTUALIZANDO REPOSITORIOS ----")
os.system("apt update")
print(" ---- DESCARGANDO DEPENDENCIAS DE NODEJS ----")
os.system("curl -sL https://deb.nodesource.com/setup_8.x | sudo bash -")
print(" ---- INSTALANDO NODEJS ----")
os.system("apt-get install nodejs")
print(" ---- FIN INSTALACION NODEJS ----")

print(" ---- CLONACION DEL CRM ----")
os.system("git clone https://github.com/CORE-UPM/CRM_2017.git")

os.chdir("CRM_2017")
print(" ---- INICIO INSTALACION NPM ----")
os.system("npm install")
os.system("npm install forever")
print(" ---- FIN INSTALACION NPM ----")

os.system("export DATABASE_URL=postgres://crm:xxxx@10.1.4.31:5432/crm")
os.system("export CLOUDINARY_SUBFOLDER=/mnt/nas")

# SOLO EN S1
if socket.gethostname() == "s1":
	print(" ---- MIGRACION DE LA BASE DE DATOS ----")
	os.system("npm run-script migrate_local")
	os.system("npm run-script seed_local")

os.system("./node_modules/forever/bin/forever start ./bin/www")
os.system("sudo iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 80 -j REDIRECT --to-port 3000")