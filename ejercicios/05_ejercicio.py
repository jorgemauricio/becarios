#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo:
Un sitio de internet requiere que el password que ingresa el usuario
cumpla con las siguientes caracteristicas para un registro satisfactorio:
1. Al menos un caracter entre [a-z]
2. Al menos un numero entre [0-9]
3. Al menos una letra mayuscula entre [A-Z]
4. Al menos un caracter de los siguientes simbolos [$#@]
5. Longitud mínima de 6 caracteres
6. Longitud máxima de 12 caracteres

Ej.
Si los siguientes passwords los introduce el usuario

passwords = ['HoLa123@7','12345','2w3E*','2We3345']

Resultado:

HoLa123@7
"""

passwords = ['HoLa123@7','12345','2w3E*','2We3345']

minusculas = "abcdefghijklmnospqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOSPQRSTUVWXYZ"
numeros = "1234567890"
simbolos = "$#@"
LONG_MIN = 6
LONG_MAX = 12

for password in passwords:
    mayuscula = False
    minuscula = False
    numero = False
    simbolo = False

    if len(password) >= LONG_MIN and len(password)<= LONG_MAX:
        for letter in password:
            if mayuscula == False:
                if letter in mayusculas:
                    mayuscula = True
            if minuscula == False:
                if letter in minusculas:
                    minuscula = True
            if numero == False:
                if letter in numeros:
                    numero = True
            if simbolo == False:
                if letter in simbolos:
                    simbolo = True
        if minuscula and mayuscula and numero and simbolo:
            print(password)
    else:
        pass
