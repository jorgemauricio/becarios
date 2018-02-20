#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo: Crear un script el cual de una frase dada, imprima las palabras que su
primer letra sea una s.

frase = "El día de hoy el Sol salió alrededor de las 6 am por segundo día consecutivo"

Resultado:
Sol
salió
segundo
"""
frase = "El día de hoy el Sol salió alrededor de las 6 am por segundo día consecutivo"
for i in frase.split():
	if i[0] == 's' or i[0] == 'S':
		print(i)