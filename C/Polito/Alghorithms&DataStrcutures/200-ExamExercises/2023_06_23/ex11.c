#include <stdio.h>
#include <stdlib.h>





int max_diff( int mat[ 4 ][ 5 ] , int r , int c ){

    int k = 0 ;
    int curr_min = INT_MAX ;
    int curr_max = INT_MIN ;
    int max_diff = INT_MIN ;
    int max_row , max_col ;


    for( int i = 0 ; i < r ; i++ ){
        for( int j = 0 ; j < c ; j++ ){

            k = 1 ;

            while( i + k < r && j + k < c &&  i - k >= 0 && j - k >= 0 ){

                if( mat[ i + k ][ j + k ] > curr_max ){
                    curr_max = mat[ i + k ][ j + k ] ;
                }

                if( mat[ i + k ][ j + k ] < curr_min ){
                    curr_min = mat[ i + k ][ j + k ] ;
                }

                if( mat[ i - k ][ j - k ] > curr_max ){
                    curr_max = mat[ i - k ][ j - k ] ;
                }

                if( mat[ i - k ][ j - k ] < curr_min ){
                    curr_min = mat[ i - k ][ j - k ] ;
                }

                if( mat[ i + k ][ j - k ] > curr_max ){
                    curr_max = mat[ i + k ][ j - k ] ;
                }

                if( mat[ i + k ][ j - k ] < curr_min ){
                    curr_min = mat[ i + k ][ j - k ] ;
                }

                if( mat[ i - k ][ j + k ] > curr_max ){
                    curr_max = mat[ i - k ][ j + k ] ;
                }

                if( mat[ i - k ][ j + k ] < curr_min ){
                    curr_min = mat[ i - k ][ j + k ] ;
                }


                k++ ;
            }


            if( curr_max - curr_min > max_diff ){
                max_diff = curr_max - curr_min ;
                max_row = i ;
                max_col = j ;
            }

        }
    }

    printf( "Row: %d - col : %d - max diff : %d \n" , max_row + 1 , max_col +  1, max_diff ) ;
    return max_diff ;

}


void main( ){

    int mat[ 4 ][ 5 ] = { { 0 , -2 , 1 , 0 , 0  } , 
                        { 0 , 0 , 1 , 0  , 2 } , 
                        { 0 , 0 , 0 , 1 , 1 } , 
                        { 1 , 0 , 5 , 0 , 0 } } ;

    int max = max_diff( mat , 4 , 5 ) ;

}