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
Data una fecha en el formato AAAA-MM-DD HH:MM donde:
AAAA: año
MM: mes
DD: dia
HH: hora (24 hrs)
MM: minuto

crear un script que permita al usuario agregar el número de minutos que el desee
y se imprima la nueva fecha.

Ej.
fechaInicial = ['2018-01-01 12:00']
agregarMinutos = 70

Resultado:
Fecha Final: 2018-01-01 13:10
"""

ag_min = int(input('Inserte minutos a agregar: '))
fechaInicial = ['2018-01-01 12:00']
ano, mes, dia = (n for n in fechaInicial[0].split("-"))
dia, hora = (n for n in dia.split(" "))
hora, minuto = (n for n in hora.split(":"))
ano, mes, dia, hora, minuto = int(ano), int(mes), int(dia), int(hora), int(minuto)
if mes in (1, 3, 5, 7, 8, 10, 12): #Validacion de fecha
    dias_mes = 31
elif mes == 2:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0): #Si el mes se visiesto
        dias_mes = 29
    else:
        dias_mes = 28
elif mes in (4, 6, 9, 11):
    dias_mes = 30
minuto = minuto + ag_min
while minuto >= 60:
	minuto = minuto - 60
	hora = hora + 1
while hora >= 24:
	hora = hora - 24
	dia = dia + 1
while dia > dias_mes:
	dia = dia - dias_mes
	mes = mes + 1
while mes > 12:
	mes = mes - 12
	ano = ano + 1
print ('{}\n{:04d}-{:02d}-{:02d} {:02d}:{:02d}'.format(fechaInicial[0],ano,mes,dia,hora,minuto))


	