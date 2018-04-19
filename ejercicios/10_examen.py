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

import random
import time

def main():
    horizontal_1 = False
    horizontal_2 = False
    horizontal_3 = False

    vertical_1 = False
    vertical_2 = False
    vertical_3 = False

    diagonal_1 = False
    diagonal_2 = False

    espacio_1 = 0
    espacio_2 = 0
    espacio_3 = 0
    espacio_4 = 0
    espacio_5 = 0
    espacio_6 = 0
    espacio_7 = 0
    espacio_8 = 0
    espacio_9 = 0

    array_valores = [1,2,3,4,5,6,7,8,9]

    status = False

    contador = 0



    while status == False:

        a1,a2,a3,a4,a5,a6,a7,a8,a9 = generar_valores(array_valores)

        if a1 + a2 + a3 == 15:
            horizontal_1 = True
        if a4 + a5 + a6 == 15:
            horizontal_1 = True
        if a7 + a8 + a9 == 15:
            horizontal_1 = True
        if a1 + a4 + a7 == 15:
            vertical_1 = True
        if a2 + a5 + a8 == 15:
            vertical_2 = True
        if a3 + a6 + a9 == 15:
            vertical_3 = True
        if a1 + a5 + a9 == 15:
            diagonal_1 = True
        if a7 + a5 + a3 == 15:
            diagonal_2 = True

        contador += 1
        if horizontal_1 and horizontal_2 and horizontal_3 and vertical_1 and vertical_2 and vertical_3 and diagonal_1 and diagonal_2:
            status = True
        imprimir_cuadro(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        print("iteraciones: ", contador)

    print("Iteraciones: {}".format(count))

def generar_valores(arr):

    rand = random.randint(0, len(arr))
    print(rand)
    b1 = arr[rand]
    del arr[rand]

    rand = random.randint(0, len(arr))
    print(rand)
    b2 = arr[rand]
    del arr[rand]

    rand = random.randint(0, len(arr))
    print(rand)
    b3 = arr[rand]
    del arr[rand]

    rand = random.randint(0, len(arr))
    print(rand)
    b4 = arr[rand]
    del arr[rand]

    rand = random.randint(0, len(arr))
    print(rand)
    b5 = arr[rand]
    del arr[rand]

    rand = random.randint(0, len(arr))
    print(rand)
    b6 = arr[rand]
    del arr[rand]

    rand = random.randint(0, len(arr))
    print(rand)
    b7 = arr[rand]
    del arr[rand]

    rand = random.randint(0, len(arr))
    print(rand)
    b8 = arr[rand]
    del arr[rand]

    b9 = arr[0]

    return [b1,b2,b3,b4,b5,b6,b7,b8,b9]

def validacion(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    pass

def imprimir_cuadro(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    print("\n")
    print("{}|{}|{}".format(a1,a2,a3))
    print("{}|{}|{}".format(a4,a5,a6))
    print("{}|{}|{}".format(a7,a8,a9))
    print("\n")
    #time.sleep(0.5)

if __name__ == '__main__':
    main()
