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
Escribe un programa que calcule el valor neto de una cuenta de banco basado
en las transacciones que se ingresan en la consola de comandos.

Ej:
	D 200
	D 250
	P 300
	D 100
	P 200
	Donde:
	D = Deposito
	P = Pago

Resultado:
	50

"""
print ('TRANSFERENCIAS BANCARIAS')
print ('SELECCIONA UN NUMERO PARA REALIZAR UNA ACCION')
cont = 0
res = 0
while cont ==0:
	opcion = int(input ('1 = Deposito, 2 = Pago, 3 = Resultado: '))
	if opcion == 1:
		dep = int(input ('Ingrese la cantidad a depositar: '))
		res = res + dep
		new = int(input ('Desea realizar otra accion. "SI" = 1, "NO" = 2: '))
		if new == 2:
			cont = 1
			print ('Su estado de cuenta es {}'.format(res))
	elif opcion == 2:
		pag = int(input('Ingrese la cantidad a pagar: '))
		if pag > res:
			print ('No cuenta con la cantidad necesaria para realizar el pago. Fondos = {}'.format(res))
			new = int(input ('Desea realizar otra accion. "SI" = 1, "NO" = 2: '))
		else:
			res = res - pag
			new = int(input ('Desea realizar otra accion. "SI" = 1, "NO" = 2: '))
		if new == 2:
			cont = 1
			print ('Su estado de cuenta es {}'.format(res))
	elif opcion == 3:
		print ('Su estado de cuenta es {}'.format(res))