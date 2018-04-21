#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 9
# Valor: 10 puntos
#######################################

Dada una palabra mediante una función ordenar sus letras por orden alfabetico

Ej.

palabra = "parangaricutirimicuaro"

Resultado.

aaaaccgiiiimnoprrrrtuu

"""
def main():
	alfabeto = "abcdefghijklmnñopqrstuvwxyz"
	palabra = "parangaricutirimicuaro"
	orden = ordenar_letras(palabra, alfabeto)
	print('Palabra = "{}"'.format(orden))

def ordenar_letras(palabra, alfabeto):
    """
    Función que ordena las letras de una palabra
    param: word: palabra a la cual se le van a ordenar sus letras
    """
    lista = ''
    for i in alfabeto:
    	for j in palabra:
    		if j == i:
    			lista = lista + j
    return lista
    print (lista)


if __name__ == '__main__':
     main()
