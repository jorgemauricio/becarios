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

status = True
cuenta_banco = 0
print("* * * * * MENU * * * * *")
print("* Para depositar incluye D y el monto*")
print("* Para pagar incluye P y el monto*")
print("* Para salir teclea EXIT*")
transaccion = input("Transacción:\n")
while status:
	if transaccion.upper() == "EXIT":
		print("Cuenta de banco con: {}".format(cuenta_banco))
		break
	elif transaccion.split()[0].upper() == "D":
		cuenta_banco += int(transaccion.split()[1])
	elif transaccion.split()[0].upper() == "P":
		if cuenta_banco - int(transaccion.split()[1]) < 0:
			print("Fondos insuficientes")
		else:
			cuenta_banco -= int(transaccion.split()[1])
	else:
		print("Error")
	transaccion = input("Transacción:\n")
