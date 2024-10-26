#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define DIM1 5
#define DIM2 3

int main()
{
    FILE *main_fptr ;
    FILE *sub_fptr ;
    main_fptr = fopen( "main_matrix.txt" , "r" ) ;

    char main_matrix[ DIM1 ][ DIM1 ] ;
    char sub_matrix[ DIM2 ][ DIM2 ] ;
    char output_matrix[ DIM1 ][ DIM1 ] ;

    int i = 0 ;
    int j = 0 ;

    bool is_submatrix = true ;
    int r ;
    int c ;

    printf( "The main matrix is: \n") ;
    while( fscanf( main_fptr , "%s" , main_matrix[ i ] ) != EOF ){
        printf( "%s\n" , main_matrix[ i ] ) ;
        i++ ;
    }

    sub_fptr = fopen( "sub_matrix.txt" , "r" ) ;

    printf( "The sub matrix is: \n") ;
    while( fscanf( sub_fptr , "%s"  , sub_matrix[ j ] ) != EOF ){
        printf( "%s\n" , sub_matrix[ j ] ) ;
        j++ ;
    }


    for( i = 0 ; i < DIM1 ; i++ ){
        for( j = 0 ; j < DIM1 ; j++){
            output_matrix[ i ][ j ] = 'n' ;
        }
    }

    for( i = 0 ; i <= ( DIM1 - DIM2 ) ; i++){
        for( j = 0 ; j <= ( DIM1 - DIM2 ) ; j++ ){
            is_submatrix = true ;
            for( r = 0 ; r < DIM2 ; r ++ ){
                for( c = 0 ; c < DIM2 ; c ++ ){
                    if( main_matrix[ i + r ][ j + c ] != sub_matrix[ r ][ c ] ){
                        is_submatrix = false ;
                    }

                }
            }

            if( is_submatrix ){
                for( r = 0 ; r < DIM2 ; r ++ ){
                    for( c = 0 ; c < DIM2; c++ ){
                        output_matrix[ i + r ][ j + c ] = sub_matrix[ r ][ c ];
                    }
                }
            }
        }
    }

    printf( "The output is: \n") ;
    for( i = 0 ; i < DIM1 ; i++ ){
        for( j = 0 ; j < DIM1 ; j++ ){
                printf( "%c" , output_matrix[ i ][ j ] ) ;
        }
        printf( "\n") ;
    }


    fclose( main_fptr );
    fclose( sub_fptr ) ;
    return 0 ;


}
