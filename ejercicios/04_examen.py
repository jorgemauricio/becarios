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
x=1
while x !=0:
    ano = int(input('\nIngresa el año: '))
    mes = int(input('Ingresa el mes: '))
    dia = int(input('Ingresa el año: '))

    if mes in (1, 3, 5, 7, 8, 10, 12): #Validacion de fecha
        dias_mes = 31
    elif mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0): #Si el mes se visiesto
            dias_mes = 29
        else:
            dias_mes = 28
    elif mes in (4, 6, 9, 11):
        dias_mes = 30

    if mes <= 12 and mes >= 1 and dia <= dias_mes and dia >= 1:
        dia = dia + 7
        while dia > dias_mes:
        	dia = dia - dias_mes
        	mes = mes + 1
        while mes > 12:
        	mes = mes - 12
        	ano = ano + 1
        print ('{:04d}-{:02d}-{:02d}'.format(ano,mes,dia))
        x=0
    else:
        print('Fecha incorrecta, inserte los datos nuevamente: ')

