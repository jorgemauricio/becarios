#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 10
# Valor: 10 puntos
#######################################

Generar un script capaz de resolver un cuadro mágico, mediante el uso de
machine learning.

El cuadro mágico es una tabla de grado primario donde se dispone de una
serie de números enteros en un cuadrado o matriz de forma tal que la
suma de los números por columnas, filas y diagonales principales sea la misma

Para este ejercicio se va a resolver un cuadrado mágico de 3 x 3, la suma de
sus valores horizontales, verticales y diagonales debe de ser 15.

El valor principal que hay que tomar en cuenta, es el número de iteraciones
que realiza la computadora para resolver este problema.

__|__|__
__|__|__
  |  |

"""
print ("CUADRO MAGICO")
tamano=int(input("Ingresa el tamaño del Cuadro impar: "))
magia=tamano*(pow(tamano,2)+1)/2
print ("El numero magico es: "+str(magia))
centro=int(tamano/2)
cuadro=[[0 for a in range(tamano)] for a in range(tamano)]
cuadro[0][centro]=1

num=1
fila=0
columna=centro

for a in range((tamano*tamano)-1):    
    num=num+1
    ubifila=fila
    fila=fila-1
    ubicolumna=columna
    columna=columna-1
   
    if fila<0:        
        fila=tamano-1
    if columna<0:        
        columna=tamano-1
    if cuadro[fila][columna]==0:
        cuadro[fila][columna]=num       
    elif cuadro[fila][columna]!=0:
        fila=fila+1
        if fila>0:        
            fila=ubifila+1
        columna=ubicolumna
        cuadro[fila][columna]=num
for n in range(tamano):    
    print (str(cuadro[0:tamano][n]))
   
