#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h> 


typedef struct list_s{
    char *s ;
    struct list_s *next ;
} list_t ;

list_t* new_element( int len ){

    list_t *ptr = ( list_t* ) malloc( sizeof( list_t ) ) ;
    ptr->s = ( char * ) malloc( len * sizeof( char ) ) ;

}

list_t *push( list_t *tail , list_t *new ){

    if( tail == NULL ){
        tail = new ;
        tail->next = new ;
    }else{

        new->next = tail->next ;
        tail->next = new ;
    }

    return tail ;

}

void string_to_fifo( char *s , list_t **letter , list_t **digit ){

    int len = strlen( s ) ; 
    int is_char = 0 ;

    char letter_buffer[ len ] ;
    char digit_buffer[ len ] ;

    list_t *local_letter = new_element( len ) ;
    list_t *num_local = new_element( len ) ;

    local_letter = NULL ;
    num_local = NULL ;

    list_t *new ;

    if( isalpha( s[ 0 ] ) ){
        is_char = 1 ;
        letter_buffer[ 0 ] = s[ 0 ] ;
    }else{
        is_char = 0 ;
        digit_buffer[ 0 ] = s[ 0 ] ;
    }

    for( int i = 1 ; i < len ; i++ ){

        if( is_char == 1 ){

            if( isalpha( s[ i ] ) == 1 ){
                digit_buffer[ i ] = s[ i ] ;
            }else{
                is_char = 0 ;
                new = new_element( len ) ;
                strcpy( new->s , digit_buffer ) ;
                local_letter = push( local_letter , new ) ;
            }
        }


    }

    *letter = local_letter ;
    *digit = num_local ;



}


