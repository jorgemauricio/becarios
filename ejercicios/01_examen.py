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

5) Calcular las Unidades Calor (uc) para cada una de las filas con la formúla
que se indica en el programa.
"""

# librerias
import pandas as pd
import numpy as np

# función main()

def main():
    data=pd.read_csv('../data/examen_final.csv')
    dia1=data[data['Dia']==1]
    dia1.to_csv('resultados/Dia1.csv')
    # de aquí en adelante el código esta mal verificarlo
    dia2=data[data['Dia']==2]
    dia.to_csv('resultados/Dia2.csv')
    dia3=data[data['Dia']==3]
    dia.to_csv('resultados/Dia3.csv')
    dia4=data[data['Dia']==4]
    dia.to_csv('resultados/Dia4.csv')
    dia5=data[data['Dia']==5]
    dia.to_csv('resultados/Dia5.csv')
    corte_Lat= data[(data['Lat'] > 21.0) & (data['Lat'] < 24.0)]
    corte_Lat.to_csv('resultados/Latitud.csv')
    corte_Long= data[(data['Long'] > -104.0) & (data['Long'] < -100.0)]
    corte_Long.to_csv('resultados/Longitud.csv')
    media=data[data['Rain']==1]






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
