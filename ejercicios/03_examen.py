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

palabra = p

Resultado:
La palabra sOmetEmoS es palíndromo
"""
#palabra = sOmetEmoS
palabra = input('Ingrese una palabra:')
pal = palabra.lower()
temp = pal.replace(' ','')

if temp == temp[::-1]:
	print('la palabra'   +pal+   ' es palindromo')
else:
	print('la palbra ' +pal+ 'no es palindromo')

