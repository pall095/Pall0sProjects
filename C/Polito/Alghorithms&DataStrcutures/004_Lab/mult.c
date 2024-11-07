#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int mult( int , int ) ;

void main( int argc , char **argv ){


    int num1 = atoi( argv[ 1 ] ) ;
    int num2 = atoi( argv[ 2 ] ) ;

    printf( "The result of the multiplication %d and %d is %d" , num1 , num2 , mult( num1 , num2 ) ) ;



}

int mult( int n1 , int n2 ){

    if( n2 == 1 ){
        return n1 ;
    }

    return ( n1 + mult( n1 , n2 - 1 ) ) ;
}