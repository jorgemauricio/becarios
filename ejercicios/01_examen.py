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
    data = pd.read_csv('examen_final.csv') 
    data.head()

    datafr = data[data['Dia'] == 1]
    datafr.to_csv('resultados/Dia1.csv')
    datafr = data[data['Dia'] == 2]
    datafr.to_csv('resultados/Dia2.csv')
    datafr = data[data['Dia'] == 3]
    datafr.to_csv('resultados/Dia3.csv')
    datafr = data[data['Dia'] == 4]
    datafr.to_csv('resultados/Dia4.csv')
    datafr = data[data['Dia'] == 5]
    datafr.to_csv('resultados/Dia5.csv')

    datafr = data[data['Dia'] == 1]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr.to_csv('resultados/Longitudes_y_Latitudes1.csv')
    datafr = data[data['Dia'] == 2]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr.to_csv('resultados/Longitudes_y_Latitudes2.csv')
    datafr = data[data['Dia'] == 3]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr.to_csv('resultados/Longitudes_y_Latitudes3.csv')
    datafr = data[data['Dia'] == 4]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr.to_csv('resultados/Longitudes_y_Latitudes4.csv')
    datafr = data[data['Dia'] == 5]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr.to_csv('resultados/Longitudes_y_Latitudes5.csv')

    datafr = data[data['Dia'] == 1]
    datafr = datafr.mean()
    datafr.to_csv('resultados/Media1.csv')
    datafr = data[data['Dia'] == 2]
    datafr = datafr.mean()
    datafr.to_csv('resultados/Media2.csv')
    datafr = data[data['Dia'] == 3]
    datafr = datafr.mean()
    datafr.to_csv('resultados/Media3.csv')
    datafr = data[data['Dia'] == 4]
    datafr = datafr.mean()
    datafr.to_csv('resultados/Media4.csv')
    datafr = data[data['Dia'] == 5]
    datafr = datafr.mean()
    datafr.to_csv('resultados/Media5.csv')

    datafr = data[data['Dia'] == 1]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr = datafr.mean()
    datafr.to_csv('resultados/LongitudesMedia1.csv')
    datafr = data[data['Dia'] == 2]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr = datafr.mean()
    datafr.to_csv('resultados/LongitudesMedia2.csv')
    datafr = data[data['Dia'] == 3]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr = datafr.mean()
    datafr.to_csv('resultados/LongitudesMedia3.csv')
    datafr = data[data['Dia'] == 4]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr = datafr.mean()
    datafr.to_csv('resultados/LongitudesMedia4.csv')
    datafr = data[data['Dia'] == 5]
    datafr = datafr[datafr['Lat'] >= 21]
    datafr = datafr[datafr['Lat'] <= 24]
    datafr = datafr[datafr['Long'] >= -104.0]
    datafr = datafr[datafr['Long'] <=-100.0]
    datafr = datafr.mean()
    datafr.to_csv('resultados/LongitudesMedia5.csv')

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