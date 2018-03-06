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
    tmax = np.array(data['Tmax'])
    tmin = np.array(data['Tmin'])
    dias(data)
    medias(data)
    calcularUnidadesCalorBase10(tmax, tmin)

def dias(data):
    for i in range (1,6):
        df = data[data['Dia']==i]
        df.to_csv('resultados/d{}.csv'.format(i)) 
        df = df[df['Lat'] > 21.0]
        df = df[df['Lat'] < 24.0]
        df = df[df['Long'] > -104.0]
        df = df[df['Long'] < -100.0]
        df.to_csv('resultados/d{}_filtro.csv'.format(i))

def medias(data):
    Rain1,Rain2,Tmax1,Tmax2,Tmin1,Tmin2,Dia=[],[],[],[],[],[],[]
    new1, new2 = pd.DataFrame(), pd.DataFrame()
    for i in range (1,6):
        df = data[data['Dia']==i]
        Rain1.append(df['Rain'].mean())
        Tmax1.append(df['Tmax'].mean())
        Tmin1.append(df['Tmin'].mean())
        Dia.append(i)
        df = df[df['Lat'] > 21.0]
        df = df[df['Lat'] < 24.0]
        df = df[df['Long'] > -104.0]
        df = df[df['Long'] < -100.0]
        Rain2.append(df['Rain'].mean())
        Tmax2.append(df['Tmax'].mean())
        Tmin2.append(df['Tmin'].mean())
    new1['Dia'], new1['Rain'], new1['Tmax'], new1['Tmin'] = Dia, Rain1, Tmax1, Tmin1
    new2['Dia'], new2['Rain'], new2['Tmax'], new2['Tmin'] = Dia, Rain2, Tmax2, Tmin2
    new1.to_csv('resultados/Medias.csv')
    new2.to_csv('resultados/Medias_filtro.csv')    

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
    x,y,cu=[],[],[]
    for i in tmax:
        if i > 30:
            i = 10
        x.append(i)
    for i in tmin:
        if i < 10:  
            i = 10
        y.append(i)
    for i in range(len(x)):
        cu.append((x[i]+y[i])/2-10)
    df = pd.DataFrame(cu)
    df.rename(columns={0:'Cu'})
    df.to_csv('resultados/Unidades_de_Calor.csv')

if __name__ == '__main__':
    main()
