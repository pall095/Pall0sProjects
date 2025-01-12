#include "listPublic.h"



void main( int argc , char **argv ){


    char name[ MAX_STR ] ;
    char surname[ MAX_STR ] ;
    list_t *head = NULL ;
    int s ;
    

    while( 1 ){

        printf( "Insert a name and surname: \n" ) ;
        scanf( "%s %s" , name , surname ) ;
        head = order_insert( head , name , surname ) ;
        print_list( head ) ;
    
    }

}