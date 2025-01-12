#ifndef _SET_PUBLIC
#define _SET_PUBLIC 

#include<stdio.h>
#include<stdlib.h>

typedef struct set_s set_t;
extern set_t set_from_file( char* ) ;
extern void print_set( set_t ) ;


#endif
