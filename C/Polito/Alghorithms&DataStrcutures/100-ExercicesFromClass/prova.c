#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void do_something( char **s ){

    printf( "%c" , *(*( s )) ) ;

} 

void main( int argc , char **argv ){


    char *s ="This is a string" ;
    do_something( &s ) ;



}