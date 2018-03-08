#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 2
# Valor: 9 puntos
#######################################

Corrigue el siguiente script, recuerda realizar tus commits cada 5 min.
"""
import random
for i in range(1,12):
	a = random.randint(1,12)
	b = random.randint(1,12)
	question="What is {} x {}? ".format(a,b)
	answer=int(input(question))
	if answer==(a*b):
	 	print ("Well done!")
	else:
	 	print("No.")
