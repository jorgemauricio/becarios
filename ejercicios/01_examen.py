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
import pandas as pd
import numpy as np

# función main()

def main():
    # leer csv
    data = pd.read_csv("data/examen_final.csv")

    # generar mis csv por día
    for i in range(1,6):
        data.loc[data["Dia"] == i].to_csv("resultados/dia{}.csv".format(i))
        data.loc[data["Dia"] == i].mean()[["Rain", "Tmax", "Tmin"]].to_csv("resultados/dia_m{}.csv".format(i))

        # corte a lat y long
        data.loc[(data["Dia"] == i) & (data["Lat"] > 21) & (data["Lat"] < 24) & (data["Long"] > -104) & (data["Long"] < -100)].to_csv("resultados/dia_c{}.csv".format(i))
        data.loc[(data["Dia"] == i) & (data["Lat"] > 21) & (data["Lat"] < 24) & (data["Long"] > -104) & (data["Long"] < -100)].mean()[["Rain", "Tmax", "Tmin"]].to_csv("resultados/dia_c_m{}.csv".format(i))

        data["uc"] = data.apply(lambda x: calcularUnidadesCalorBase10(x["Tmax"], x["Tmin"]), axis=1)
        data.to_csv("resultados/data_uc.csv")

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
    if tmax > 30:
        tmax = 30
    if tmin < 10:
        tmin = 10

    uc = 0
    tbase = 10
    uc = (tmax + tmin) / 2 - tbase

    if uc < 0:
        uc = 0
    return uc

if __name__ == '__main__':
    main()
