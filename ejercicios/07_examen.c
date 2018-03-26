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
    int number1;
    int number2;

    // Print Menu
    printf("El siguiente programa te solicitara que ingreses dos numeros \n");
    printf("Posteriormente te indicara los numeros que te solicito \n");
    printf("Primero desplegando el primer numero\n");
    printf("Y en seguida el segundo numero\n");

    // printf() dislpays the formatted output
    printf("Ingresa el primer entero: ");

    // scanf() reads the formatted input and stores them
    scanf("%d", &number1);

    // printf() dislpays the formatted output
    printf("Ingresa el segundo entero: ");

    // scanf() reads the formatted input and stores them
    scanf("%d", &number2);

    // printf() displays the formatted output
    printf("Primer numero: %d \n", number1);
    printf("Segundo numero: %d", number2);

    return 0;
}
