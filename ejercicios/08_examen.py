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
datos = [2,4,10,21, 7]
sumatoria, promedio = [2, 5], [7]
for i in sumatoria:
	suma = 0
	for j in datos:
		if int(j) % int(i) == 0:
			suma = suma + j
	print ('La sumatoria de los numeros divisibles entre {} es: {}\n'.format(i, suma))

for i in promedio:
	lista = []
	for j in datos:
		if int(j) % int(i) == 0:
			lista.append(j)
	prom, cont = 0, 0
	for j in lista:
		prom = prom + j
		cont = cont + 1
	prom = prom/cont
	print ('El promedio de los numeros divisibles entre {} es: {}\n'.format(i, prom))

cont = 0
prom = 0
for i in datos:
	if i % 2 == 0 or i % 5 == 0 or i % 7 == 0:
		prom = prom + i
		cont = cont + 1
tot = prom / cont
print(prom)
print ('el promedio de los numeros que sean divisibles entre 2, 5, y 7 es: {}'.format(tot))

