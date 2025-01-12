#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>


char* reorder_string( char *s1 , int *v ){

    char *output = ( char * ) malloc( ( strlen( s1 )  + 1 ) * sizeof( char )  );

    for( int i = 0 ; i < strlen( s1 ) ; i++ ){
        if( v[ i ] >= strlen( s1 ) ){
            printf( "Array has invalid values!\n" ) ;
            return NULL ;
        }
    }

    for( int i = 0 ; i < strlen( s1 ) ; i++ ){
        output[ v[ i ] ] = s1[ i ] ;        
 
    }

    return output ;

}



void main( int argc , char **argv ){
    char *s1 = "abcdefgh" ;
    int v[] = { 7, 4, 3, 0, 1, 2, 5, 6 } ;
    char *s2 = reorder_string( s1 , v ) ;
    printf( "The output string: %s \n" , s2 ) ;

}