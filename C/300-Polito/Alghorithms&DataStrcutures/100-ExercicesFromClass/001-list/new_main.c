#include "list_fun.h"


void main( int argc , char **argv ) {

    list_t *head = read_from_file( argv[ 1 ] , 0  ) ;
    print_list( head ) ;

    return ;

}