#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 8
# Valor: 10 puntos
#######################################

De una serie de datos del 0 al 100, realizar
las siguientes acciones:

1. Imprimir la sumatoria de los numeros pares.
2. Imprimir la sumatoria de los numeros divisibles entre 5
3. Imprimir el promedio de los numeros divisibles entre 7
4. Imprimir el promedio de los numeros que sean divisibles entre 2, 5, y 7.
"""

Pares = 0
Divisibles = 0
Divisibles1 = 0
Prom = 0
PromeDiv = 0

for i in range(0, 101):
	if i%2 == 0:
		Pares += i
	if i%5 == 0:
		Divisibles / 5
	if i%7 == 0:
		Prom += i
		Divisibles1 / 7
	if i%2 == 0 and i%5 == 0 and i%7 == 0:
		Prom += i 
		PromeDiv += 1
print("La sumatoria de los numeros pares es: {}".format(Pares)) 
print("La sumatoria de los numeros divisibles entre 5 son: {}".format(Divisibles)) 
print("El promedio de los numeros divisibles es entre 7 son: {}".format(Divisibles1, Prom))
print("El promedio de los numeros divisibles entre 2, 5 y 7 es: {}{}".format(Prom, PromeDiv)) 



