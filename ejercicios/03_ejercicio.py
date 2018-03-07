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
for i in listaDeNumeros:
	contador0 = i
	contador1 = 0
	var = len(str(contador0))
	while var > 1:
		for j in str(contador0):
			contador1 = contador1 + int(j)
		var = len(str(contador1))
		contador0 = contador1
		contador1 = 0
	print("Resultado es: {}".format(contador0))