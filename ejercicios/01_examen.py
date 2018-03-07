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
    data = pd.read_csv('../data/examen_final.csv')
    for i in range (1,6):
        data[data['Dia']==i].to_csv('resultados/d{}.csv'.format(i))
        data[data['Dia']==i].mean()[['Rain','Tmax','Tmin']].to_csv('resultados/Medias_d{}.csv'.format(i)) 
        data[(data['Dia']==i) & (data['Lat'] > 21.0) & (data['Lat'] < 24.0) & (data['Long'] > -104.0) & (data['Long'] < -100.0)].to_csv('resultados/Medias_d{}.csv'.format(i))
        data[(data['Dia']==i) & (data['Lat'] > 21.0) & (data['Lat'] < 24.0) & (data['Long'] > -104.0) & (data['Long'] < -100.0)].mean()[['Rain','Tmax','Tmin']].to_csv('resultados/Medias_d{}_corte.csv'.format(i))
    data['Unidades_de_Calor'] = data.apply(lambda x:calcularUnidadesCalorBase10(x['Tmax'],x['Tmin'])axis=1)

def calcularUnidadesCalorBase10(tmax, tmin):
    '''
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
    '''
    cu = 0
    if tmax > 30:
        tmax = 10
    if tmin < 10:  
        tmin = 10
    cu = (tmax+tmin)/2-10

if __name__ == '__main__':
    main()
