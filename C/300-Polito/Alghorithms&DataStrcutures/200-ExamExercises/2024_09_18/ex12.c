#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_NAME 100 

typedef struct list_s{
    int val ;
    struct list_s *next ;

} list_t ;


typedef struct node_s{
    char *key ;
    struct node_s *left ;
    struct node_s *right ;
    list_t *head ;
} node_t ;

void print_list( list_t *head ){

    while( head != NULL ){
        printf( "%d -> " , head->val ) ;
        head = head->next ;
    }
    printf( "\n" ) ;

}

void print_tree_pre( node_t *root ){

    if( root == NULL ){
        return ;
    }

    printf( "%s " , root->key ) ;
    print_list( root->head ) ;
    print_tree_pre( root->left ) ;
    print_tree_pre( root->right ) ;
}

void print_tree_in( node_t *root ){

    if( root == NULL ){
        return ;
    }

    
    print_tree_in( root->left ) ;
    printf( "%s " , root->key ) ;
    print_list( root->head ) ;
    print_tree_in( root->right ) ;
}


list_t* new_list( ){

    list_t *ptr = ( list_t * ) malloc( sizeof( list_t ) ) ;

    if( ptr == NULL ){
        printf( "Unable to allocate memory for list element!\n" );
        return NULL ;
    }
    return ptr ;
}

list_t* push( list_t *head , int val ){
    list_t *ptr = ( list_t * ) malloc( sizeof( list_t ) ) ;
    ptr->val = val ;
    ptr->next = head ;
    head = ptr ;
    return head ;
}


node_t* new_node( char *key , node_t *left , node_t* right ){
    
    node_t *ptr = ( node_t * ) malloc( sizeof( node_t ) ) ;
    if( ptr == NULL ){
        printf( "Unable to allocate memory for node!\n" ) ;
        return NULL ;
    }

    ptr->key = ( char * ) malloc( ( strlen( key) + 1 ) * sizeof( char ) ) ;
    strcpy( ptr->key , key ) ;
    ptr->left = left ;
    ptr->right = right ;
    ptr->head = NULL ;

    return ptr ;
}

node_t* find( node_t *root , char *key ){

    if( root == NULL ){
        return NULL ;
    }

    if( strcmp( key , root->key ) > 0 ){
        return find( root->right , key ) ; 
    }

    if( strcmp( key , root->key ) < 0 ){
        return find( root->left , key ) ;
    }

    return root ;

}

node_t* insert( node_t *root , node_t *new ){

    if( root == NULL ){
        return new ;
    }

    if( strcmp( new->key , root->key ) > 0 ){
        root->right = insert( root->right , new ) ;
    }

    if( strcmp( new->key , root->key ) < 0 ){
        root->left = insert( root->left , new ) ;
    }

    return root ;
}


node_t* file_to_bst_of_lists( char *filename ){

    FILE *f_ptr = fopen( filename , "r" ) ;
    node_t *tmp_node ;
    node_t *root = NULL ;
    
    char temp_key[ MAX_NAME + 1 ] ;
    int num_values ;
    int current_value ;
    int i ;
    int found = 0 ;


    if( f_ptr == NULL ){
        printf( "Unable to open the file!\n" ) ;
        return NULL ;
    }else{
        printf( "File opened correctly!\n" ) ;
    }

    while( fscanf( f_ptr , "%s %d" , temp_key , &num_values ) != EOF ){

        tmp_node = find( root , temp_key ) ;
        if( tmp_node == NULL  ){
            tmp_node = new_node( temp_key , NULL , NULL ) ;
            found = 0 ;      
        }else{
            found = 1 ;
        }

        i = 0 ;
        while( i < num_values ){
            fscanf( f_ptr , " %d" , &current_value ) ;
            tmp_node->head = push( tmp_node->head , current_value ) ;
            i++ ; 
        }

        if( found == 0 ){
            root = insert( root , tmp_node ) ;
        }
    }


    return root ;
}

void main( int argc , char **argv ){

    node_t *root = file_to_bst_of_lists( argv[ 1 ] ) ;
    print_tree_pre( root ) ;
    printf( "----" ) ;  
    print_tree_in( root ) ;

}


