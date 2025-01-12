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

int how_many( int *sol , int n ){

    // Initialize a bitmask of zero.
    int *flagger = ( int * ) calloc( n , sizeof( int ) ) ;
    int sum = 0 ;

    // Setting bitmask values to 1 when a color is found.
    for( int i = 0 ; i < n ; i++ ){
        flagger[ sol[ i ] - 1 ] = 1 ; // -1 to recover from color shifting.
    }

    // Counting how many bits are ON.
    for( int i = 0 ; i < n ; i++ ){
        sum = sum + flagger[ i ] ;
    }

    free( flagger ) ;
    return( sum ) ;
}

// Simple print function.
void print_sol( int *sol , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%c:%d " , i + 'A' , sol[ i ] ) ;
    }
    printf( "- N colors %d\n" , how_many( sol , n ) ) ;
    return ;
}

int is_valid( int **graph , int *sol , int n ){

    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < n ; j++ ){
            if( graph[ i ][ j ] == 1 && sol[ i ] == sol[ j ] ){
                return 0 ;
            }
        }
    }
    return 1 ;
}



void permutate( int **graph , int n , int *sol , int depth ){

    if( depth >= n ){
        if( is_valid( graph , sol , n ) == 1 ){
            print_sol( sol , n ) ;
        }
        return ;
    }

    for( int i = 0 ; i < n ; i++ ){
        sol[ depth ] = i + 1 ; // + 1 to shift upwards colors so not to use 0 as valid color.
        permutate( graph , n , sol , depth + 1 ) ;
    }
    return ;

}

void color( int **graph , int n ){

    int *sol = ( int * ) calloc( n , sizeof( int ) ) ;
    permutate( graph , n , sol , 0 ) ;




}


void main( int argc , char **argv ){

    int row = 4 ;
    int col = 4 ;
    int **mat = mat_from_file( argv[ 1 ] , row , col ) ;
    color( mat , row ) ;


}
