#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r")
usuarios = fichero.readlines()
fichero.close()

dicc_usuarios = {}
for linea in usuarios:
    contenido = linea.split(":")
    dicc_usuarios[contenido[0]] = contenido[-1]

try:
    print "root", "->", dicc_usuarios["root"][:-1]
except KeyError:
    print ("Usuario no encontrado")
        
try:
    print "imaginario", "->", dicc_usuarios["imaginario"][:-1]
except KeyError:
    print ("Usuario no encontrado")










