#include <stdlib.h>

typedef struct list_s{

    int key ;
    struct list_s *next ;

} list_t ;

// Function declaration
list_t* new_element( ) ;
list_t* push( list_t* , int ) ;
list_t* pop( list_t* , int * , int * ) ;

// Function implementation
list_t* new_element( ){

    list_t *p ;

    p = ( list_t * ) malloc( sizeof( list_t) ) ;

    if( p == NULL ){
        printf( "Unable to allocate memory for the element!\n" ) ;
        return EXIT_FAILURE ;
    }else{
        return p ;
    }
}

list_t* push( list_t* head , int val ){

    list_t* new = new_element( ) ;
    new->key = val ;
    new->next = head ;
    head = new ;

    return head ; //io lo farei senza fare questa assegnazione. Ritorno direttamente new.
}   


list_t* pop( list_t *head , int* val , int* status ){

    list_t *temp ;

    if( head == NULL ){
        *status = -1 ;
    }else{
        *status = 0 ;
        *val = head->key ;
        temp = head ;
        head = head->next ;
    }

    free( temp ) ;
    
    return head ;
}

