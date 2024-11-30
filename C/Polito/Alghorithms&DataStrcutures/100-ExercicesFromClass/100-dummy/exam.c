#include "setPrivate.h"

#define NUM_SETS 3

int mult_principle( set_t* , char* , int , int , int );
void print_sol( char* , int , char ) ;
int theoretical_count( set_t* , int ) ;

int main( int arc , char **argv ){

    int count ;
    set_t chars = set_from_file( argv[ 1 ] ) ;
    set_t chars_upper = set_from_file( argv[ 2] ) ;
    set_t nums = set_from_file( argv[ 3 ] ) ;
    set_t *vals = ( set_t* ) malloc( NUM_SETS * sizeof( set_t ) ) ;

    vals[ 0 ] = chars ;
    vals[ 1 ] = chars_upper ;
    vals[ 2 ] = nums ;

    char *sol = ( char* ) malloc( NUM_SETS * sizeof( char ) ) ;
    count = mult_principle( vals , sol , NUM_SETS , 0 , 0 ) ;
    printf( "Number of found combinations: %d\n" , count ) ;
    printf( "Number of theoretical combinations: %d\n" , 2*theoretical_count( vals , NUM_SETS ) ) ;

}

int mult_principle( set_t *vals , char *sol , int N , int depth  , int count ){

    if( depth >= N ){
        print_sol( sol , N , '-' );
        print_sol( sol , N , '+' );
        return count + 2 ;
    }

    for( int i = 0 ; i < vals[ depth ].num_choiches ; i++ ){
        sol[ depth ] = vals[ depth ].choiches[ i ] ;
        count = mult_principle( vals , sol , N , depth + 1 , count ) ;
    }

    return count ;

} 

void print_sol( char *sol , int N , char mirror ){

    for( int i = 0 ; i < N ; i++ ){
        printf( "%c" , sol[ i ] ) ;
    }
    printf( "%c" , mirror ) ;
    for( int i = N - 1  ; i >= 0 ; i-- ){
        printf( "%c" , sol[ i ] ) ;
    }
    printf( "\n" ) ;

}

int theoretical_count( set_t *vals , int N ){

    int count = 1 ;
    for( int i = 0 ; i < N ; i++ ){
        count = count*vals[ i ].num_choiches ;
    }

    return count ; 

}