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

lon= 3
magia=lon*(pow(lon,2)+1)/2
cen=int(lon/2)
cuadro=[[0 for i in range(lon)] for i in range(lon)]
cuadro[0][cen]=1

Var=1
fila=0
columna=cen
print ("Este es el cuadro magico de 3 X 3, Con la respectiva suma de sus valores en 15, Horizontales, Verticales y Diagonales")
for i in range((lon*lon)-1):
    Var=Var+1
    ubif=fila
    fila=fila-1
    ubic=columna
    columna=columna-1
    if fila<0:
        fila=lon-1
    if columna<0:
        columna=lon-1
    if cuadro[fila][columna]==0:
        cuadro[fila][columna]=Var
    elif cuadro[fila][columna]!=0:
        fila=fila+1
        if fila>0:
            fila=ubif+1
        columna=ubic
        cuadro[fila][columna]=Var
for n in range(lon):
    print (str(cuadro[0:lon][n]))
