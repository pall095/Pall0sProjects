#include<stdio.h>
#include<stdlib.h>
#include<float.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<time.h>

void print_sol( int *sol , int n ){
    printf( "{ " ) ; 
    for( int i = 0 ; i < n ; i++ ){
        printf( "%d " , sol[ i ] ) ;
    }
    printf( "}" ) ;
    printf( "\n" ) ;
    return ;
}

void simple_combinations_r( int *arr , int len , int n , int start , int depth , int *sol ){

    if( depth >= n ){
        print_sol( sol , n ) ;
        return ;
    }

    for( int i = start ; i < len ; i++ ){
        sol[ depth ] = arr[ i ] ;
        simple_combinations_r( arr , len , n , i + 1 , depth + 1 , sol ) ;
    }


}

void simple_combinations( int *arr , int len , int n ){
    int *sol = ( int * ) calloc( n , sizeof( int ) ) ;
    int depth = 0 ;
    simple_combinations_r( arr , len , n , 0 , 0 , sol ) ;
    free( sol ) ;

}

void generate_powerset( int *arr , int n ){
    for( int i = 1 ; i <= n ; i++ ){
        simple_combinations( arr , n , i ) ;
    }

}

void main( int argc , char **argv ){

    clock_t t = clock( ) ;
    int n = atoi( argv[ 1 ] ) ;
    int verbose = atoi( argv[ 2 ] ) ;
    int *arr = ( int * ) calloc( n , sizeof( int ) ) ;
    printf( "%d\n" , n ) ;

    for( int i = 0 ; i < n ; i++ ){
        arr[ i ] = i + 1 ;
    }
    generate_powerset(  arr , n ) ;
    t = clock( ) - t ;
    double time_taken = ( ( double ) t ) / CLOCKS_PER_SEC ;
    printf( "Time taken: %f\n"  , time_taken )  ;
}