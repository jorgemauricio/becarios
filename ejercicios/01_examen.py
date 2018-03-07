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
import pandas as pd
import numpy as np

# función main()

def main():
    data = pd.read_csv('../data/examen_final.csv')
    df = data
    lista = []
    maxt = np.array(data['Tmax'])
    mint = np.array(data['Tmin'])

    for i in range(1, 6):
        print('Generando el csv cuando Dia es igual a {}'.format(i))
        dia = data[data['Dia'] == i]
        dia.to_csv('resultados/Dia{}.csv'.format(i))
        print('Generando las medias de la variables del Dia {}'.format(i))
        dia = dia.mean()
        dia.to_csv('resultados/Medias(Dia{}).csv'.format(i))
    for i in range(1, 6):
        print('Generando el csv de fltrado de informacion por Dia {}'.format(i))
        dia = data[data['Dia'] == i]
        dia = dia[(dia['Lat'] > 21.0 )& (dia['Lat'] < 24.0)]
        dia = dia[(dia['Long'] > -100.0) & (dia['Long'] < -104.0)]
        dia.to_csv('resultados/filtrado(Dia{}).csv'.format(i))
        dia = dia.mean()
        print('Generando el csv de media del fltrado de informacion por Dia {}'.format(i))
        dia.to_csv('resultados/MediaFiltrado(Dia{}).csv'.format(i))
    print("*"*10)
    print('Generando csv calculando las Unidad de Calor')
    for i in range(0, len(maxt)):
        tmax = maxt[i]
        tmin = mint[i]
        resul = calcularUnidadesCalorBase10(tmax, tmin)
        lista.append(resul)
    df['UnidadCalor'] = lista
    df.to_csv('resultados/UnidadesCalor.csv')

def calcularUnidadesCalorBase10(tmax, tmin):
    tbase = 10
    if tmax > 30:
        tmax = 30
    if tmin < 10:
        tmin = 10
    uc = tmax + tmin / 2 - tbase
    if uc < 0:
        uc = 0
    return uc

if __name__ == '__main__':
     main()