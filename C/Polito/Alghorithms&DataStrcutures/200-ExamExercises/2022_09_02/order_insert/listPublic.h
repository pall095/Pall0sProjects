#ifndef _LIST_PUB
#define _LIST_PUB

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR 20 

typedef struct list_s list_t ;

list_t* new_element( char* , char* ) ;
list_t* order_insert( list_t* , char* , char* ) ;
void print_list( list_t* ) ;

#endif 