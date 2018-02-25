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
De una matrix dada, encontrar el maximo producto que resulte de la multiplicación
de cinco de sus elementos sin utilizar la función de sorted

matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]

Resultado: 1778400

"""
matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]
a, a2, resul = [], [], 1
for i in range(0, len(matrix)):
	for j in range(0, len(matrix[i])):
		a.append(matrix[i][j])

for i in range(0, 5):
	maximo = max(a)
	a2.append(maximo)
	resul *= a2[i]
	index = a.index(maximo)
	a.pop(index)
print("Resultado: {}".format(resul))