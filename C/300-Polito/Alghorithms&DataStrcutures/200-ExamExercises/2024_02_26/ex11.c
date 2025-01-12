#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>


char *merge_string( char *s1 , char *s2 ){


    char *output = ( char * ) malloc( ( strlen( s1) + strlen( s2 ) + 2 ) *sizeof( char ) ) ;

    int i = 0 ;
    int k = 0 ;
    int j = 0 ;

    while( i < strlen( s1 ) - 1 ){
        if( s1[ i ] > s1[ i + 1 ] ){
            printf( "S1 is not sorted because of characters %c %c!\n" , s1[ i ] , s1[ i + 1 ] ) ;
            return NULL ;
        }
        i++;
    }

    i = 0 ;
    while( i < strlen( s2 ) - 1 ){
        if( s2[ i ] > s2[ i + 1 ] ){
            printf( "S2is not sorted because of characters %c %c!\n" , s2[ i ] , s2[ i + 1 ] ) ;
            return NULL ;
        }
        i++;
    }

    i = 0 ;
    while( k < strlen( s1 ) && k < strlen( s2 ) ){
        if( s1[ i ] <= s2[ j ] ){
            output[ k++ ] = s1[ i++ ] ;
        }else{
            output[ k++ ] = s2[ j++ ] ;
        }
    }
    while( i < strlen( s1 ) ){
        output[ k++ ] = s1[ i++ ] ;
    }

    while( j < strlen( s2 ) ){
        output[ k++ ] = s2[ j++ ] ;
    }
    return output ;
}

void main( int argc , char **argv ){

    char *s1 = "abcdxyz" ;
    char *s2 = "abcdefgh" ;

    char *s3 = merge_string( s1 , s2  );

    printf( "The merged string is: %s \n" , s3 ) ;




}

