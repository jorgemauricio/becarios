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

Desplegar el 7mo. día a partir de la fecha dada
por el usuario de la siguiente manera

Ingresa el año: 2016
Ingresa el mes [1-12]: 08
Ingresa el día [1-31]: 23
El 7mo día a partir de la fecha es [aaaa-mm-dd] 2016-8-30
"""
ano = int(input("Ingresa el ano: "))
mes = int(input("Ingresa el mes: "))
dia = int(input("Ingresa el dia: "))

print ("El 7mo dia a partir de la fecha es: {}-{}-{}".format(ano,mes, dia+7))