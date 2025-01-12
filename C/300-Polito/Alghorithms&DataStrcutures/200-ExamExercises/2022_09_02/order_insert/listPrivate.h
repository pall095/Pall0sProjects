#ifndef _LIST_PRV
#define _LIST_PRV

#include "listPublic.h"

typedef struct list_s{
    char *surname ;
    char *name ;
    struct list_s *next ;
} list_t ;

list_t* new_element( char* , char* ) ;
list_t* order_insert( list_t *list , char* , char* ) ;
void print_list( list_t* ) ;

#endif 