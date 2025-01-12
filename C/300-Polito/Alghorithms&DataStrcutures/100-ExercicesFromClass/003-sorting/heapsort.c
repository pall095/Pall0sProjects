#include<stdio.h>
#include<stdlib.h>


#define LEFT( i ) ( 2*i + 1 )
#define RIGHT( i ) ( 2*i + 2 )
#define PARENT( i ) ( ( int )( i - 1 ) / 2  ) 

#define SIZE 9

int* swap( int *arr , int i , int j ){
    int tmp = arr[ i ] ;
    arr[ i ] = arr[ j ] ;
    arr[ j ] = tmp ;
    return arr ;
}


void print_arr( int *arr , int size ){
    for( int i = 0 ; i < size ; i++ ){
        printf( "%d " , arr[ i ] ) ;
    }
    printf( "\n" ) ;
}

int* heapify( int *arr , int i , int size ){

    int l = LEFT( i ) ;
    int r = RIGHT( i ) ;
    int largest ;

    if(  l < size && arr[ i ] < arr[ l ] ){
        largest = l ;
    }else{
        largest = i ;
    }

    if( r < size && arr[ largest ] < arr[ r ] ){
        largest = r ;
    }

    if( largest != i ){
        arr = swap( arr , i , largest ) ;
        arr = heapify( arr , largest , size ) ;
    }
    return arr ;

}

int* build_heap( int *arr , int size ){
    
    for( int i = ( size )/2 - 1 ; i >= 0 ; i-- ){
        arr = heapify( arr , i  , size ) ;
    }
    return arr ;
}

int* heapsort( int *arr , int size ){
    
    arr = build_heap( arr , size ) ;
    printf( "arr after build heap\n" ) ;
    print_arr( arr , size  ) ;
    while( size > 0 ){
        print_arr( arr , SIZE ) ;
        arr = swap( arr , 0 , size - 1 ) ;
        size-- ;
        arr = heapify( arr , 0 , size ) ;
    }

    return arr ;
}


void main( ){

    int arr[ ] = { 2 , 1 , 6 , 3 , 13 , 15 , 21 , 9  } ;
    int size = 8 ;

    int *arr2 = heapsort( arr , size ) ;
    print_arr( arr2 , size ) ;

}