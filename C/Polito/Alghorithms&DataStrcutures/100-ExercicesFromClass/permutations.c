#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


int* read_set( char* , int* ) ;
void print_set( int* , int ) ;
void simple_permutations( int* , int , int , int ) ;
void repetition_permutations( int* , int , int , int ) ;
int simple_permutations_r( int* , int* , int* , int , int , int , int , int ) ;
int repetition_permutations_r( int* , int* , int , int , int , int , int ) ;
void print_solution( int* , int ) ;
int fact( int ) ;


void main( int argc , char **argv ){


    int n = 0  ;
    int *set = read_set( argv[ 1 ] , &n ) ; 
    simple_permutations( set , n , atoi( argv[ 2 ] ) , atoi( argv[ 3 ] ) ) ;
    repetition_permutations( set , n , atoi( argv[ 2 ] ) , atoi( argv[ 3 ] ) ) ;


}

void print_set( int *set , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "Item %d: %d\n" , i , set[ i ] ) ;
    }

}

void repetition_permutations( int *set , int n , int k , int verbose ){

    // Allocate solution array.
    int *sol = ( int *) malloc( n * sizeof( int ) ) ;
    if( sol == NULL ){
        printf( "Unable to allocate sol array\n" ) ;
        exit( EXIT_FAILURE ) ;
    } 

    int depth = 0 ;
    int count = 0 ;
    count = repetition_permutations_r( set , sol , n , k , depth , count , verbose) ;
    
    printf( "Counte number of repetition permutations : %d\n" , count ) ;
    printf( "Theorical number of repetition permutations: %d\n" ,  (int)pow( n , k ) ) ;

}

void simple_permutations( int* set , int n , int k , int verbose ){

    // Allocate and initalize marker.
    int *marker = ( int * ) malloc( n *sizeof( int ) ) ;
    if( marker == NULL ){
        printf( "Unable to allocate marker array!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }
    for( int i = 0 ; i < n ; i++ ){
        marker[ i ] = 0 ;
    }

    // Allocate solution array.
    int *sol = ( int *) malloc( n * sizeof( int ) ) ;
    if( sol == NULL ){
        printf( "Unable to allocate sol array\n" ) ;
        exit( EXIT_FAILURE ) ;
    } 

    int depth = 0 ;
    int count = 0 ;
    count = simple_permutations_r( set , marker , sol , n , k , depth , count , verbose ) ;
    
    printf( "Counte number of simple permutations : %d\n" , count ) ;
    printf( "Theorical number of simple permutations: %d\n" ,  fact( n )/( fact( n - k ) ) ) ;

} 


int simple_permutations_r( int *set , int *marker , int *sol , int n , int k , int depth , int count , int verbose ){

    if( depth >= k ){
        if( verbose == 1 ){
            print_solution( sol , k ) ;
        }
        return count + 1 ;
    }


    for( int j = 0 ; j < n ; j++ ){
        if( marker[ j ] == 0 ){
            sol[ depth ] = set[ j ] ;
            marker[ j ] = 1 ;
            count = simple_permutations_r( set , marker , sol , n , k , depth + 1 , count , verbose ) ;
            marker[ j ] = 0 ;
        }
    }
    return count ;
}

int repetition_permutations_r( int *set , int *sol , int n , int k , int depth , int count , int verbose ){

    if( depth >= k ){
        if( verbose == 1 ){
            print_solution( sol , k ) ;
        }
        return count + 1 ;
    }


    for( int j = 0 ; j < n ; j++ ){
        sol[ depth ] = set[ j ] ;
        count = repetition_permutations_r( set , sol , n , k , depth + 1 , count , verbose ) ;
    }
    return count ;
}


int* read_set( char *filename , int *n ){

    FILE *ptr = fopen( filename , "r" ) ;
    int buffer ;
    int i = 0 ;
    
    if( ptr == NULL ){
        printf( "Unable to open the file!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }

    while( fscanf( ptr , "%d" , &buffer ) != EOF ){
        *n = *n + 1 ;
    }

    fclose( ptr ) ;

    int *set = ( int * ) malloc( *n * sizeof( int ) ) ;
    ptr = fopen( filename , "r" ) ;

    while( fscanf( ptr , "%d" , &set[ i ] ) != EOF ){
        i++ ;
    } 
    fclose( ptr ) ;
    return set;
}

int fact( int num ){

    if( num == 0 ){
        return 1 ;
    }
    return num * fact( num - 1 ) ;
}

void print_solution( int *sol , int k ){
    for( int i = 0 ; i < k ; i++ ){
        printf( "%d " , sol[ i ] ) ;
    }
    printf( "\n" ) ;
}
