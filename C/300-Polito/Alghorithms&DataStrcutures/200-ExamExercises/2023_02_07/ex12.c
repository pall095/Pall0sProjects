#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define MAX_CHAR 101

typedef struct list_s{
    char key[ MAX_CHAR ] ;
    struct list_s *next ;
} list_t ;


typedef struct bst_s{
    int key ;
    struct bst_s *left ;
    struct bst_s *right ;
    list_t *head ;
} bst_t ;

void print_list( list_t *head ){
    while( head != NULL ){
        printf( "%s --> " , head->key ) ;
        head = head->next ;
    }
    printf( "\n" ) ;
    return ;
}

void print_tree( bst_t *root ){

    if( root == NULL ){
        return ;
    }

    printf( "%d : " , root->key ) ;
    print_list( root->head ) ;
    print_tree( root->left ) ;
    print_tree( root->right ) ;
    return ;

}


bst_t* new_bst( int key , bst_t *left , bst_t *right ){

    bst_t *ptr = ( bst_t * ) calloc( 1 , sizeof( bst_t ) ) ;
    ptr->key = key ;
    ptr->left = left ;
    ptr->right = right ;
    ptr->head = NULL ;
    return ptr;
}

list_t* new_list( char key[ MAX_CHAR ] ){
    list_t *ptr = ( list_t * ) calloc( 1 , sizeof( list_t ) ) ;
    strcpy( ptr->key , key ) ;
    return ptr ;
}

list_t* push( list_t *head , list_t *new ){
    new->next = head ;
    head = new ;
    return head ;
}


bst_t* insert_recursive( bst_t *root , bst_t* new_b , list_t *new_l ){

    if( root == NULL ){
        root = new_b ;
        root->head = push( root->head , new_l ) ;
        return root ;
    }

    if( root->key > new_b->key ){
        root->left = insert_recursive( root->left , new_b , new_l ) ;
        return root ;
    }

    if( root->key < new_b->key ){
        root->right = insert_recursive( root->right , new_b , new_l ) ;
        return root ;
    }

    if( root->key == new_b->key ){
        root->head = push( root->head , new_l ) ;
        return root ;
    }

}


bst_t* insert( char *file ){

    FILE *f_ptr = fopen( file , "r" ) ;
    bst_t *root = NULL ;
    int current_num ;
    char current_name[ MAX_CHAR ] ;
    bst_t *new_b ;
    list_t *new_l ;

    while( fscanf( f_ptr , "%d %s" , &current_num , current_name ) != EOF ){

        new_b = new_bst( current_num , NULL , NULL ) ;
        new_l = new_list( current_name ) ;
        root = insert_recursive( root , new_b , new_l ) ;
    }

    return root ;

}

void main( int argc , char **argv ){

    bst_t *root = insert( argv[ 1 ] ) ;
    print_tree( root ) ;
}
