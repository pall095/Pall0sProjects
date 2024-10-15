#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

/*--- HELPER FUNCTIONS ---  */
void print_grid( int *grid , int WIDTH ){
    for( int i = 0 ; i < WIDTH * WIDTH ; i++ ){
        printf("%d " , grid[ i ] );
        if( ( i + 1 ) % WIDTH == 0 ){
            printf("\n" );
        }
    }
}


void read_grid( char *file_name , int *grid ){
    FILE *fp = fopen( file_name , "r" ) ;
    int index = 0 ;
    int current_num = 0 ;
    if( fp == NULL ){
        printf( "Unable to open file!\n" ) ;
        return ;
    }
    while( fscanf( fp , "%d" , &current_num ) != EOF ){
        grid[ index ] = current_num ;
        index++ ;
    }
}

/* --- END of Helper Functions --- */

/* --- Array <--> Matrix conversion functions --- */

int rowcol2index( int row , int col , int WIDTH ){
    return ( row * WIDTH ) + col ;
}

void index2rowcol( int index , int *row , int *col , int WIDTH ){
    *row = index / WIDTH ;
    *col = index % WIDTH ;
    return ;
}

/* --- END of  Array <--> Matrix conversion functions*/

int isEmpty( int *grid , int row , int col , int WIDTH ){  
    int index = rowcol2index( row , col , WIDTH ) ;  
    if( grid[ index ] == 0 ){
        return 1 ;
    }else{
        return 0 ;
    }  
}

int isSafe( int *grid , int row , int col , int n , int WIDTH , int verbose ){
    int index = rowcol2index( row , col , WIDTH ) ;
    int i , j ;
    int row_ok = 1 ;
    int col_ok = 1 ;
    int cell_ok = 1 ;
    int ok = 1 ;

    // Check for rows
    for( i = row * WIDTH ; i < row * WIDTH + WIDTH ; i++  ){
        if( grid[ i ] == grid[ index ] ){
            ok = 0 ; 
            row_ok = 0 ;
        }
    }

    // Check for columns
    for( i = col ; i < col + ( WIDTH - 1 )*WIDTH ; i = i + WIDTH ){
        if( grid[ i ] == grid[ index ] ){
            ok = 0 ;
            col_ok = 0 ;
        }
    }

    // Check for cell
    // Seems silly to divide and multiply for the same value. But this way, you get the starting indices of the submatrixes.
    int sub_matrix = 3 ;
    int start_row = floor( row / sub_matrix ) * sub_matrix;
    int start_col = floor( col / sub_matrix ) * sub_matrix ;
    int start_index = rowcol2index( start_row , start_col , WIDTH ) ;
    int end_index = rowcol2index( start_row + sub_matrix , start_col + sub_matrix , WIDTH ) ;
    i = start_index ;
    j = 0 ;

    while( ( i + j ) < end_index ){     
        if( grid[ i + j ] == n ){
            ok = 0 ;
            cell_ok = 0 ;
        }
        j++ ;
        if( j == sub_matrix ){
            j = 0 ;
            i = i + WIDTH ;
        }
    }

    if( verbose == 1 ){
        if( ok == 0 ){
            printf( "Number %d CANNOT be placed in %d : %d\n" , n , row  , col ) ;
            if( row_ok == 0 ){
                printf( "Row KO\n" );
            }

            if( col_ok == 0 ){
                printf( "Col KO\n" ) ;
            }

            if( cell_ok == 0 ){
                printf( "Cell KO\n" ) ;
            }
        }else{
            printf( "Number %d CAN be placed in %d : %d\n" , n , row  , col ) ;
        }
    }

    return ok ;

}


int solve( int *grid , int WIDTH ){

    int N = WIDTH * WIDTH ;
    int i  ;
    int trial_index = -1 ;
    int trial_row = 0 ;
    int trial_col = 0 ;
    int trial_num = 0 ;


    for( i = 0 ; i < N ; i++ ){
        if( grid[ i ] == 0 ){
            trial_index = i ;
            break ;
        }
    }
    
    if( trial_index == -1 ){
        printf( "Sudoku solved! \n" ) ;
        return ;
    }

    if( trial_index != -1 ){
        for( trial_num = 1 ; trial_num <= WIDTH , trial_num++ ){
            index2rowcol( i , &trial_row , &trial_col ) ;
            if( isSafe( grid , trial_row , trial_col ) ){
                grid[ i ] = trial_num ;
                solve( grid , WIDTH ) ;
            }
        }
    }
    
}


