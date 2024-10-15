#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "functions.c"

#define WIDTH 9

int main()
{
    char file_name[ ] = "sudoku_debug.txt" ;
    int N = WIDTH * WIDTH ;
    int grid[ N ] ;

    read_grid( file_name , grid ) ;
    print_grid( grid , WIDTH ) ;
    //solve( grid , WIDTH ) ;

    // TO DO: ricontrollare tutte le conversioni matrice/array e gli shift riga colonna.
    // ho paura di aver fatto un casino.

    return 0 ;


    

}
