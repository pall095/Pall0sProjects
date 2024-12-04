#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<ctype.h>


#define BUFFER 100

// Declaring structure for the set
typedef struct set_s{
    int num_choiches ;
    char *choiches ;
} set_t ;

// Just for debuggin.
void print_set( set_t *set , int len ){
    for( int i = 0 ; i < len ; i++ ){
        for( int j = 0 ; j < set[ i ].num_choiches ; j++ ){
            printf( "%c " , set[ i ].choiches[ j ] );
        }
        printf( "\n" ) ;
    }
    return ;
}


// Function to apply multiplication principle.
// With respect to standard algorithm takes two more inputs:
// need_num = indicates if the next step of the solution needs a number or a char.
// f_ptr pointer to the output file where to store the solution.
void mult_princ( set_t *set , char *sol , int len , int depth , int need_num  , FILE *f_ptr ){

    // If depth reached, print solution to file.
    if( depth >= len ){

        for( int k = 0 ; k < len ; k++ ){
            fprintf( f_ptr , "%c " , sol[ k ] ) ;
        }

        fprintf( f_ptr , "\n" ) ;
        return ;
    }

    // Iterates through the possible choiches (verifying it is the correct char or digit )
    // and calls recursion.
    for( int i = 0 ; i < set[ depth ].num_choiches ; i++ ){

        if( need_num == 1 ){

            if( isdigit( set[ depth ].choiches[ i ] ) == 1 ){
                sol[ depth ] = set[ depth ].choiches[ i ] ;
                mult_princ( set , sol , len , depth + 1 , 0 , f_ptr ) ;
            }

        }else{

            if( isalpha( set[ depth ].choiches[ i ] ) != 0  ){
                sol[ depth ] = set[ depth ].choiches[ i ] ;
                mult_princ( set , sol , len , depth + 1 , 1 , f_ptr ) ;
            }
        }
    }   
}


// Core function
void acronym( char *filename_input , char *filename_output ) {
    
    FILE *f_in = fopen( filename_input , "r" ) ;
    FILE *f_out = fopen( filename_output , "w" ) ;
    int len ;
    char current_string[ BUFFER ] ; 
    char *sol ;
    set_t *set ; 
    int i = 0 ;
    
    if( f_in == NULL ){
        printf( "Unable to open the input file!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }

    if( f_out == NULL ){
        printf( "Unable to open the output file!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }

    // reading solution len and length of the file.
    fscanf( f_in , "%d" , &len ) ;
    
    // Allocating sets and solution.
    set = ( set_t* ) malloc( len * sizeof( set_t ) ) ;
    sol = ( char* ) malloc( len * sizeof( char ) ) ;
    
    // Reading set from file.
    // TO DO: is there a way to avoid having to use a pre-allocated string of size == BUFFER?
    while( fscanf( f_in , "%s" , &current_string ) != EOF ){
        
        set[ i ].num_choiches = strlen( current_string ) ;
        set[ i ].choiches = ( char* ) malloc( strlen( current_string ) * sizeof( char ) ) ;
        
        for( int j = 0 ; j < strlen( current_string ) ; j++ ){

            if( current_string[ j ] != '\0' ){
                set[ i ].choiches[ j ] = current_string[ j ] ;
            }
        }
        i++ ; 
    }
    fclose( f_in ) ;

    // Initiating recursion
    mult_princ( set , sol , len , 0 , 0 , f_out ) ;
    mult_princ( set , sol , len , 0 , 1 , f_out ) ;
    fclose( f_out ) ;
    
    // Clearing out.
    for( int i = 0 ; i < len ; i++ ){
        free( set[ i ].choiches ) ;
    }
    free( set ) ;

}

void main( int argc , char **argv ){
    int len ; 
    acronym( argv[ 1 ] , argv[ 2 ] ) ;
}








