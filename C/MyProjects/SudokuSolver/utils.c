
#include "utils.h"

void display_grid( int **grid ){
    int extra_char = 5 ;

    for( int k = 0 ; k < 2 * SIZE + extra_char ; k++ ){
            printf( "-" ) ;
        }   

    printf( "\n" ) ;

    for( int i = 0 ; i < SIZE ; i++ ){

        printf( "| " ) ;

        for( int j = 0 ; j < SIZE ; j++ ){

            printf( "%d " , grid[ i ][ j ] ) ;

            if( ( j + 1 ) % 3 == 0 ){
                printf( "| " ) ;
            }
        }

        printf( "\n" ) ;

        if( ( i + 1 ) % 3 == 0 ){
            for( int k = 0 ; k < 2 * SIZE + 4 ; k++ ){
                printf( "-" ) ;
            }   
            printf( "\n" ) ;
        }
    }

    return ;
}

int** read_file( char *filename ){

    int **grid ;
    FILE *f ;
    char *curr_line = ( char * ) calloc( SIZE + 1 , sizeof( char ) ) ;
    int row = 0 ;
    int col = 0 ;

    // Grid init
    grid = ( int ** ) calloc( SIZE , sizeof( int* ) ) ;
    for( int i = 0 ; i < SIZE ; i++ ){
        grid[ i ] = ( int * ) calloc( SIZE , sizeof( int ) ) ;
    } 

    //Open file
    f = fopen( filename , "r" ) ;
    if( f == NULL ){
        printf( "Unable to open file!\n" ) ;
    }

    //Reading 
    row = 0 ;
    while( fscanf( f , "%s" , curr_line ) != EOF ){
        
        for( int i = 0 ; i < SIZE ; i++ ){
            grid[ row ][ col ] = curr_line[ i ] - '0'  ;
            col++ ;
        }
        row++ ;
        col = 0 ;
    } 

    free( curr_line ) ;
    fclose( f ) ;
    return grid ;
}


int is_valid( int **grid , int r , int c , int num , int verbose ){

    int sub_size = SIZE / 3 ;
    int sub_cell_row ;
    int sub_cell_col ;

    for( int i = 0 ; i < SIZE ; i++ ){
        if( grid[ r ][ i ] == num && i != c ){
            if( verbose == 1 ){
                printf( "%d cannot be in %d - %d, row check fails!\n" , num , r , c ) ;
            }
            return 0 ;
        }
    }

    for( int i = 0 ; i < SIZE ; i++ ){
        if( grid[ i ][ c ] == num && i != r ){

            if( verbose == 1 ){
                printf( "%d cannot be in %d - %d, col check fails!\n" , num , r , c ) ;
            }
            return 0 ;
        }
    }

    sub_cell_row = r / sub_size * sub_size ;
    sub_cell_col = c / sub_size * sub_size ;

    for( int i = sub_cell_row ; i < sub_cell_row + sub_size ; i++  ){
        for( int j = sub_cell_col ; j < sub_cell_col + sub_size ; j++ ){
            if( grid[ i ][ j ] == num && i != r && j != c ){
                if( verbose == 1 ){
                    printf( "%d cannot be in %d - %d, cell check fails!\n" , num , r , c ) ;
                }
                return 0 ;
            }
        } 
    }
    return 1 ;
}

int is_solved( int **grid ){

    for( int i = 0 ; i < SIZE ; i++ ){
        for( int j = 0 ; j < SIZE ; j++ ){
            if( is_valid( grid , i , j , grid[ i ][ j ] , 1 ) == 0 ){
                return 0 ;
            }
        }
    }
    return 1 ;
}

void solve_r( int **grid , int r , int c ){

    if( c >= SIZE ){
        c = 0 ;
        r = r + 1 ;
        solve_r( grid , r , c ) ;
        return ;
    }    
    
    if( r >= SIZE ){
        if( is_solved( grid ) == 1 ){
            display_grid( grid ) ;
            printf( "Solved" ) ;
        }else{
            printf( "Not solved!\n" ) ;
        }
        return ;
    }

    if( grid[ r ][ c ] == 0 ){

        for( int k = 0 ; k < SIZE ; k++ ){
            if( is_valid( grid , r , c , k + 1 , 0 ) == 1 ){
                grid[ r ][ c ] = k + 1 ;
                solve_r( grid , r , c + 1 ) ;
                grid[ r ][ c ] = 0 ; 
            }
        }
    }else{
        solve_r( grid , r , c + 1 ) ;
    }
}