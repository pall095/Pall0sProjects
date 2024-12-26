#include<stdio.h>
#include<stdlib.h>

#define SIZE 6 

void check( int m[ SIZE ][ SIZE ] , int n , int k ){


    int max_r , max_c ;
    int min_r , min_c ;

    int MIN = INT_MAX ;
    int MAX = INT_MIN ;

    int i , j , ii , jj ;
    int tmp ;

    for( i = 0 ; i <= n - k ; i++ ){
        for( j = 0 ; j <= n - k ; j++ ){

            tmp = 0 ;

            for( ii = 0 ; ii < k ; ii++ ){
                for( jj = 0 ; jj < k ; jj++ ){
                    tmp = tmp + m[ i + ii ][ j + jj ] ;
                }
            }


            if( tmp > MAX ){
                MAX = tmp ;
                max_r = i ;
                max_c = j ;
            }

            if( tmp <= MIN ){
                MIN = tmp ;
                min_r = i ;
                min_c = j ;
            }
        }
    }


    for( i = max_r ; i < max_r + k ; i++ ){
        for( j = max_c ; j < max_c + k ; j++ ){
            printf( "%d " , m[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }

    printf( "---\n" ) ;
    
    for( i = min_r ; i < min_r + k ; i++ ){
        for( j = min_c ; j < min_c + k ; j++ ){
            printf( "%d " , m[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }

    return ;

}

void main( ){

    int matrix[ SIZE ][ SIZE ] = { { 0 , 1 , 0 , 1 , 0 , 1 } , 
                                { 1 , 0 , 1 , 0 , 1 , 0 } , 
                                { 0 , 1 , 0 , 0 , 0 , 1 } ,
                                { 1 , 0 , 1 , 0 , 1 , 0 } ,
                                { 0 , 1 , 0 , 0 , 0 , 0 } ,
                                { 3 , 0 , 1 , 0 , 2 , 0 } } ;

    check( matrix , 6 , 3 ) ;





}