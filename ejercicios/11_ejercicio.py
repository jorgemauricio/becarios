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
p=''
i, player1, player2 = 0,0,0
while i !=1:
	cp1,cp2='',''
	player1 = player1 + random.randint(1,10)
	player2 = player2 + random.randint(1,10)
	if player1 >= 100 and player2 < 99:
		i = 1
		p = 'Player1'
	elif player2 >= 100 and player1 < 99:
		i = 1
		p = 'Player2'
	elif player2 >= 100 and player1 >= 100:
		i = 1
		if player1 > player2:
			p = 'Player1'
		elif player2 > player1:
			p = 'Player2'
		elif player1 == player2:
			p = 'Player1 y Player2'
	for x in range(0,player1):
		cp1 =cp1+'*'
	for y in range(0,player2):
		cp2 =cp2+'*'
	print('Player1: {} {}'.format(cp1,player1))	
	print('Player2: {} {}\n'.format(cp2,player2))
	time.sleep(1)
	os.system('cls')
print('Player1: {} {}'.format(cp1,player1))	
print('Player2: {} {}\n'.format(cp2,player2))
print('{} wins'.format(p))