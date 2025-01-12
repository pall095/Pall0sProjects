#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int isPalindrome( char* , int ) ;


void main( int argc , char **argv ){

    char word[ ] = "tette" ;
    int len = 4 ;


    if( isPalindrome( word , len ) == 0 ){
        printf( "Word is not palindrome\n" ) ;
    }else{
        printf( "Word is palindrome!\n" ) ;
    }

}


int isPalindrome( char *word , int len ){

if( len <= 1 ){
    return 1 ;
}

return( *word == word[ len -1 ] && isPalindrome( word + 1 , len -2 ) ) ;

}