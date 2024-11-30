#ifndef _SET_PRIVATE
#define _SET_PRIVATE

#include "setPublic.h"

struct set_s{ 
    int num_choiches ;
    char *choiches ;

} ;

set_t set_from_file( char* ) ;
void print_set( set_t ) ;


#endif