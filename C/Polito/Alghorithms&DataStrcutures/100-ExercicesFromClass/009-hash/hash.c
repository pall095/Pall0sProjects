#include<stdio.h>
#include<stdlib.h>


#define M 23 
#define INIT -1 


int* init_hash( int size ){
    int *hash = ( int * ) malloc( size * sizeof( int ) ) ;
    if( hash == NULL ){
        printf( "Unable to allocate memory for hash table!\n" ) ;
        return NULL ;
    }
    for( int i = 0 ; i < size ; i++ ){
        hash[ i ] = INIT ;
    }
    return hash ;
}

void display_hash( int *hash , int size ){
    for( int i = 0 ; i < size ; i++ ){
        printf( "%d " , i ) ;
    }

    printf( "\n" ) ;

    for( int i = 0 ; i < size ; i++ ){
        printf( "%d " , hash[ i ] ) ;
    }    
    printf( "\n" ) ;
}

int* insert( int *hash , int size , int new ){

    int j = 1 ; 
    int i = new % size ;

    if( hash[ i ] == INIT ){
        printf( "Hash value is %d\n" , i ) ;
        hash[ i ] = new ;
        return hash ;
    }

    while( j < size ){

        j = ( i + j * ( 1 + new % 97 ) ) % M ;

        if( hash[ j ] == INIT ){
            printf( "Hash value is %d\n" , j ) ;
            hash[ j ] = new ;
            return hash ;

        }else{
           j++ ; 
        }
    }
}

void main( int argc , char **argv ){


    int *hash_map = init_hash( M ) ;
    display_hash( hash_map , M ) ;
    int current ;


    while( 1 ){
        printf( "Which value you want to put in the hash table: \n" ) ;
        scanf( "%d" , &current ) ;
        hash_map = insert( hash_map , M , current ) ;
        display_hash( hash_map , M ) ; 
    }







}