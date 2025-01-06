#include "utils.h"

void main( int argc , char **argv ){
    int **grid = read_file( argv[ 1 ] ) ;
    solve_r( grid , 0 , 0 ) ;
}