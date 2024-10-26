#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define NUM_CLASS 10

int main()
{
    int array[ NUM_CLASS ] = { 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0 } ;
    bool end = false ;
    int current_num ;

    while( !end ){

        printf( "Input a number: \n" ) ;
        scanf( "%d" , &current_num ) ;

        if( current_num < 0 || current_num > 10 * NUM_CLASS ){
            end = true ;
            break ;
        }
        array[ current_num / NUM_CLASS ]++ ;
    }


    for( int i = 0 ; i < NUM_CLASS ; i++ ){

        printf( "Class %d - %d : " , i*NUM_CLASS , (i*NUM_CLASS + NUM_CLASS - 1 ) ) ;
        for( int j = 0 ; j < array[ i ] ; j++ ){
            printf( "#" ) ;
        }
        printf( "\n" ) ;

    }

    return 0 ;

}
