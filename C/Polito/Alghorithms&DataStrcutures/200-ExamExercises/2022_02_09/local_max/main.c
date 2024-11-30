#include <stdio.h>
#include <stdlib.h>

int** init_mat( int ) ;
void print_mat( int** , int ) ;
void local_max( int** , int , int ) ;

void main( int argc , char **argv ){


    int **mat ;
    int size ;
    int k ;

    printf( "Insert size: " ) ;
    scanf( "%d" , &size ) ;

    printf( "Insert window size: " ) ;
    scanf( "%d" , &k ) ;

    mat = init_mat( size ) ;
    print_mat( mat , size ) ;
    local_max( mat , size , k ) ;
}


int** init_mat( int size  ){
    int **mat = ( int ** ) malloc( size * size +sizeof( int ) ) ;
    for( int i = 0 ; i < size ; i++ ){
        mat[ i ] = ( int * ) malloc( size * sizeof( int ) ) ;
    }

    for( int i = 0 ; i < size ; i++ ){
        for( int j = 0 ; j < size; j++ ){
            mat[ i ][ j ] = rand( ) % 10 ;
        }
    }
    return mat ;
}


void print_mat( int **mat , int size ){
    for( int i = 0 ; i < size ; i++ ){
        for( int j = 0 ; j < size ; j++ ){
            printf( "%d " , mat[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }

}

void local_max( int **mat , int n , int k ){

    int start_row = 0 ;
    int start_col = 0 ;
    int local_max = 0 ;
    int max_row = 0 ;
    int max_col = 0 ;

    while( ( start_row + k ) <= n ){
        local_max = 0 ;
        for( int i = start_row ; i < start_row + k ; i++ ){
            for( int j = start_col ; j < start_col + k ; j++ ){

                if( mat[ i ][ j ] > local_max ){
                    local_max = mat[ i ][ j ] ;
                    max_row = i ;
                    max_col = j ;
                }
            }
        }

        printf( "Maximum for window starting at %d %d is %d with coord %d %d\n" , start_row + 1 , start_col + 1 , local_max , max_row + 1 , max_col + 1 ) ;

        if( start_col + k >= n ){
            start_col = 0 ;
            start_row = start_row + 1 ;
        }else{
            start_col = start_col + 1;
        }


    }


}