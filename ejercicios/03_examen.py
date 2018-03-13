#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 2
# Valor: 10 puntos
#######################################

Script que permita determinar si una palabra es
palíndromo o no.

Palíndromo: es una palabra, número o frase que se lee igual adelante que atrás

ej:

palabra = sOmetEmoS

Resultado:
La palabra sOmetEmoS es palíndromo
"""

frase1 = input("Inserte una palabra: ")
frase1 = frase1.lower()
x = len(frase1)
frase2 = []
while x > 0:
	frase2.append(frase1[x-1])
	x = x-1
frase2 = frase2.split(',')
print(frase2)