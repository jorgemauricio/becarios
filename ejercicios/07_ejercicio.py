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
frase = "Hola becarios como se encuentran el día de hoy"
for i in frase.split():
	num,imp1,imp2 = 30,'',''
	if len(i) %2 ==0:
		div1 = int((num - len(i))/2)
		div2 = int((num - len(i))/2)
	else:
		div1 = int((num - len(i))/2)
		div2 = int((num - len(i))/2+1)
	while div1 > 0:
	    imp1 = imp1 + '*'
	    div1 -= 1
	while div2 > 0:
	    imp2 = imp2 + '*'
	    div2 -= 1
	print('{}{}{}'.format(imp1,i,imp2))

