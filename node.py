
#!/usr/bin/python
# -*- coding: latin-1 -*-


import time
import sys
import os
import socket

print(" ---- ACTUALIZANDO REPOSITORIOS ----")
os.system("apt update")
print(" ---- DESCARGANDO DEPENDENCIAS DE NODEJS ----")
os.system("curl -sL https://deb.nodesource.com/setup_9.x | sudo bash -")
print(" ---- INSTALANDO NODEJS ----")
os.system("apt-get install nodejs")
print(" ---- FIN INSTALACION NODEJS ----")


