#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo:
Desarrollar un script que permita geneara un password aleatorio con las siquientes
características mínimas. El usuario puede escoger que su password sea de entre
8 y 20 caracteres.

1. Al menos un caracter entre [a-z]
2. Al menos un numero entre [0-9]
3. Al menos una letra mayuscula entre [A-Z]
4. Al menos un caracter de los siguientes simbolos [$#@]

Resultado:

Introduce la longitud deseada de tu password: 9

H0La123@7
"""
import random 
o = 's'
print("Ingresa -1 para salir")
while(o != 'n'):
	lon = int(input("Ingresa la longitud deseada de tu password: "))
	contra = ''
	if lon >= 8 and lon <=20:
		for i in range(0, lon):
			a = random.randint(1,4)
			if (a == 1):
				b = random.randint(97,122)
				contra += chr(b)
			elif (a == 2):
				b = random.randint(48,57)
				contra += chr(b)
			elif (a == 3):
				b = random.randint(65,90)
				contra += chr(b)
			elif (a == 4):
				b = random.randint(35,36)
				contra += chr(b)
		print(contra)
	elif lon == -1:
		o = 'n'
	else:
		print("Por tu seguridad debes ingresar") 
		print("una longitud que se encuentre en 8 y 20")
		o = input("Deseas intentarlo de nuevo s/n: ")
		if o == 'n':
			o = 'n'