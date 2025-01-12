#include<stdio.h>
#include<stdlib.h>


#define N 4 

void local_max( int mat[ N ][ N ] , int n , int k ){


    int max_row , max_col ;
    int max_value = INT_MIN ;
    int tmp_sum = 0 ;

    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < n ; j++ ){

            tmp_sum = 0 ;

            for( int ii = -k ; ii <= k ; ii++ ){
                for( int jj = -k ; jj <= k ; jj++ ){

                    if( i + ii >= 0 && i + ii < n && j + jj  >= 0 && j + jj < n ){
                        tmp_sum = tmp_sum + mat[ i + ii ][ j + jj ] ;
                    }
                }
            }

            if( tmp_sum > max_value ){
                max_value = tmp_sum ;
                max_row = i ;
                max_col = j ;
            }

        }
    }

    printf( "%d - %d \n" , max_row , max_col ) ;

}


void main( ){


    int mat[ N ][ N ] = { { 3 , 2 , 1 , 1 } , { 2 , 4 , 1 , 1 } , { 0 , 1 , 0 , 0 } , { 1 , 0 , 1 , 2 } } ;
    local_max( mat , 4 , 2 ) ; 



}