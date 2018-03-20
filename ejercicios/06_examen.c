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
int main()
{
    int n1, n2, suma;

    printf( "\n   Introducir el primer numero: " );
    scanf ( "%d", &n1 );
    printf( "\n   Introducir el segundo numero: " );
    scanf ( "%d", &n2 );

    suma = n1 + n2;
    
    printf( "\n   La suma de los dos numeros es: %d", suma );
   
    getch(); /* Pausa */

    return 0;
}
