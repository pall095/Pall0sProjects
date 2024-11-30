#include<stdio.h>

#define ARRAY_SIZE 8 

int find_max( int[ ] , int , int ) ;

void main( ){


    int arr[ ARRAY_SIZE ] ;

    for( int i = 0 ; i < ARRAY_SIZE ; i++ ){

        printf( "Insert the next number: \n" ) ;
        scanf( "%d" , &arr[ i ] ) ;

    }

    int max = find_max( arr , 0 , ARRAY_SIZE - 1 ) ;
    printf( "The max in the array is: %d\n" , max  ) ;
}


int find_max( int arr[ ] , int l , int r ){

    int c, m1, m2;

    if( l >= r ){
        return arr[ l ] ;
    }

    c = ( l + r ) / 2 ;
    m1 = find_max( arr , l , c ) ;
    m2 = find_max( arr , c + 1 , r ) ;

    if(  m1 > m2 ){
        return m1 ;
    }else{
        return m2 ;
    }
}