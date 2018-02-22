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
arr3=[]
x,y=0,1
while x!=4:
	arr1 =[]
	for i in matrix[x]:
		arr1.append(i)
	x = x + 1
	y = x

	while y!=5:
		arr2 =[]
		for j in matrix[y]:
			arr2.append(j)
		if max(arr1) == max(arr2):
			arr1.remove(max(arr2))
		y = y + 1

	arr3.append(max(arr1))
arr3.append(max(arr2))
print(arr3)