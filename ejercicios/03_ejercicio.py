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
    variable = i
    sumatoria = 0
    while len(str(variable)) > 1:
        for j in str(variable):
            sumatoria += int(j)
        variable = sumatoria
        sumatoria = 0
    print("Resultado: {}".format(variable))
