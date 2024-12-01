#include<stdio.h>
#include<stdlib.h>
#include<math.h>


#define SIZE 6

void check( int m[ SIZE ][ SIZE ] , int n , int k ){

    int n_sun_m = n / k ;
    int tmp_sum = 0 ;
    int max = 0 ;
    int min = 10000 ;
    int max_start_row = 0  ;
    int max_start_col = 0 ;
    int min_start_row = 0 ;
    int min_start_col = 0 ;


    for( int i = 0 ; i <= n - k ; i++ ){

        for( int j = 0 ; j <= n - k ; j++ ){

                tmp_sum = 0 ;

                for( int y = 0 ; y < k ; y++ ){
                    for( int x = 0 ; x < k ; x++ ){
                        tmp_sum = tmp_sum + m[ i + y ][ j + x ] ;
                    }
                }

                printf( "%d \n" , tmp_sum ) ;


                if( tmp_sum > max ){
                    max = tmp_sum ;
                    max_start_col = j ;
                    max_start_row = i ;
                }

                if( tmp_sum < min ){
                    min = tmp_sum ;
                    min_start_col = j ;
                    min_start_row = i ;
                }

        }
    }


    printf( "The min matrix is and the min is %d: \n" , min ) ;

    for( int i = min_start_row ; i < min_start_row + k ; i++ ){
        for( int j = min_start_col ; j < min_start_col + k ; j++ ){

            printf( "%d " , m[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }

    printf( "The max matrix is and the max is %d: \n" , max ) ;

    for( int i = max_start_row ; i < max_start_row + k ; i++ ){
        for( int j = max_start_col ; j < max_start_col + k ; j++ ){

            printf( "%d " , m[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
}


void main( ){

    int matrix[ SIZE ][ SIZE ] = { { 0 , 1 , 0 , 1 , 0 , 1 } , 
                                   { 1 , 0 , 1 , 0 , 1 , 0 } , 
                                   { 0 , 1 , 0 , 0 , 0 , 1 } ,
                                   { 1 , 0 , 1 , 0 , 1 , 0 } ,
                                   { 0 , 1 , 0 , 0 , 0 , 0 } ,
                                   { 3 , 0 , 1 , 0 , 2 , 0 } } ;

    for( int i = 0 ; i < SIZE ; i++ ){
        for( int j = 0 ; j < SIZE ; j++ ){
            printf( "%d " , matrix[ i ][ j ]  ) ;
        }
        printf( "\n" ) ;
    }

    check( matrix , SIZE , 3 ) ;


}