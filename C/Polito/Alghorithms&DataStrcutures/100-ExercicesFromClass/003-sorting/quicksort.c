#include <stdio.h>
#include <stdlib.h> 
#include <string.h>


#define ARRAY_SIZE 10

void print_array( int* ) ;
void quick_sort( int * , int ,  int ) ;
int partition( int* , int , int ) ;
void swap_elements( int* , int , int ) ;


void main( int argc , char **argv ){
    int arr[  ARRAY_SIZE ] = { 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0 } ;
    print_array( arr ) ;
    quick_sort( arr , 0 , 9 ) ;
    print_array( arr ) ;
    return ; 
}


void print_array( int* arr ){

    for( int i = 0 ; i < ARRAY_SIZE ; i++ ){
        printf("%d" , arr[ i ] ) ;
    }

    printf( "\n" ) ;
    return ;
}

void quick_sort( int* arr , int l , int r ){

    if( l >= r ){
        return ;
    }
    int c = partition( arr , l , r );
    quick_sort( arr , l , c - 1 ) ;
    quick_sort( arr , c + 1 , r ) ;
    return ;

}

int partition( int* arr , int l , int r ){

    int i = l - 1 ;
    int j = r ;
    int pivot = arr[ r ] ;

    while( i < j ){

        while( arr[ ++i ] < pivot ) ;
        while( j > l && arr[ --j ] >= pivot ) ;
        if( i < j ){
            swap_elements( arr , i , j ) ;
        } 
    }
    swap_elements( arr , i , r ) ;
    return i ; 

} 

void swap_elements( int* arr , int i , int j ){

    printf( "Swapping %d with %d \n" , arr[ i ] , arr[ j ] ) ;
    int tmp = arr[ i ] ;
    arr[ i ] = arr[ j ] ;
    arr[ j ] = tmp ;

    return ;
}