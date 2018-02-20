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
	c1,c2,c3,c4,ct=0,0,0,0,0
	if len(i) >=6 and len(i) <= 12:
		for j in i:
			if j in ('1','2','3','4','5','6','7','8','9','0'):
				c1 = 1
			elif j in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'): 
				c2 = 1
			elif j in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'): 
				c3 = 1
			elif j in ('$','#','@'):
				c4 = 1
		ct = c1+c2+c3+c4
		if ct ==4:
			print(i)