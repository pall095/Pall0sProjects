#include<stdio.h>
#include<stdlib.h>

typedef struct list_s list_t ;
list_t* new_element( ) ;
list_t* read_from_file( char* , int ) ;
list_t* push( list_t* , int ) ;
void print_list( list_t* ) ;