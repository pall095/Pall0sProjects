#include "setPrivate.h"

set_t set_from_file( char *filename ){

    FILE *file_ptr = fopen( filename , "r" ) ;
    set_t set ;
    char current ;
    int i = 0 ;
    int count = 0 ;

    if( file_ptr == NULL ){
        printf( "Unable to open the file!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }

    while( fscanf( file_ptr , "%c" , &current ) != EOF ){
        if( current != '\n' && current != '\0' ){
            count = count + 1 ;
        }
    }
    fclose( file_ptr );

    set.num_choiches = count ;
    set.choiches = ( char * ) malloc( set.num_choiches * sizeof( char ) ) ;

    file_ptr = fopen( filename , "r" ) ;
    while( fscanf( file_ptr , "%c" , &current ) != EOF  ){
        
        if( current != '\n' && current != '\0' ){
            set.choiches[ i ] = current ;
            i++ ;
        }
    }

    return set ;
} 

void print_set( set_t s ){
    for( int i = 0 ; i < s.num_choiches ; i++ ){
        printf( "%c " , s.choiches[ i ] ) ;
    }
    printf( "\n" ) ;
}



