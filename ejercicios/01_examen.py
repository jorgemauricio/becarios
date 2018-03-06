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

Solucionar los siguientes puntos mediante un script:
1) Del archivo examen_final.csv genera un archivo csv para cada día, estos csv
deben de guardarse en la carpeta de resultados
2) De la información que se tiene, genera un corte de información para las columnas
Lat y Long con los siguientes valores

Lat > 21.0
Lat < 24.0
Long > -104.0
Long < -100.0

3) Calcula las medias de cada una de las variables Rain, Tmax, Tmin por día
y guardalas en un csv en la carpeta de resultados

4) Calcula las medias de cada una de las variables Rain, Tmax, Tmin por día
del corte de información limitado por las columnas Lat y Long con los siguientes
valores:

Lat > 21.0
Lat < 24.0
Long > -104.0
Long < -100.0

y guardalas en un csv en la carpeta de resultados

5) Calcular las Unidades Calor (UC) para cada una de las filas con la formúla
que se indica en el programa.
"""

# librerias
import Pandas as pd
import numpy as np

# función main()

def main():




def calcularUnidadesCalorBase10(tmax, tmin):
     """
    Función que permite el calculo de unidades Calor
    param: tmax: Temperatura Máxima
    param: tmin: Temperatura Mínima
    param: tbase: Temperatura Base = 10
    Formula uc = tmax + tmin / 2 - tbase
    Donde:
    uc =  unidades calor
    tmax = temperatura máxima
    tmin = tempratura mínima
    tbase = 10
    si tmax > 30 :  tmax = 30
    si tmin < 10 : tmin = 10
    si uc < 0 : uc = 0
    """
if __name__ == '__main__':
     main()
