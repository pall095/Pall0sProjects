#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE 10

void merge_standalone( int* , int* , int* , int ) ;
void merge_r( int* , int* , int , int , int ) ;
void print_array( int* , int ) ;
void merge_sort( int* , int ) ;
void merge_sort_rec( int* , int* , int , int ) ;

void main( int argc , char **argv ){

    int arr1[ ] = { 1000 , 10 , 20 , 30 , 40 , 138 , 60 , 80 , 90 , 100 } ;
    merge_sort( arr1 , ARRAY_SIZE ) ;
 


}

void print_array( int *arr , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%d - " , arr[ i ] ) ;
    }
    printf( "\n" ) ;
    return ;
}



void merge_sort( int* arr , int n ){
    printf( "Before sorting: \n" ) ;
    print_array( arr , n ) ;
    int *arr_tmp = ( int * ) malloc( n * sizeof( int ) ) ;
    merge_sort_rec( arr , arr_tmp , 0 , n - 1  ) ;
    printf( "After sorting: \n" ) ;
    print_array( arr , n ) ;
    return ;

}

void merge_sort_rec( int *arr , int *arr_tmp , int l , int r ){

    if( l >= r ){
        return ;
    }

    int c = ( l + r ) / 2 ;
    merge_sort_rec( arr , arr_tmp , l , c );
    merge_sort_rec( arr , arr_tmp , c + 1 , r ) ;
    merge_r( arr , arr_tmp , l , c , r ) ;
    return ;

}

void merge_r( int *v , int *v_tmp , int l , int c , int r ){

    int i = l ;
    int k = l ; 
    int j = c + 1 ;

    while( i <= c && j <= r ){

        if( v[ i ] <= v[ j ] ){
            v_tmp[ k++ ] = v[ i++ ] ;
        }else{
            v_tmp[ k++ ] = v[ j++ ] ;
        }
    }

    while( i <= c ){
        v_tmp[ k++ ] = v[ i++ ];
    }

    while( j <= r ){
        v_tmp[ k++ ] = v[ j++ ] ;
    }

    for( i = l ; i <= r ; i++ ){
        v[ i ] = v_tmp[ i ] ;
    }

    return ;

}

void merge_standalone( int *v1 , int *v2 , int *v3 , int n ){

    int i = 0 ;
    int j = 0 ;
    int k = 0 ;
    
    while( i < n && j < n ){
        if( v1[ i ] < v2[ j ] ){
            v3[ k++ ] = v1[ i++ ] ;
        }else{
            v3[ k++ ] = v2[ j++ ] ;
        }
    }

    while( i < n ){
        v3[ k++ ] = v1[ i++ ] ;
    }

    while( j < n ){
        v3[ k++ ] = v2[ j++ ] ;
    }

    return ;
}