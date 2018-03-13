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
palabra = 'sOmetEmoS'
palabra = palabra.lower()
lista = []
for i in palabra:
	lista.append(i)

longitud = len(lista)
x = 0
palabra2 = ''
while(x != longitud):
	palabra2 += lista[-x]
	x += 1

if palabra == palabra2:
	print("Las palabras son polindromo")
else:
	print("Las palabras no son polindromo")