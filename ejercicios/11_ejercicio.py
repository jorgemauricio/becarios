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
Desarrollar un script capaz de generar una simulación de carrera entre dos jugadores
utilizando el modulo random, el primer jugador que llegue a 100 gana la carrera.

Ej.
import random

a = random.randint(1,10)
a: puede ser un valor entre 1 y 10 aleatorio

Para evitar que la simulación se despliegue muy rápido, puedes utilizar el módulo time

import time

time.sleep(1)

el programa detiene su ejecución en 1 segundo

Resultado:

player1: ************************************************************************************************* 97
player2: **************************************************************************************************** 100
player2 wins

"""
import random 
import time
import os
win, wins1, wins2 = -1, 0, 0
a, b = 0, 0
while (win != 100):
	jug1 = random.randint(1,10)
	jug2 = random.randint(1,10)
	a , b=  a + jug1, b + jug2
	if (a >= 100):
		a = 100
		win = 100
		wins1 = 1
		print("player1: ","*"*100," 100")
		print("player2: ","*"*b,"{}".format(b))
	elif(b >= 100):
		b = 100
		win = 100
		wins2 = 1
		print("player1: ","*"*a,"{}".format(a))
		print("player2: ","*"*100," 100")
	else:
		print("player1: ","*"*a,"{}".format(a))
		print("player2: ","*"*b,"{}".format(b))
	time.sleep(1)
	os.system("cls")
if (wins1 == 1 and wins2 == 1):
	print("player1: ","*"*a,"{}".format(a))
	print("player2: ","*"*b,"{}".format(b))
	print("Hubo un empate en la carrera")
elif(wins1 == 1):
	print("player1: ","*"*a,"{}".format(a))
	print("player2: ","*"*b,"{}".format(b))
	print("player1 wins")
else:
	print("player1: ","*"*a,"{}".format(a))
	print("player2: ","*"*b,"{}".format(b))
	print("player1 win2")