#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo: Dada una lista de números, sumar sus dígitos entre sí hasta que el valor,
solo sea un dígito de longitud 1.

listaDeNumeros = [7, 23, 478, 8976, 99999, 901298]

Resultado: 7
Resultado: 5
Resultado: 1
Resultado: 3
Resultado: 9
Resultado: 2

"""
listaDeNumeros = [7, 23, 478, 8976, 99999, 901298]

a = []
j = 0
for i in listaDeNumeros:
	a.append(str(listaDeNumeros[j]))
	j += 1

for z in a:
	lon = len(z)
	if lon >= 2:
		for i in range(0, lon):
			pass
	else:
		print ('Resultado: {}'.format(int(z)))