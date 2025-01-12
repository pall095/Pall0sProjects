#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int countSpaces( char* ) ;



void main( int argc , char **argv ){

    char word[ ] = "This is a string with spaces    !" ;
    int num_white = countSpaces( word ) ;

    printf( "Number of spaces is: %d \n" , num_white ) ;

}

int countSpaces( char *word ){

    if( *word == '\0' ){
        return 0 ;
    }

    return( (isspace( *word ) ? 1 : 0) + countSpaces( word + 1 ) ) ;


}