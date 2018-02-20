#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo: Crear un script el cual de una frase dada, clasifique las
palabras de acuerdo a su longitud y contabilice cuantas
existen en la frase.

frase = "Para resolver el siguiente ejercicio van a tener 20 minutos debes
         de subir tu branch al git"

Resultado:
Longitud 5, numero de palabras 3
Longitud 9, numero de palabras 2
Longitud 2, numero de palabras 5
Longitud 7, numero de palabras 1
Longitud 6, numero de palabras 1
Longitud 1, numero de palabras 1
Longitud 8, numero de palabras 1
Longitud 3, numero de palabras 2
Longitud 4, numero de palabras 1


"""
frase = input ('Inserte una frase: ')
a = []
for i in frase.split():
	a.append(len(i))	
min, max = min(a), max(a) 
for i in range (min, max +1):
	c = 0
	for j in frase.split():
		if len(j) == i:	
			c = c + 1
	if c != 0:
		print ('Longitud {}, numero de palabras {}'.format(i,c))