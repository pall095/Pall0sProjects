#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>


void print_square( int** , int ) ;
void shuffle_matrix( int** , int ) ;
int** allocate_matrix( int ) ;
int* generate_marker( int ) ;

void create_magical( int** , int* , int , int , int ) ;
int sum_row( int** , int , int ) ;
int sum_column( int** , int , int ) ; 
int is_magic( int** , int ) ;

void main( int argc , char **argv ){


    int n = atoi( argv[ 1 ] ) ;
    int **square = allocate_matrix( n ) ;
    int max = n * n ;
    int *marker = generate_marker( n ) ;

    create_magical( square , marker , 0 , 0 , n ) ;
    print_square( square , n ) ;
    if( is_magic( square , n ) == 1 ){
        printf( "Square is magical!\n" ) ;
    }else{
        printf( "Square is not magical! \n " ) ;
    }


}

void create_magical( int **square , int *marker , int row , int col , int n ){

    if( is_magic( square , n ) == 1 ){
        return ;
    }

    for( int i = 1 ; i <= ( n * n )  && is_magic( square , n ) == 0 ; i++ ){
        if( marker[ i ] == 0 ){
            square[ row ][ col ] = i ;
            marker[ i ] = 1 ;
            if( col == ( n - 1 ) ){
                create_magical( square , marker , row + 1 , 0 , n ) ;
            }else{
                create_magical( square , marker , row , col + 1 , n ) ;
            }
            
            if( is_magic( square , n ) == 0 ){
                marker[ i ] = 0 ;
                square[ row ][ col ] = 0 ;
            }else{
                return ;
            }

        }
    }
}


int* generate_marker( int n ){
    int *marker = ( int *) malloc( n * n * sizeof( int ) ) ;
    if( marker == NULL ){
        printf( "Unable to allocate memory for marker array!\n" ) ;
        return NULL ;
    }
    for( int i = 0 ; i <= n * n ; i++ ){
        marker[ i ] = 0 ;
    }
    return marker ;
}

int is_magic( int **matrix , int n ){

    int sum = sum_row( matrix , n , 0 ) ;
    for( int i = 1 ; i < n ; i++ ){
        if( sum_row( matrix , n , i ) != sum ){
            return 0 ;
        }
    }
    for( int j = 0 ; j < n ; j++ ){
        if( sum_column( matrix , n , j ) != sum ){
            return 0 ;
        }
    }

    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < n ; j++){
            if( matrix[ i ][ j ] == 0 ){
                return 0 ;
            }
        }
    }

    return 1 ;

}


int sum_row( int **matrix , int n , int row ){
    int sum = 0 ; 
    for( int j = 0 ; j < n ; j++ ){
        sum = sum + matrix[ row ][ j ] ;
    }
    return sum ;
}

int sum_column( int **matrix , int n , int column ){
    int sum = 0 ; 
    for( int i = 0 ; i < n ; i++ ){
        sum = sum + matrix[ i ][ column ] ;
    }
    return sum ;
}

void print_square( int **square , int n ){

    for( int i = 0 ; i < n ; i ++ ){
        for( int j = 0 ; j < n ; j++ ){
            printf( "%d " , square[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
}

void shuffle_matrix( int **matrix , int n ){
    for( int i = 0 ; i < n ; i ++){
        for( int j = 0 ; j < n ; j++ ){
            matrix[ i ][ j ] = i + j ;
        }
    }
    return ;
}

int** allocate_matrix( int n ){
    int **square ;
    square = ( int** ) malloc( n * sizeof( int* ) ) ;

    for( int i = 0 ; i < n ; i++ ){
        square[ i ] = ( int * ) malloc( n * sizeof( int ) ) ;
    }
    return square ;
} 