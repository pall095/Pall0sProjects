#include<stdio.h>
#include<stdlib.h>


void invert_string( char* , char** , int ) ;

void main( int argc , char *argv ){

    int len ;

    printf( "Input string length: " ) ; 
    scanf( "%d" , &len ) ;

    char *s1 = ( char *) malloc( len *sizeof( char ) ) ;
    char *s2 ;

    invert_string( s1 , &s2 , len ) ;

    for( int i = 0 ; i < len ; i++ ){
        printf( "%c " , s2[ i ] ) ;
    }


}

void invert_string( char *s1 , char **s2 , int len ){
    char c ;


    char *s3 = ( char *) malloc( len *sizeof( char ) ) ;

    for( int i = 0 ; i < len ; i++ ){
        printf( "Insert the next char: \n" ) ;   
        scanf( " %c" , &c ) ;
        s1[ i ] = c ;
    }

    for( int k = 0 ; k < len ; k++ ){
        printf( "%c " , s1[ k ] ) ;
    }
    printf( "\n" ) ;


    int start = 0 ;
    int i = 1 ;
    int j = 0 ;

    while( start < len ){

        while( s1[ i - 1 ] < s1[ i ] && i < len ){
            i++ ;
        }

        for( int k = i - 1 ; k >= start ; k-- ){
            s3[ j++ ] = s1[ k ] ; 
        }

        start = i ;
        i = i + 1 ;


    }

    *s2 = s3 ;
    
}