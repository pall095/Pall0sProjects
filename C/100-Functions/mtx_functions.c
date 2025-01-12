#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

void print_mat( int **mat , int row , int col ){
    for( int i = 0 ; i < row ; i++ ){
        for( int j = 0 ; j < col ; j++ ){
            printf( "%d " , mat[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
    printf( "\n" ) ;
    return ;
}

int **mat_from_file( char *filename , int row , int col ){

    FILE *f_ptr = fopen( filename , "r" ) ;
    int **mat ;
    char *current_line ; // <-- Buffer line to read the file.
    int i , j ;

    // Checking if file opened correctly
    if( f_ptr == NULL ){
        printf( "Unable to open the file %s!\n" , filename ) ;
        return NULL ; 
    }

    //Initializing matrix
    mat = ( int** ) calloc( row , sizeof( int*) ) ;

    if( mat == NULL ){
        printf( "Unable to allocate matrix!\n" ) ;
        return NULL ; 
    }

    for( int i = 0 ; i < col ; i++ ){
        mat[ i ] = ( int* ) calloc( col , sizeof( int ) ) ;
        if( mat[ i ] == NULL ){
            printf( "Unable to allocate memory for %d line!\n" , i ) ;
            return NULL ; 
        } 
    }

    //Initializing support variables to read.
    current_line = ( char * ) calloc( col + 1 , sizeof( int ) ) ; 
    i = 0 ;
    j = 0 ;

    //Reading
    while( fscanf( f_ptr , "%s" , current_line ) != EOF ){
        for( j = 0 ; j < col ; j++ ){
            mat[ i ][ j ] = current_line[ j ] - '0' ;
        }
        i++ ;
    }

    fclose( f_ptr ) ;
    return mat ;

}

void main( int argc , char **argv ){

    int row = 9 ;
    int col = 9 ;
    int **mat = mat_from_file( argv[ 1 ] , row , col ) ;
    print_mat( mat , row , col ) ;


}