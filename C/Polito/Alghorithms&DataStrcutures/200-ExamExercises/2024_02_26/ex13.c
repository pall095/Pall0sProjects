#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>

#define BUF 101

typedef struct set_s{

    int size ;
    char *str ;

} set_t ;

void print_set( set_t set ){
    printf( "Set size: %d\n" , set.size ) ;
    for( int i = 0 ; i < set.size ; i++ ){
        printf( "%c" , set.str[ i ] ) ;
    }
    printf( "\n" ) ;
}

void print_superset( set_t *superset , int n ){

    for( int i = 0 ; i < n ; i++ ){
        print_set( superset[ i ] ) ;
    }
    printf( "\n" ) ;
    return ;
}

set_t* read_file( char *filename , int *n ){

    FILE *ptr = fopen( filename , "r" ) ;
    char tmp_string[ BUF ] ;
    set_t set ;
    int k = 0 ;
    fscanf( ptr , "%d" , n ) ;
    set_t *superset = ( set_t* ) calloc( *n , sizeof( set_t ) ) ;
    while( fscanf( ptr , "%s" , tmp_string ) != EOF ){

        set.size = strlen( tmp_string ) ;
        set.str = strdup( tmp_string ) ;
        superset[ k ] = set ;
        k++ ;

    }

    fclose( ptr ) ;
    return superset ; 
    
}

int is_consistend( char *sol , int n ){

    int type = -1 ;

    for( int i = 0 ; i < n ; i++ ){

        if( isalpha( sol[ i ] ) != 0 ){
            if( type == -1 ){
                type = isupper( sol[ i ] ) ;
            }else{

                if( type != isupper( sol[ i ] ) ){
                    return 0 ;
                }
            }
        }
    }

    return 1 ;

}

int is_alternating( char *sol , int n ){
    for( int i = 0 ; i < n - 1 ; i++ ){

        if( isdigit( sol[ i ] ) != 0 && isdigit( sol[ i + 1 ] ) != 0 ){
            return 0 ;
        }

        if( isalpha( sol[ i ] ) != 0 && isalpha( sol[ i + 1 ] ) != 0 ){
            return 0 ;
        }

    }
    return 1 ;
}

void print_sol( char *sol , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%c " , sol[ i ] ) ;
    }
    printf( "\n" ) ;
    return ;
}

void mult_principle( set_t *superset , int n , int depth , char *sol , FILE *ptr_o ){

    if( depth >= n ){
        if( is_alternating( sol , n ) == 1 && is_consistend( sol , n ) == 1   ){
            print_sol( sol , n ) ;
            fprintf( ptr_o , "%s\n" , sol ) ;
        } 

        
        return ;
    }

    for( int i = 0 ; i < superset[ depth ].size ; i++ ){
        sol[ depth ] = superset[ depth ].str[ i ] ;
        mult_principle( superset , n , depth + 1 , sol , ptr_o ) ;
    
    }

}

void acronym ( char *nameI , char *nameO ){


    FILE *ptr_o = fopen( nameO , "w" ) ;
    int n = 0 ;
    set_t *superset = read_file( nameI , &n ) ;
    char *sol = ( char * ) calloc( n , sizeof( char ) ) ;

    mult_principle( superset , n , 0 , sol , ptr_o ) ;
    free( sol ) ;
    free( superset ) ;
    fclose( ptr_o ) ;
    return ;

}

void main( int argc , char **argv ){

    acronym( argv[ 1 ] ,  argv[ 2 ] ) ;

}
