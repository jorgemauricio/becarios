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
Un sitio de internet requiere que el password que ingresa el usuario
cumpla con las siguientes caracteristicas para un registro stisfactorio:
1. Al menos un caracter entre [a-z]
2. Al menos un numero entre [0-9]
3. Al menos una letra mayuscula entre [A-Z]
4. Al menos un caracter de los siguientes simbolos [$#@]
5. Longitud mínima de 6 caracteres
6. Longitud máxima de 12 caracteres

Ej.
Si los siguientes passwords los introduce el usuario

passwords = ['HoLa123@7','12345','2w3E*','2We3345']

Resultado:

HoLa123@7
"""
passwords = ['HoLa123@7','12345','2w3E*','2We3345']
for i in passwords:
	az, AZ, o9, simbolos = 0, 0, 0, 0
	if len(i) >= 6  and len(i) <= 12:
		for j in i:
			a = ord(j)
			if (a >= 97 and a <= 122):
				az = 1
			elif (a >= 65 and a <= 90):
				AZ = 1
			elif (a >= 48 and a <= 57):
				o9 = 1
			elif (a == 35 or a == 36 or a == 64):
				simbolos = 1
		if ((az + AZ + o9 + simbolos) == 4):
			print(i)