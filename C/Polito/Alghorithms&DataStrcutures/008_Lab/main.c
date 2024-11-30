#include <stdio.h>
#include <stdlib.h>
#include "treePublic.h"


void main( int argc , char **argv ){

    FILE *ptr = fopen( argv[ 1 ] , "r" ) ;
    if( ptr == NULL ){
        printf( "Unable to read the file!\n" ) ;
        return ;
    }

    node_t *tree = readTree( ptr ) ;

}
