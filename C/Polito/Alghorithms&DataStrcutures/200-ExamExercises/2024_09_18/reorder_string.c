#include<stdio.h>
#include<stdlib.h>
#include<string.h>




char* reoder_string( char *s1 , int *v ){

    int len = strlen( s1  );
    char *s2 = ( char * ) malloc( ( len + 1) * sizeof( char ) ) ;
    
    for( int i = 0 ; i < len ; i++ ){
        if( v[ i ] >= len || v[ i ] < 0 ){
            printf( "Invalid array V\n" ) ;
            return NULL ;
        }
    }

    for( int j = 0 ; j < len ; j++ ){
        
        s2[ v[ j ] ] = s1[ j ] ;
    }

    return s2 ;

}

void main( ){

    char *s1 = "abcdefgh" ;
    int v[] = { 7 , 4 , 3 , 0 , 1 , 2 , 5 , 6 } ;

    char *s2 = reoder_string( s1 , v ) ; 

    printf( "%s" , s2  ) ;
}