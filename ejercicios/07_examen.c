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
    printf("Posteriormente te indicara los numeros que te solicito");
    printf("Primero desplegando el primer numero");
    printf("Y en seguida el segundo numero");

    // printf() dislpays the formatted output
    printf("\n	Ingresa el primer entero: ");
    scanf("%d", &number1);


    // printf() dislpays the formatted output
    printf("\n	Ingresa el segundo entero: ");
	scanf("%d", &number2);

	
    // printf() displays the formatted output
    printf("\n	Primer numero: %d", number1);
    printf("\n	Segundo numero: %d", number2);
    
    getch();

    return 0;
}
