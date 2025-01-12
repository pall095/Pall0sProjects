#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct list_s{
    char *key ;
    int is_common ;
    struct list_s *next ;
} list_t ;

typedef struct node_s{

    char *key ;
    struct node_s *l ;
    struct node_s *r ;

} node_t ;


int search( node_t *root , char *key ){

    if( root == NULL ){
        return 0 ;
    }
    if( strcmp( root->key , key ) < 0 ){
        return search( root->l , key ) ;
    }
    if( strcmp( root->key , key ) > 0 ){
        return search( root->r , key ) ;
    }
    return 1 ;
}

list_t* new_elem( char *key ){
    list_t *ptr = ( list_t * ) malloc( sizeof( list_t ) ) ;
    if( ptr == NULL ){
        printf( "Unable to allocate memory!\n" ) ;
        return NULL ;
    } 
    ptr->key = ( char * ) malloc( ( strlen( key ) + 1 ) * sizeof( char )  );
    strcpy( ptr->key , key ) ;
    return ptr ;

}

list_t* push( list_t* head , list_t *new  ){
    new->next = head ;
    head = new ;
    return head ;
}

list_t* pre_order_flattener( node_t *root , list_t *head ){

    if( root == NULL ){
        return head;
    }

    list_t *new = new_elem( root->key ) ;
    new->is_common = 1 ;

    head = push( head , new ) ;

    head = pre_order_flattener( root->l , head ) ;
    head = pre_order_flattener( root->r , head ) ;

    return head ;

}

void display_common( node_t *root[ N ] ){

    list_t *main_linearized = NULL ;
    list_t *traverser ;
    main_linearized = pre_order_flattener( root[ 0 ] , main_linearized ) ;
    traverser = main_linearized ;
    while( traverser != NULL ){

        traverser = main_linearized;
        for( int i = 1 ; i < N ; i++ ){
            if( search( root[ i ] , traverser->key ) == 0 ){
                traverser->is_common = 0 ;
                break ;
            }else{
                traverser = traverser->next ;
            } 
        }
    }

    traverser = main_linearized ;
    while( main_linearized != NULL ){

        traverser = main_linearized ;
        if( traverser->is_common == 1 ){
            printf( "%s " , main_linearized->key ) ;
        }
        main_linearized = main_linearized->next ;
        free( traverser ) ;
    }
}





