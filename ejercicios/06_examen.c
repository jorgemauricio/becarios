/*
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 5
# Valor: 10 puntos
# El siguiente programa pide al usuario 2 números
# para posteriormente sumarlos e imprimir
# el resultado
*/
#include <stdio.h>

int main()
{
    int a, b, suma;

    printf( "\n   Introducir el primer numero: " );
    scanf ( "%d", &a );
    printf( "\n   Introducir el segundo numero: " );
    scanf ( "%d", &b );

    suma = a + b;
    
    printf( "\n   La suma de los dos numeros es: %d", suma );

    return 0;
}
