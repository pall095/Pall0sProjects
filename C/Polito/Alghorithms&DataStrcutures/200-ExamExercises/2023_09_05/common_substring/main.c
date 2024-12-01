#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>






int common_substring( char *s1 , char *s2 ){


    int max_len ;
    int start ;
    int cnt_max = 0 ;
    int k ;



    for( int j = 0 ; j < strlen( s2 ) ; j++ ){

        for( int i = 0 ; i < strlen( s1 ) ; i++ ){

            if( s1[ i ] == s2[ j ] ){
                k = 0 ;
                while( s1[ i + k ] == s2[ j + k ] ){
                    k++ ;
                }

                if( k > cnt_max ){
                    start = i ;
                    cnt_max = k ;
                    i = k ;
                }
            }


        }



    }


    for( int i = start ; i < start + cnt_max ; i++ ){
        printf( "%c " , s1[ i ] ) ;
    }
    printf( "\n" ) ;

    return cnt_max ;
}


void main( ){

    char s1[ ] = "123ABCD34EFG" ;
    char s2[ ] = "123ABCE124YABCD" ;

    int cnt = common_substring( s1 , s2 ) ;
    printf("The count is %d\n" , cnt ) ;





}