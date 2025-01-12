#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int* read_set( char* , int* ) ;
void print_set( int* , int ) ;
void print_solution( int* , int ) ;
int fact( int ) ;


int simple_arragements_r( int* , int* , int* , int , int , int , int ) ;
void simple_arrangements( int* , int , int ) ;

void arrangements_repetition( int* , int , int ) ;
int arrangements_repetition_r( int* , int* , int , int , int , int ) ;

void simple_combinations( int* , int , int ) ;
int simple_combinations_r( int* , int* , int , int , int , int , int ) ;

void combinations_repetition( int* , int , int ) ;
int combinations_repetition_r( int* , int* , int , int , int , int , int ) ;


void main( int argc , char **argv ){

    int N ; 
    int *set = read_set( argv[ 1 ] , &N ) ;
    simple_arrangements( set , 6 , N ) ;
    arrangements_repetition( set , 6 , N ) ;
    simple_combinations( set , 6 , N ) ;
    combinations_repetition( set , 6 , N ) ;

}

void combinations_repetition( int *set , int k , int N ){

    int *sol = ( int * ) malloc( k * sizeof( int ) ) ;
    if( sol == NULL ){
        printf( "Unable to allocate solution array!\n" ) ;
        return ;
    }

    int count = 0 ;
    int recursion = 0 ;
    int start = 0 ;
    count = combinations_repetition_r( set , sol , start , count , k , N , recursion ) ; 
    printf( "Number of combinations with repetition is : %d\n" , count ) ;
    // printf( "Number of theoretical combination with repetition is : %f\n" , th_comb ); --> comes out too big

}

int combinations_repetition_r( int *set , int *sol , int start , int count , int k , int N , int recursion ){

    if( recursion >= k ){
        //print_solution( sol , k ) ;
        return count + 1 ; 
    }

    for( int i = start ; i < N ; i++ ){
        sol[ recursion ] = set[ i ];
        count = combinations_repetition_r( set , sol , i , count , k , N , recursion + 1 ) ;
    }

    return count ;

}


void simple_combinations( int *set , int k , int N ){

    int *sol = ( int * ) malloc( k * sizeof( int ) ) ;
    if( sol == NULL ){
        printf( "Unable to allocate solution array!\n" ) ;
        return ;
    }

    int count = 0 ;
    int recursion = 0 ;
    int start = 0 ;
    count = simple_combinations_r( set , sol , start , count , k , N , recursion ) ; 
    printf( "Number of combinations without repetition is : %d\n" , count ) ;
    printf( "Number of theoretical combination withouth repetition is : %d\n" , fact( N )/( fact( k ) * fact( N -  k ) ) );

}

int simple_combinations_r( int *set , int *sol , int start , int count , int k , int N , int recursion ){

    if( recursion >= k ){
        //print_solution( sol , k ) ;
        return count + 1 ; 
    }

    for( int i = start ; i < N ; i++ ){
        sol[ recursion ] = set[ i ];
        count = simple_combinations_r( set , sol , i + 1 , count , k , N , recursion + 1 ) ;
    }

    return count ;

}

void arrangements_repetition( int *set , int k , int N ){
    
    int *sol = ( int * ) malloc( k * sizeof( int ) ) ;
    if( sol == NULL ){
        printf( "Unable to allocate solution array!\n" ) ;
        return ;
    }

    int count = 0 ;
    int recursion = 0 ;

    count = arrangements_repetition_r( set , sol , count , k , N , recursion ) ;
    
    if( k < N ){
        printf( "Number of arrangements with repetition is : %d\n" , count ) ;
        printf( "Number of theoretical arrangements with repetition : %d\n" ,  (int)pow( N , k ) ) ;
        return ;
    }

    if( k == N ){
        printf( "Number of permutations with repetition is : %d\n" , count ) ;
        printf( "Number of permutations arrangements with repetition : %d\n" ,  (int)pow( N , k ) ) ;
        return ; 
    }
}

int arrangements_repetition_r( int *set , int *sol  , int count , int k , int N , int recursion  ){
    if( recursion >= k ){
        //print_solution( sol , k ) ;
        return count + 1; 
    }
    for( int i = 0 ; i < N ; i++ ){

        sol[ recursion ] = set[ i ] ;
        count = arrangements_repetition_r( set , sol , count , k , N , recursion + 1 ) ;
        
    }
    return count ;
}

void simple_arrangements( int *set , int k , int N ){
    int *mark = ( int * ) malloc( N * sizeof( int) ) ;

    if( mark == NULL ){
        printf( "Unable to allocate marker array!\n" ) ;
        return ;
    }

    for( int i = 0 ; i < N ; i++ ){
        mark[ i ] = 0 ;
    }

    int *sol = ( int * ) malloc( k * sizeof( int ) ) ;
    if( sol == NULL ){
        printf( "Unable to allocate solution array!\n" ) ;
        return ;
    }

    int count = 0 ;
    int recursion = 0 ;

    count = simple_arragements_r( set , sol , mark , count , k , N , recursion ) ;
    if( k < N ){
        printf( "Number of simple arrangements without repetition is : %d\n" , count ) ;
        printf( "Number of theoretical simple arrangements without repetition is : %d\n" ,  fact( N )/fact( N - k ) ) ;
        return ;
    }

    if( k == N ){
        printf( "Number of permutations without repetition is: %d\n" , count ) ;
        printf( "Number of permutations arrangements without repetition is : %d\n" ,  fact( N )/fact( N - k ) ) ;
        return ; 
    }
}



int simple_arragements_r( int *set , int *sol , int *mark , int count , int k , int N , int recursion  ){
    if( recursion >= k ){
        //print_solution( sol , k ) ;
        return count + 1; 
    }
    for( int i = 0 ; i < N ; i++ ){
        if( mark[ i ] == 0 ){
            mark[ i ] = 1 ;
            sol[ recursion ] = set[ i ] ;
            count = simple_arragements_r( set , sol , mark , count , k , N , recursion + 1 ) ;
            mark[ i ] =  0;
        }
    }
    return count ;
}


// Auxiliary functions.

void print_solution( int *sol , int k ){
    for( int i = 0 ; i < k ; i++ ){
        printf( "%d " , sol[ i ] ) ;
    }
    printf( "\n" ) ;
}


void print_set( int *set , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "Item %d: %d\n" , i , set[ i ] ) ;
    }

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