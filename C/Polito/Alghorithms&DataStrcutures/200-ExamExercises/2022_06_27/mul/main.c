#include<stdio.h>
#include<stdlib.h>
#include<math.h>



void mul( int *v1 , int *v2 , int n , int **pv ){

    int *pv_local = ( int * ) malloc( 2 * n * sizeof( int ) ) ;
    int *tmp_arr = ( int * ) malloc( 2 * n * sizeof( int ) ) ;
    int num = 0 ;
    int tmp = 0 ;
    int num_shift = 0 ;

    for( int i = 0 ; i < 2*n ; i ++ ){
        pv_local[ i ] = 0 ;
        tmp_arr[ i ] = 0 ;
    }

    
    for( int i = 0 ; i < n ; i++ ){
        num = num + v1[ i ] * pow( 10 , n - i - 1 ) ; 
    }

    for( int j = n - 1 ; j >= 0 ; j-- ){

        for( int i = 0 ; i < 2*n ; i ++ ){
            tmp_arr[ i ] = 0 ;
        }

        tmp = num * v2[ j ] ;

        for( int k = 0 ; k < 2 * n  ; k++ ){
            tmp_arr[ k - num_shift ] = tmp / pow( 10 , 2*n - k - 1 ) ;
            tmp = tmp - tmp_arr[ k - num_shift ] * pow( 10 , 2*n - k - 1 ) ;
        }


        for( int f = 2*n - 1 ; f >= 0 ; f -- ){
            pv_local[ f ] = tmp_arr[ f ] + pv_local[ f ] ;
            if( pv_local[ f ] >= 10 ){
                pv_local[ f ] = pv_local[ f ] % 10 ;
                pv_local[ f - 1 ] = 1 ;
            }
        }
        num_shift++ ;
    }

    *pv = pv_local ;

}



void main( ){

    int v1[ ] = { 0 , 3 , 2 } ;
    int v2[ ] = { 2 , 4 , 3 } ;
    int *pv ;
    int n = 3 ;

    mul( v1 , v2 , n , &pv ) ;

    for( int i = 0 ; i < 2*n ; i++ ){
        printf( "%d " , pv[ i ] ) ;
    }
 


}