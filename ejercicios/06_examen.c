
int main()
{
    int n1, n2, suma;

    printf( "\n   Introducir el primer numero: " );
    scanf( "%d", &n1 );
    printf( "\n   Introducir el segundo numero: " );
    scanf( "%d", &n2 );

    suma = n1 + n2;
    
    printf( "\n   La suma es: %d", suma );
   
    getch(); /* Pausa */

    return 0;
}
