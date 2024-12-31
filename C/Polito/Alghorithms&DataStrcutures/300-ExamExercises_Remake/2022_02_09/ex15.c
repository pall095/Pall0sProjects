#include<stdio.h>
#include<stdlib.h>
#include<string.h> 


typedef struct list_s{

    char *s ;
    struct list_s *next ;

} list_t ;


list_t* push( list_t* , list_t* ) ;
list_t* new_element( ) ;
void print_list( list_t* ) ;

list_t *new_element( char *start , int len ){

    list_t *new = ( list_t * ) malloc( sizeof( list_t ) ) ;
    new->s = ( char * ) malloc( ( len + 1 ) * sizeof( char ) ) ;

    strncpy( new->s , start , len ) ;
    new->s[ len ] = '\0' ;
    return new ;

}

list_t *push( list_t *head , list_t *new ){
    
    printf( "Pushing %s \n" , new->s ) ;
    new->next = head ;
    head = new ;
    return head ;

}


list_t *split_str( char *str ){


    char *start = str ;
    char *s = str ;
    list_t *head = NULL ;
    list_t *new ;
    int len ;

    while( *s != '\0' ){

        if( *s == '.' ){

            len = s - start ;
            new = new_element( start , len ) ;
            head = push( head , new ) ;
            start = s + 1 ;

        }

        s++ ;

    } 

    //Adding tail
    len = s - start ;
    new = new_element( start , len ) ;
    head = push( head , new ) ;


    return head ;

}

void print_list( list_t* head ){

    while( head != NULL ){
        printf( "%s -->" , head->s ) ;
        head = head->next ;
    }

}

void main( ){

    char *s = "a.bb.ccc.dddd.eeeee.ffffff" ;
    list_t *head = split_str( s ) ;
    print_list( head ) ;


}
