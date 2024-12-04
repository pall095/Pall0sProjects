#include<stdio.h>
#include<stdlib.h>

#define ARRAY_SIZE 10 


//generic functions
void print_array( int* , int ) ;
void print_partial_array( int* , int , int ) ;

//merge sort
void merge_sort( int* , int ) ;
void merge_sort_r( int* , int* , int , int ) ;
void merge( int* , int* , int , int , int  ) ; 

// quicksort
void quick_sort( int* , int ) ;
void quick_sort_r( int* , int , int ) ;
int partition( int* , int , int ) ;
void swap( int* , int , int ) ;

void main( int argc , char **argv ){


    int arr[ ] = { 13 , 5 , 8 , 11 , 12 , 0 , 1 , 7 , 2 , 3} ;
    //merge_sort( arr , ARRAY_SIZE ) ;
    quick_sort( arr , ARRAY_SIZE ) ;
    print_array( arr , ARRAY_SIZE ) ;



}

// Quicksort
void quick_sort( int *arr , int N ){
    quick_sort_r( arr , 0 , N - 1 ) ;
}

void quick_sort_r( int *arr , int l , int r ){

    if( l >= r ){
        return ;
    }
    
    printf( "Pivot is: %d \n" , arr[ r ] ) ;
    int c = partition( arr , l , r ) ;
    print_partial_array( arr , l , c - 1 ) ;
    print_partial_array( arr , c + 1 , r ) ;
    quick_sort_r( arr , l , c - 1 ) ;
    
    quick_sort_r( arr , c + 1 , r  );
    

}

int partition( int *arr , int l , int r ){

    int pivot = arr[ r ] ;
    int i = l - 1 ;
    int j = r ;

    while(  i < j ){
        while( arr[ ++i ] < pivot ) ;
        while( j > l && arr[ --j ] >= pivot ) ;
        if( i < j ){
            swap( arr , i , j ) ;
        }
    }
    swap( arr , i ,  r ) ;
    return i ;

}

void swap( int *arr , int i , int j ){
    int tmp = arr[ j ] ;
    arr[ j ] = arr[ i ] ;
    arr[ i ] = tmp ;
    return ;
}


// Merge sort
void merge_sort( int *arr , int N ){
    int *sup = ( int * ) malloc( N * sizeof( int ) ) ;
    if( sup == NULL ){
        printf( "Unable to allocate memory for support array!\n") ;
        return ;
    }
    merge_sort_r( arr , sup , 0 , ARRAY_SIZE - 1 ) ;
}


void merge_sort_r( int *arr , int *sup , int l , int r ){
    if( l >= r ){
        return ;
    }
    int c = ( l + r ) / 2 ;
    merge_sort_r( arr , sup , l , c ) ;
    merge_sort_r( arr , sup , c + 1 , r  ) ;
    print_partial_array( arr , l , c ) ;
    print_partial_array( arr , c + 1 , r ) ;
    merge( arr , sup , l , c , r ) ;
}

void merge( int *arr , int *sup , int l , int c , int r ){
    int i = l ;
    int j = c + 1 ;
    int k = l ;
    while( i <= c && j <= r ){
        if( arr[ i ] <= arr[ j ] ){
            sup[ k++ ] = arr[ i++ ] ;
        }else{
            sup[ k++ ] = arr[ j++ ] ;
        }
    }
    while( i <= c ){
        sup[ k++ ] = arr[ i++ ] ;
    }
    while( j <= r ){
        sup[ k++ ] = arr[ j++ ] ;
    }
    for( i = l ; i <= r ; i++ ){
        arr[ i ] = sup[ i ] ;
    }
}



// Generic functions.

void print_array( int *arr , int N ){

    for( int i = 0 ; i < N ; i++ ){
        printf( "%d - " , arr[ i ] ) ;
    }
    printf( "\n" ) ;
    return;
}
void print_partial_array( int *arr , int l , int r ){

    for( int i = l ; i <= r ; i++ ){
        printf( "%d - " , arr[ i ] ) ;
    }
    printf( "\n" ) ;
    return ;
}

