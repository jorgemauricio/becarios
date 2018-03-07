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

saldo = 0;
opcion = 's';

while ( opcion != 'N'):
	op = input("Seleciona la opcion de que se desea 'D/P':")
	if op == 'D':
		s = int(input("Ingresar la cantidad"))
		saldo = saldo + s 
	if op == 'P':
		pago = int(input("Ingresar la cantidad de que se quiere ingresar:"))
		if pago > saldo:
			print("Saldo insuficiente")
		else:
			saldo = saldo - pago
			print("Tu saldo correspondiente es {}".format(saldo))
		opcion = input("Desea continuar con la transaccion: S/N")