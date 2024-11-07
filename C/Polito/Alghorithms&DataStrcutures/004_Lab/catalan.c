#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int catalan( int ) ;

void main( int argc , char **argv ){
    
    int num = atoi( argv[ 1 ] ) ;
    printf( "Catalan of %d is: %d" , num ,  catalan( num) ) ;
}


int catalan( int num ){
    
    if( num == 0 ){
        return 1;
    }
    
    int cat = 0 ;

    for( int i = 0 ; i < num ; i++ ){
        cat = cat + catalan( i )*catalan( num -  1 - i ) ;
    }

    return cat ;

}