#include <stdio.h>

int factorial( int ) ;

void main( ){

    int number ;

    printf( "Insert a number: " ) ;
    scanf( "%d" , &number ) ;
    printf( "The factorial of the number is: %d" , factorial( number ) );

}

int factorial( int number ){
    if( number == 0 ){
        return 1;
    }

    return number * factorial( number -1 ) ;
}