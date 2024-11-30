#include "list_fun.h" 


typedef struct list_s{
    int val ;
    struct list_s* next ;
} list_t ;


list_t* new_element( void ){
    list_t* ptr = ( list_t* ) malloc( sizeof( list_t ) ) ;
    if( ptr == NULL ){
        printf( "Unable to allocate memory!\n" ) ;
        return NULL ;
    }
    return ptr ;
}

list_t* read_from_file( char *filename , int mode ){
    FILE *ptr = fopen( filename , "r" ) ;
    int current_value ;
    list_t* head = NULL ;
    list_t* new ; 
    if( ptr == NULL ){
        printf( "Unable to open the file!\n ") ;
        return NULL ;
    }
    while( fscanf( ptr , "%d" , &current_value ) != EOF ){
        head = push( head , current_value ) ;
    }
    fclose( ptr ) ;
    return head ; 
}

void print_list( list_t* head ){
    while( head != NULL ){
        printf( "%d --> " , head->val ) ;
        head = head->next ;
    }
    printf( "\n" ) ;
}

list_t* push( list_t* head , int val ){
    list_t* new = new_element( ) ;
    new->val = val ;
    new->next = head ;
    head = new ;
    return head ;
}



