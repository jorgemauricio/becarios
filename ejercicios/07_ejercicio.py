#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0b %
#######################################

Objetivo:
De una frase, imprimir cada una de sus palabras centradas en un marco de 30
espacios

Ej.
frase = "Hola becarios como se encuentran el día de hoy"

Resultado:
*************hola*************
***********becarios***********
*************como*************
**************se**************
**********encuentran**********
**************el**************
*************dia**************
**************de**************
*************hoy**************
"""
frase = "hola becarios como se encuentran el dia de hoy".split()
for i in frase:
	a = len(i)
	if a >= 1 and a <= 30:
		b = 30 - a
		c, d = b/2, b%2 
		print("*"*int(c)+"{}".format(i)+"*"*(int(c)+int(d)))
	else: 
		print("Palabra {} esta fuera de la longitud valida".format(i))