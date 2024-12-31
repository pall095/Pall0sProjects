#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<float.h>

void copy_sol( float *sol , float **best_sol , int n ){
    float *local_best = ( float * ) calloc( n , sizeof( float ) ) ;
    for( int i = 0 ; i < n ; i++ ){
        local_best[ i ] = sol[ i ] ;
    }

    *best_sol = local_best ;
    free( local_best ) ;
    return ;
}

float eval( float *sol  , int n ){
    float tmp = 0 ;
    for( int i = 0 ; i < n ; i++ ){
        tmp = tmp + sol[ i ] ;
    }
    return tmp ;

}

void permutate( float weight[ 5 ] , float value[ 5 ] ,  int *marker , float *sol_weight , float *sol_value , int n , float load , int depth , float *best_value , float **best_sol_weight , float **best_sol_value ){

    if( depth >= n || eval( sol_value , n ) > *best_value ){

        if( eval( sol_value , n ) > *best_value && eval( sol_weight , n ) < load ){
            *best_value = eval( sol_value , n ) ;
            copy_sol( sol_value , best_sol_value , n ) ; 
            copy_sol( sol_weight , best_sol_weight , n ) ;
        }
        return ;
    }

    for( int i = 0 ; i < n ; i++ ){
        if( marker[ i ] == 0 ){
            marker[ i ] = 1 ;
            sol_weight[ depth ] = weight[ i ] ;
            sol_value[ depth ] = value[ i ] ;
            permutate( weight , value , marker , sol_weight , sol_value , n , load , depth + 1 , best_value , best_sol_value , best_sol_weight ) ;
            marker[ i ] = 0 ;
            sol_weight[ i ] = 0 ;
            sol_value[ i ] = 0 ;
        }
    }
}

void load_truck( float weight[ 5 ] , float value[ 5 ] , int n , float load ){

    int *marker = ( int* ) calloc( n , sizeof( int ) ) ;
    float *sol_weight = ( float* ) calloc( n , sizeof( float ) ) ;
    float *sol_value = ( float* ) calloc( n , sizeof( float ) ) ;
    float *best_sol_weight = ( float* ) calloc( n , sizeof( float ) ) ;
    float *best_sol_value = ( float* ) calloc( n , sizeof( float ) ) ;
    float best_value = FLT_MIN ;

    permutate( weight , value , marker , sol_weight , sol_value , n , load , 0 , &best_value , &best_sol_weight , &best_sol_value ) ;

    printf( "Best weights are: ") ;
    for( int i = 0 ; i < n ; i++ ){
        printf( "%.2f " , best_sol_weight[ i ] ) ;
    }
    printf( " - Total weight is: %.2f" , eval( best_sol_weight , n ) ) ;

    printf( "\n" ) ;
    printf( "Best values are: ") ;
    for( int i = 0 ; i < n ; i++ ){
        printf( "%.2f " , best_sol_value[ i ] ) ;
    }
    printf( " - Total value is: %.2f" , eval( best_sol_value , n ) ) ;

    free( sol_weight ) ;
    free( sol_value ) ;
    free( best_sol_weight ) ;
    free( best_sol_value ) ;

}


void main( ){
    float weight[ 5 ] = {10.0, 15.0, 25.5, 39.5, 17.0 } ;
    float value[ 5 ] = { 19.99, 9.50, 15.00, 27.50, 11.40 } ;
    int n = 5 ;
    int load = 50 ;
    load_truck( weight , value , n , load ) ;
}