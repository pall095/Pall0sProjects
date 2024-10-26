#include <stdio.h>
#include <stdlib.h>

#define DIM 5

int main()
{

    int i = 0 ;
    int array[ DIM ] = {} ;

    for( i = 0 ; i < DIM ; i++){
        printf( "Input a number: \n" ) ;
        scanf( "%d" , &array[ i ] ) ;
    }

    printf( "Original array is: \n") ;
    for( i = 0 ; i < DIM ; i ++ ){
        printf( "%d - " , array[ i ] ) ;
    }

    int j = 0 ;
    for( i = 0 ; i < DIM ; i++ ){

        if( array[ i ] != 0 ){
            array[ j ] = array[ i ] ;
            j++ ;
        }
    }

    printf( "Array with zeros removed is : \n") ;
    for( i = 0 ; i < j ; i ++ ){
        printf( "%d - " , array[ i ] ) ;
    }


}
