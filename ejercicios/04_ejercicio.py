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
o = 'I'
D = 0
while(o != 'S'):
	op = input("Actividad a realizar D/P/S ")
	if op == 'D' or op == 'd':
		D += int(input("Deposito: "))
	elif op == 'P' or op == 'p':
		P = int(input("Pago: "))
		if P > D:
			print("Error al realizar la transaccion ya que el el pago es mayor al deposito")
		else:
			D -= P
			print("Tu deposito Actual es de {}".format(D))
	elif op == 'S' or op == 's':
		print("Tu deposito es de {}".format(D))
		o = 'S'
	else:
		print("Letra no validad Intenta de nuevo")