#include<stdio.h>
#include<stdlib.h>



typedef struct list_s{

    char key ;
    struct list_s *next ;

} list_t ;

list_t* new_element( ){

    list_t *ptr = ( list_t * ) malloc( sizeof( list_t ) ) ;
    return ptr ;
}

list_t *push( list_t *head , list_t *new ){
    
    new->next = head ;
    head = new ;
    return head ;
}

int is_in( list_t *head , char c ){

    while( head != NULL ){
        if( head->key == c ){
            return 1 ;
        }
        head = head->next ;
    }

    return 0 ;
}

void print_list( list_t *head ){
    while( head != NULL ){
        printf( "%c -> " , head->key ) ;
        head = head->next ;
    }
    printf( "\n" ) ;
}

void erase_duplicate( char *str ){

    list_t *head = NULL ;
    list_t *new ;
    int list_len = 0 ;
    char *clean_string ;
    int cnt = 0 ;

    while( *str != '\0' ){

        if( is_in( head , *str ) == 0 ){
            new = new_element( ) ;
            new->key = *str ;
            head = push( head , new ) ;
            list_len++ ;
        }
        str++ ;
    }

    clean_string = ( char * ) calloc( ( list_len + 1 ) , sizeof( char ) ) ;

    while( head != NULL ){
        clean_string[ cnt ] = head->key ;
        cnt++ ;
        head = head->next ;
    }
    printf( "The cleaned string is: %s \n" , clean_string ) ;
    return ;

}


void main( ){

    char *str = "aa;;;bbbab" ;
    erase_duplicate( str ) ;


}
