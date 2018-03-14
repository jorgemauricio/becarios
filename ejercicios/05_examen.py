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

De la siguiente matrix de datos, imprime el valor y la posición
de los 5 numéros más altos
matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]

resultado:
Valor 20, posición 0,0
Valor 20, posición 0,2
Valor 20, posición 3,2
Valor 19, posición 1,0
Valor 18, posición 4,2
"""
matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]
orden = []
maximos = []
x = -1

for i in range(0, len(matrix)):
	for j in range(0, len(matrix[i])):
		orden.append(matrix[i][j])
tam = len(orden)
for i in range(0, len(orden)):
	for j in range(0, tam-1):
		if orden[j] > orden[j+1]:
			aux = orden[j+1]
			orden[j+1] = orden[j]
			orden[j] = aux
for i in range(1, 6):
	maximos.append(orden[x])
	x-=1

for i in range(0, len(matrix)):
	for j in range(0, len(matrix[i])):
		if matrix[i][j] in maximos:
			print('Valor {}, posición {},{}'.format(matrix[i][j], i,j))