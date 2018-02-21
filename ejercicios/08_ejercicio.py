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
de cinco de sus elementos

matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]

Resultado: 1778400

"""
matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]
arr =[]
for i in matrix:
	cont = 1
	for j in i:
		arr.append(j)
arr = sorted(arr)
arr = arr[-1]*arr[-2]*arr[-3]*arr[-4]*arr[-5]
print(arr)

