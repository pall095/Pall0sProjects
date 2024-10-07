#ifndef FUNCTIONS_H_INCLUDED
#define FUNCTIONS_H_INCLUDED

#include <math.h>

int print_grid( int grid[ 9 ][ 9 ] , int WIDTH ){

    int row , col ;
    printf( "-------------------------------\n") ;
    for( row = 0 ; row < WIDTH ; row++ ){
        for( col = 0 ; col < WIDTH ; col++){

            if( col == 0 ){
                printf( "|" );
            }

            printf( " %d ", grid[ row ][ col ] ) ;

            if( (int)fmod( (col + 1 ) , 3 ) == 0 ) {
                printf( "|") ;
            }
        }
        if( (int)fmod( ( row + 1 ) , 3 ) == 0 ){
            printf( "\n-------------------------------") ;
        }
        printf("\n" ) ;
    }



}

void read_grid( char *file_name , int grid[ 9 ][ 9 ] , int WIDTH , bool verbose ){

    FILE *file_ptr ;
    int row = 0 ;
    int col = 0 ;
    char line[ WIDTH ] ;
    file_ptr = fopen( file_name , "r" ) ;
    int current_num ;

    while( fgets( line , WIDTH + 2 , file_ptr) != NULL ){
        for( col = 0 ; col < WIDTH ; col++ ){
            current_num = line[ col ] - '0' ;
            grid[ row ][ col ] = current_num ;
            if( verbose ){
                printf( "Num: %d , Row: %d , Col: %d \n" , current_num , row , col );
            }
        }
        row++ ;
    }
 }


#endif // FUNCTIONS_H_INCLUDED
