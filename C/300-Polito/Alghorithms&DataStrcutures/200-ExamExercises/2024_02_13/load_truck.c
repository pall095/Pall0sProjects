#include<stdio.h>
#include<stdlib.h>
#include<math.h>


float calc_value( float *value , int n ){
    float val = 0 ;
    for( int i = 0 ; i < n ; i++ ){
        val = val + value[ i ] ;
    }
    return val ;
}

float calc_weight( float *w, int n ){
    float weight = 0 ;
    for( int i = 0 ; i < n ; i++ ){
        weight =  weight + w[ i ] ;
    }
    return weight ;
}


void permutate( float *weight , float *value , int n , int load , int *marker , float *sol_v , float *sol_w , int depth , float*best_v , float *best_w ){


    if( depth >= n ){
        return ;
    }

    for( int i = 0 ; i < n ; i++ ){

        if( marker[ i ] == 0 ){
            marker[ i ] = 1 ;
            sol_v[ depth ] = value[ i ] ;
            sol_w[ depth ] = weight[ i ] ;

            if( calc_value( sol_v , n ) > calc_value( best_v , n ) && calc_weight( sol_w , n ) <= load ){
                for( int j = 0 ; j < n ; j++ ){
                    best_v[ j ] = sol_v[ j ] ;
                    best_w[ j ] = sol_w[ j ] ;
                }
            }

            permutate( weight , value , n , load , marker , sol_v , sol_w , depth + 1 , best_v , best_w ) ;
            marker[ i ] = 0 ;
            sol_v[ depth ] = 0 ;
            sol_w[ depth ] = 0 ;
        }
    }
}


void load_truck( float *weight , float *value , int n , int load ){

    int *marker = ( int * ) malloc( n * sizeof( int ) ) ;
    float *sol_v = ( float * ) malloc( n * sizeof( float ) ) ;
    float *sol_w = ( float * ) malloc( n * sizeof( float ) ) ;
    float *best_v = ( float * ) malloc( n * sizeof( float ) ) ;
    float *best_w = ( float * ) malloc( n * sizeof( float ) ) ;

    for( int i = 0 ; i < n ; i++ ){
        marker[ i ] = 0 ;
        sol_v[ i ] = 0 ;
        sol_w[ i ] = 0 ;
        best_v[ i ] = 0 ;
        best_w[ i ] = 0 ;
    }
    permutate( weight , value , n , load , marker , sol_v ,sol_w , 0 , best_v , best_w ) ;

    printf( "The best value items are priced as follow: \n") ;
    for( int i = 0 ; i < n ; i++ ){
        printf( "%f " , best_v[ i ]  ) ;
    }

    printf( "\n" ) ;

    printf( "The best weight items are priced as follow: \n") ;
    for( int i = 0 ; i < n ; i++ ){
        printf( "%f " , best_w[ i ]  ) ;
    }

}

void main( ){

    float value[ ] = {19.99, 9.50, 15.00, 27.50, 11.40} ;
    float weight[ ] =  {10.0, 15.0,25.5, 39.5, 17.0} ;
    int n = 5 ;
    int load = 50 ;

    load_truck( weight , value , n , load ) ;

}