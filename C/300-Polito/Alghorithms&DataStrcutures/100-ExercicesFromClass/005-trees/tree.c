#include "tree.h" 


typedef struct trees_s{
    int key ;
    struct tree_s *left;
    struct tree_s *right ;

} tree_t ;


tree_t* new_node( int key , tree_t *left , tree_t* right ){

    tree_t *ptr = ( tree_t* ) malloc( sizeof( tree_t ) ) ;

    if( ptr == NULL ){
        printf( "Unable to allocate memory for tree with key %d\n" , key );
        return NULL ;
    }

    ptr->key = key ;
    ptr->left = left ;
    ptr->right = right ;
    return ptr ;

}

