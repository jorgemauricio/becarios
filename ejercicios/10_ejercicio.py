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
from random import SystemRandom

rep, ct = 0, 0
p = ""
while rep != 1:
	longitud = int(input('Introduce la longitud deseada de tu password entre (8 y 20): '))
	if longitud >=8 and longitud <= 20:
		while ct != 4:
			ct = 0
			p = ""
			lon = longitud
			valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$@#"
			cryptogen = SystemRandom()
			while lon > 0:
			    p = p + cryptogen.choice(valores)
			    lon = lon - 1

			c1,c2,c3,c4=0,0,0,0
			for j in p:
				if j in ('1','2','3','4','5','6','7','8','9','0'):
					c1 = 1
				elif j in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'): 
					c2 = 1
				elif j in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'): 
					c3 = 1
				elif j in ('$','#','@'):
					c4 = 1
			ct = c1+c2+c3+c4
		rep = 1
		print(p)
	else:
		print('longitud invalida:{}. La longitud es entre 8 y 20\n'.format(longitud))