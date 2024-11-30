#ifndef MY_NODE_H
#define MY_NODE_H

#include<stdlib.h>
#include<stdio.h>

typedef struct node_s{
    char key ;
    int row ;
    int col ;
} node_t ;
node_t* new_node( char , int , int ) ;
void print_node( node_t* ) ;


typedef struct list_s list_t ;
list_t* new_list_item( node_t* ) ;
list_t* push( list_t* , node_t* ) ;
list_t* pop( list_t* , node_t** ) ;
void print_list( list_t* ) ;
int in_list( list_t* , node_t* ) ;


#endif
