#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAX_BIT 10

void d2b( int , int* , int* ) ;



void main( int argc , char **argv ){


    int decimal = atoi( argv[ 1 ] ) ;
    int binary[ MAX_BIT ] ;
    int num_bit = 0 ;

    d2b( decimal , binary , &num_bit ) ;
    for( int i = num_bit - 1  ; i >= 0 ; i-- ){
    
        printf( "%d" , binary[ i ] ) ;
    }

}


void d2b( int num , int *bit_array , int *bit_pos ){

    
    if( num == 0 ){
        return ;
    }

    bit_array[ *bit_pos ] = num % 2 ;
    *(bit_pos) = *bit_pos + 1 ;
    d2b( num / 2 , bit_array , bit_pos ) ;

}