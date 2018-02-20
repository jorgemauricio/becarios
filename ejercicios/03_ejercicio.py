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


#ListaDeNumeros = [7, 23, 478, 8976, 99999, 901298]



lista=[7, 23, 478, 8976, 99999, 901298]
for i in lista:
	cont0 = 0
	cont1 = 0
	cont2 = 0
	var = len(str(i))
	while var 
	for j in str(i):
		cont1 = cont1 + int(j)
		cont0()
    
    while len(str(i)) <2:
    	for j in str(i):
    		cont = cont + int(j)
print ('Resultado: {}'.format(cont))


