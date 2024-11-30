#include<stdio.h>
#include<stdlib.h>


void invert_string( char* , char* ) ;

void main( int argc , char *argv ){

    char *s1 ;
    char *s2 ; ;

    invert_string( s1 , s2 ) ;

}

void invert_string( char *s1 , char *s2 ){

    int len ;
    char c ;
    printf( "Input string length: " ) ; 
    scanf( "%d" , &len ) ;

    s1 = ( char * ) malloc( len *sizeof( char ) ) ;
    s2 = ( char * ) malloc( len * sizeof( char ) ) ;

    for( int i = 0 ; i < len ; i++ ){
        printf( "Insert the next char: \n" ) ;   
        scanf( "%c\n" , &c ) ;

        if( c == '\n' ){
            i = i-1 ;
        }else{
            s1[ i ] = c ;
        }
    }

    for( int k = 0 ; k < len ; k++ ){
        printf( "%c " , s1[ k ] ) ;
    }

    printf( "\n" ) ;
    int i = 0 ;
    int j ;
    while( i < len ){

        for( j = i + 1 ; j < len ; j++ ){

            if( s1[ j ] <= s1[ i ] ){
                printf( "Found a substring starting from %d and ending %d\n" , i , j - 1  );
                i = j ;
                break ;
            }else{
                i++ ;
            }
        }

        if( j == len ){
            break ;
        }
    }

    for( int k = 0 ; k < len ; k++ ){
        printf( "%c " , s2[ k ] ) ;
    }



}