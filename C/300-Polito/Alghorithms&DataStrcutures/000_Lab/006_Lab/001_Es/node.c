#include "node.h"


typedef struct list_s{
    node_t *node ;
    struct list_s *next ;
} list_t ;

node_t* new_node( char key , int row , int col ){
    node_t *ptr = ( node_t * ) malloc( sizeof( node_t ) ) ;
    if( ptr == NULL ){
        printf( "Unable to allocaate memory for node\n" ) ;
        return NULL ;
    }
    ptr->key = key ;
    ptr->row = row ;
    ptr->col = col ;
    return ptr ;
}


list_t* new_list_item( node_t *node ){
    list_t* list_item = ( list_t* ) malloc( sizeof( list_t ) ) ;
    if( list_item == NULL ){
        printf( "Unable to create new list item" ) ;
    }
    list_item->node = node ;
    list_item->next = NULL ;
    return list_item ;

}

list_t* push( list_t* head , node_t* node ){
    list_t* list_item = new_list_item( node ) ;

    list_item->next = head ;
    head = list_item ;
    return list_item ;

}

list_t* pop( list_t *head , node_t **extracted ){

    *extracted = head->node ;
    head = head->next ;
    return head ;

}

int in_list( list_t *head , node_t *node ){
    while( head != NULL ){
        if( head->node->col == node->col && head->node->row == node->row ){
            return 1 ;
        }
        head = head->next ;
    }
    return 0 ;
}


void print_list( list_t *head ){
    while( head != NULL ){
        print_node( head->node ) ;
        head = head->next ;
    }
    return ;
}

void print_node( node_t* node ){
    printf( "Key : %c - Row : %d - Col : %d\n" , node->key , node->row , node->col ) ;
    return ;
}