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
Dada una matrix de n x n desarrollar un script capaz de identificar el número
mayor que se encuentra en cada una de sus filas, tomando en cuenta que si en la
siguiente fila el número es igual al anterior, este debe de ser actualizdo y
por consiguiente disminuir.


matrix = [[20,1,19,8,6],[2,0,5,8,20],[9,8,23,0,12],[11,2,19,4,5],[4,3,18,1,3]]

Resultado:

Fila 1, número mayor: 8
Fila 2, número mayor: 20
Fila 3, número mayor: 23
Fila 4, número mayor: 19
Fila 5, número mayor: 18

"""
matrix = [[20,1,19,8,6],[2,0,5,8,20],[9,8,23,0,12],[11,2,19,4,5],[4,3,18,1,3]]
lista, a, b = [], -1, True
for i in range(0, len(matrix)):
	if max(matrix[a]) not in lista:
		lista.append(max(matrix[a]))
	else:
		while(b):
			matrix[a].remove(max(matrix[a]))
			if max(matrix[a]) not in lista:
				lista.append(max(matrix[a]))
				b = False	
	a -= 1
lista.reverse()
print("Resultado")
for i in range(0, 5):
	print("Fila {}, numero mayor: {}".format(i+1,lista[i]))
