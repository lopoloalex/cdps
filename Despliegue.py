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

os.system("./bin/prepare-pfinal-vm")

os.system("sudo vnx -f pfinal.xml -v --destroy")
os.system("sudo vnx -f pfinal.xml -v --create")
