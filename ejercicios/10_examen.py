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

    dic = {"a1":[0, False],
            "a2":[0, False],
            "a3":[0, False],
            "a4":[0, False],
            "a5":[0, False],
            "a6":[0, False],
            "a7":[0, False],
            "a8":[0, False],
            "a9":[0, False]}

    status = True

    contador = 0

    while status:

        arr = random.sample(array_valores, len(array_valores))
        arr_validacion = []
        for k,v in dic.items():
            if v[1] == False:
                arr_validacion.append(k)

        for i in arr_validacion:
            if dic[i][1] == False:
                



        if dic["a1"][0] + dic["a2"][0] + dic["a3"][0] == 15:
            horizontal_1 = True
            dic["a1"][1] = True
            dic["a2"][1] = True
            dic["a3"][1] = True
        if dic["a4"][0] + dic["a5"][0] + dic["a6"][0] == 15:
            horizontal_1 = True
            dic["a4"][1] = True
            dic["a5"][1] = True
            dic["a6"][1] = True
        if dic["a7"][0] + dic["a8"][0] + dic["a9"][0] == 15:
            horizontal_1 = True
            dic["a7"][1] = True
            dic["a8"][1] = True
            dic["a9"][1] = True
        if dic["a1"][0] + dic["a4"][0] + dic["a7"][0] == 15:
            vertical_1 = True
            dic["a1"][1] = True
            dic["a4"][1] = True
            dic["a7"][1] = True
        if dic["a2"][0] + dic["a5"][0] + dic["a8"][0] == 15:
            vertical_2 = True
            dic["a2"][1] = True
            dic["a5"][1] = True
            dic["a8"][1] = True
        if dic["a3"][0] + dic["a6"][0] + dic["a9"][0] == 15:
            vertical_3 = True
            dic["a3"][1] = True
            dic["a6"][1] = True
            dic["a9"][1] = True
        if dic["a1"][0] + dic["a5"][0] + dic["a9"][0] == 15:
            diagonal_1 = True
            dic["a1"][1] = True
            dic["a5"][1] = True
            dic["a9"][1] = True
        if dic["a7"][0] + dic["a5"][0] + dic["a3"][0] == 15:
            diagonal_2 = True
            dic["a7"][1] = True
            dic["a5"][1] = True
            dic["a3"][1] = True

        contador += 1
        if horizontal_1 and horizontal_2 and horizontal_3 and vertical_1 and vertical_2 and vertical_3 and diagonal_1 and diagonal_2:
            status = False
        imprimir_cuadro(dic["a1"][0],dic["a2"][0],dic["a3"][0],dic["a4"][0],dic["a5"][0],dic["a6"][0],dic["a7"][0],dic["a8"][0],dic["a9"][0])
        print("iteraciones: ", contador)

    print("Iteraciones: {}".format(count))

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
