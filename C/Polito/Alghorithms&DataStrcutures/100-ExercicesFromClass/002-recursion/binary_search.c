#include <stdio.h>

#define ARRAY_SIZE 8


int binary_search( int[ ] , int , int , int ) ;


void main( ){

int arr[ ARRAY_SIZE ] ;
int key ;
int found_index ; 

for( int i = 0 ; i < ARRAY_SIZE ; i++ ){
    printf( "Insert the array in a sorted fashion: \n" ) ;
    scanf( "%d" , &arr[ i ] ) ;
}

printf( "Insert the key to search for: " ) ;
scanf( "%d" , &key ) ;

found_index = binary_search( arr , key , 0 , ARRAY_SIZE - 1 ) ;

if( found_index == -1 ){
    printf( "Item not found! \n" );
}else{
    printf( "Number %d found at index %d" , arr[ found_index ] , found_index ) ;
}

}


int binary_search( int arr[ ] , int key , int l , int r ){

    int c ;

    if( l > r ){
        return -1 ;
    }

    c = ( l + r ) / 2 ;
    if( key < arr[ c ] ){
        return binary_search( arr , key , l , c - 1  ) ;
    }
    
    if( key > arr[ c ] ) {
        return binary_search( arr , key , c + 1 , r ) ;
    }

    return c ;


}
