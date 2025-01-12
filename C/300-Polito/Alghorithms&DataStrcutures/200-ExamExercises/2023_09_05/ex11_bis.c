#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int common_substring( char *s1 , char *s2 ){

    int max = INT_MIN ;
    int max_s = 0 ;
    int ii , jj ;

    for( int i = 0 ; i < strlen( s1 ) ; i++ ){

        for( int j = 0 ; j < strlen( s2 ) ; j++ ){

            if( s1[ i ] == s2[ j ] ){

                ii = i ;
                jj = j ;

                while( s1[ ii ] == s2[ jj ] ){
                    ii++ ;
                    jj++ ;
                }

                if( ii - i > max ){
                    max_s = i ;
                    max = ii - i ;
                }

            }

        }

    }

    for( int i = max_s ; i < max_s + max ; i++ ){
        printf( "%c" , s1[ i ] ) ;
    }
    printf( "\n" ) ;

    return max ;

}

void main( ){

    char *s1 = "123ABCD34EFG" ;
    char *s2 = "XXXABCE124YABCD" ;
    printf( "Len %d\n" , common_substring( s1 , s2 ) ) ;

}