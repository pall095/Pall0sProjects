#include<stdio.h>
#include<stdio.h>
#include<string.h>

#define MAX_CHAR 21


void lcp( char **string , int n){
    
    char prefix[ MAX_CHAR ] ;
    int k = 0 ;
    int min_len = 1000 ;
    char curr_char ;
// Finds the shortest string (prefix cannot be longer than that
    for( int i = 0 ; i < n ; i++ )
        if( strlen( string[ i ] ) < min_len ){
            min_len = strlen( string[ i ] ) ;
    }
    for( int i = 0 ; i < min_len ; i++ ){
        curr_char = string[ 0 ][ i ] ;
        for( int j = 1 ; j < n ; i++ ){
            if( string[ j ][ i ] != curr_char ){
                break ;
            }
        }
            prefix[ k ] = curr_char ;
        k++ ;
    }
    prefix[ k ] = '\0' ;
    printf( "The longest prefix is: %s\n" , prefix ) ;
}


int main() {
char *string[] = {"fooo", "fooo", "fooo"};
int n = 3;
lcp(string, n);
return 0;
}
