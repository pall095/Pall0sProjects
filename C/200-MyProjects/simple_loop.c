#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>



void main( int argc , char **argv ){

    clock_t t = clock( ) ;
    int n = atoi( argv[ 1 ] ) ;

    for( int i = 0 ; i < n ; i++ ){
        continue ;
    }

    t = clock( ) - t ;
    double time_taken = ( ( double ) t ) / CLOCKS_PER_SEC ;
    printf( "Time taken: %f s\n"  , time_taken )  ;

}
