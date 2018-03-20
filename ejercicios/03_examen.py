#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 2
# Valor: 10 puntos
#######################################

Script que permita determinar si una palabra es
palíndromo o no.

Palíndromo: es una palabra, número o frase que se lee igual adelante que atrás

ej:

palabra = sOmetEmoS

Resultado:
La palabra sOmetEmoS es palíndromo
"""

class Cadenas:

    def __init__ (self, cad1):

        self.cad1=cad1

 

    def Pal(self):

        cad1 = self.cad1

        c,i,nom,cad,x = 0,0,'','',''

        i = len(cad1)

        nom = cad1.lower()

        while i != c:

            for x in nom:

                cad = x + cad

                c=c+1

            if nom==cad:

                #print (cad1, " Es Palindromo")

                return str(cad1 + " Es Palindromo")

            else:

                #print (cad1, " No es Palindromo")

                return str(cad1 + " No es Palindromo")

 

cad1 = input('Dame una palabra: ')

op1=Cadenas(cad1)

 

#op1.Pal()#Impresion de la funcion

print(op1.Pal())

