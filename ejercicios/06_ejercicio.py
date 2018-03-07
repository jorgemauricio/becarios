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
o = 1
print("Ingresa -1 para salir ")
while(o != -1):
	minutos = int(input("Minutos a ingresar: "))
	if minutos < 0:
		o = -1
	else:
		fechaInicial = ['2018-01-01 12:00']
		ano, mes, dia = (i for i in fechaInicial[0].split("-"))
		dia, hora = (i for i in dia.split(" "))
		hora, minuto = (i for i in hora.split(":"))
		ano, mes, dia, hora, minuto = int(ano), int(mes), int(dia), int(hora), int(minuto)
		if mes in (1 , 3, 5, 7, 8, 10, 12):
			dias_mes = 31
		elif mes == 2:
			if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
				dias_mes = 29
			else:
				dias_mes = 28
		elif mes in (4, 6, 9, 11):
			dias_mes = 30
		min1, min2= minutos/60, minutos%60
		minuto += minutos
		if minuto >= 60:
			minuto = int(min2)
			hora += int(min1)
			hor1, hor2 = hora/24, hora%24
			if hora >= 24:
				hora = int(hor2)
				dia += int(hor1)
				dia1, dia2 = dia/dias_mes, dia%dias_mes
				if dia > dias_mes:
					dia = int(dia2)
					mes += int(dia1)
		print('{:04d}-{:02d}-{:02d} {:02d}:{:02d}'.format(ano, mes, dia, hora, minuto))