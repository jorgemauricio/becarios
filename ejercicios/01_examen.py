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
    data=pd.read_csv('examen_final.csv')
    df=data[data['Dia']==1]
    df.to_csv('resultados/Dia1.csv')
    df=data[data['Dia']==2]
    df.to_csv('resultados/Dia2.csv')
    df=data[data['Dia']==3]
    df.to_csv('resultados/Dia3.csv')
    df=data[data['Dia']==4]
    df.to_csv('resultados/Dia4.csv')
    df=data[data['Dia']==5]
    df.to_csv('resultados/Dia5.csv')
    data=pd.read_csv('examen_final.csv')
    # a partir de esta parte el código esta mal
    # no se han corregido los errores
    df=data[data['Lat']>21]
    df=data[data['Lat']<=24]
    df=data[data['Long']>=-104]
    df=data[data['Long']<=-100]
    df.to_csv('resultados/cot_info_Lat_Log.csv')
    data=pd.read_csv('examen_final.csv')
    df1=data[data['Rain']==1]
    df1['Rain'].mean()
    print(df1)
    df=data[data['Rain']==2]
    df['Rain'].mean()
    df=data[data['Rain']==3]
    df['Rain'].mean()
    df=data[data['Rain']==4]
    df['Rain'].mean()
    df=data[data['Rain']==5]
    df['Rain'].mean()
    df=data[data['Tmax']==1]
    df['Tmax'].mean()
    df=data[data['Tmax']==2]
    df['Tmax'].mean()
    df=data[data['Tmax']==3]
    df['Tmax'].mean()
    df=data[data['Tmax']==4]
    df['Tmax'].mean()
    df=data[data['Tmax']==5]
    df['Tmax'].mean()
    df=data[data['Tmin']==1]
    df['Tmin'].mean()
    df=data[data['Tmin']==2]
    df['Tmin'].mean()
    df=data[data['Tmin']==3]
    df['Tmin'].mean()
    df=data[data['Tmin']==4]
    df['Tmin'].mean()
    df=data[data['Tmin']==5]
    df['Tmin'].mean()
    df.to_csv('resultados/medias.csv')






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
