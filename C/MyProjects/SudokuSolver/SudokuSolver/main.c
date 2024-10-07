#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "functions.h"

#define WIDTH 9

int main()
{

    char file_name[ ] = "sudoku.txt" ;
    int grid[ WIDTH ][ WIDTH ] ;
    read_grid( file_name , grid , WIDTH , false ) ;
    print_grid( grid , WIDTH ) ;


    return 0 ;

}
