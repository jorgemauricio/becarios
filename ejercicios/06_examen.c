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
	int num1, num2;
	printf("Ingresa el primer numero: ");
	scanf("%d", &num1);
	printf("Ingresa el segundo numero: ");
	scanf("%d", &num2);
	printf("La suma es: %d\n", num1 + num2);
	system("pause");
	return 0;
}