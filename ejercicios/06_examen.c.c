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

#include <stdlib.h>
int main()
{
    int n1, n2;

    printf( "\n   Introduzca el primer numero (entero): " );
    scanf( "%d", &n1 );

    printf( "\n   Introduzca el segundo numero (entero): " );
    scanf( "%d", &n2 );

    printf( "\n   La suma es: %d", n1 + n2 );
     getch(); /* Pausa */

    return 0;
}
