#include <stdio.h>
#include <stdlib.h>
#include <float.h>



void searchSubArray( float v[ 10 ] , float n , float k ){

    float *sub_max_sum = ( float *) malloc( k * sizeof( float ) ) ;
    float *sub_max_diff = ( float *) malloc( k * sizeof( float ) ) ;

    float max_sum = FLT_MIN ;
    float max_diff = FLT_MIN ;
    float curr_max ;
    float curr_min ;

    for( int i = 0 ; i < n - k ; i++ ){

        curr_max = FLT_MIN ;
        curr_min = FLT_MAX ;

        if( v[ i ] + v[ i + 1 ] + v[ i + 2] > max_sum ){
            max_sum = v[ i ] + v[ i + 1 ] + v[ i + 2 ] ;
            sub_max_sum[ 0 ] = v[ i ] ;
            sub_max_sum[ 1 ] = v[ i + 1 ] ;
            sub_max_sum[ 2 ] = v[ i +  2 ] ;
        }

        for( int j = i ; j < i + k ; j++ ){

            if( v[ j ] > curr_max ){
                curr_max = v[ j ] ;
            }

            if( v[ j ] < curr_min ){
                curr_min = v[ j ] ;
            }
        }

        if( curr_max - curr_min > max_diff ){
            max_diff = curr_max - curr_min ;
            sub_max_diff[ 0 ] = v[ i ] ;
            sub_max_diff[ 1 ] = v[ i + 1 ] ;
            sub_max_diff[ 2 ] = v[ i + 2 ] ;
        }


    }
        
    for( int i = 0 ; i < k ; i++ ){
        printf( "%f " , sub_max_sum[ i ] ) ;
    }

    printf( "\n" ) ;

    for( int i = 0 ; i < k ; i++ ){
       printf( "%f " , sub_max_diff[ i ] ) ;
    }

    printf( "\n" ) ;

}


void main( ){


    float v[ 10 ] = { 12.5 , 2.1, 3.3, 4.1, 5.4, 6.2, 7.9, 8.3, -9.9 , 5.1 }  ;

    searchSubArray( v , 10 , 3 ) ;




}