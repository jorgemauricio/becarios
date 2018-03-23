/*
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 5
# Valor: 10 puntos
# Corregir el siguiente código en c
*/
#include <stdio.h>
int main()
{
    int number1, number2;

    // Print Menu
    printf("El siguiente programa te solicitara que ingreses dos numeros");
    printf("\nPosteriormente te indicara los numeros que te solicito");
    printf("\nPrimero desplegando el primer numero");
    printf("\nY en seguida el segundo numero");

    // printf() dislpays the formatted output
    printf("\n\nIngresa el primer entero: ");

    // scanf() reads the formatted input and stores them
    scanf("%d", &number1);

    // printf() dislpays the formatted output
    printf("\nIngresa el segundo entero: ");

    // scanf() reads the formatted input and stores them
    scanf("%d", &number2);

    // printf() displays the formatted output
    printf("\nPrimer numero: %d", number1);
    printf("\nSegundo numero: %d", number2);

    return 0;
}
