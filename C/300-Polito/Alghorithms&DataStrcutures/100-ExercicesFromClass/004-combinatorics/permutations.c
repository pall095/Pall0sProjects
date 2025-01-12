#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>

void print_sol( int *sol , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%d " , sol[ i ] ) ;
    }
    printf( "\n" ) ;
    return ;
}

void permutations_r( int *arr , int *sol , int *marker , int n , int depth , int *count , int verbose ){

    if( depth >= n ){
        *count = *count + 1 ;
        if( verbose == 1 ){
            print_sol( sol , n ) ;
        }
        return ;
    }

    for( int i = 0 ; i < n ; i++ ){
        if( marker[ i ] == 0 ){
            marker[ i ] = 1 ;
            sol[ depth ] = arr[ i ] ;
            permutations_r( arr , sol , marker , n , depth + 1 , count , verbose ) ;
            marker[ i ] = 0 ;
        }
    }

}


int permutations( int n , int verbose ){

    int count = 0 ;
    int *arr = ( int * ) calloc( n , sizeof( int ) ) ;
    int *sol = ( int * ) calloc( n , sizeof( int ) ) ;
    int *marker = ( int * ) calloc( n , sizeof( int ) ) ;

    for( int i = 0 ; i < n ; i++ ){  
        arr[ i ] = i + 1 ;
    }

    permutations_r( arr , sol , marker , n , 0 , &count , verbose ) ;
    return count ;

    free( arr ) ;
    free( sol ) ;
    free( marker ) ;

}




void main( int argc , char **argv ){

    clock_t t = clock( ) ;
    int n = atoi( argv[ 1 ] ) ;
    int verbose = atoi( argv[ 2 ] ) ;
    int count = permutations( n , verbose ) ;
    t = clock( ) - t ;
    double time_taken = ( ( double ) t ) / CLOCKS_PER_SEC ;
    printf( "Time taken: %f s\n"  , time_taken )  ;
    printf( "Number of permutations: %d\n" , count ) ;



}
