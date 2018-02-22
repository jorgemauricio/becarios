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
arr =[]
arr_or =[]
for i in matrix:
	cont = 1
	for j in i:
		arr.append(j)
while len(arr) !=0:
	i =0
	minimo = arr[0]
	while i < len(arr):
		if arr[i]<minimo:
			minimo = arr[i]
			i = i +1
		else:
			i = i + 1
	arr_or.append(minimo)
	arr.remove(minimo)
arr_or = arr_or[-1]*arr_or[-2]*arr_or[-3]*arr_or[-4]*arr_or[-5]
print(arr_or)
