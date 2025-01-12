#include "utils.h"

void main( int argc , char **argv ){
    int **grid = read_file( argv[ 1 ] ) ;
    printf( "Grid before solution: \n" ) ;
    display_grid( grid ) ;
    printf( "Grid after being solved: \n" ) ;
    solve_r( grid , 0 , 0 ) ;
}
