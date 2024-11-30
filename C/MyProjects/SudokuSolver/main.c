#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define SIZE 9 
#define SUB_SIZE 3 


void read_sudoku( int** , char* ) ;
void print_sudoku( int** ) ; 
int solve( int** , int , int ) ;
int is_solved( int ** ) ;
int is_empty( int** , int , int ) ;
int is_valid( int** , int , int , int ) ;
int** allocate_matrix( void ) ;

void main( int argc , char **argv ){

    int **sudoku = allocate_matrix( ) ;
    int solved ; 
    read_sudoku( sudoku , argv[ 1 ] ) ;
    print_sudoku( sudoku ) ; 
    printf( "-------\n" ) ;
    solved = solve( sudoku , 0 , 0 ) ;
    print_sudoku( sudoku ) ;

}

int solve( int **matrix , int row , int col ){
    
    int solved = 0 ;
    if( is_solved( matrix ) == 1 ){
        printf( "Solved!\n") ;
        print_sudoku( matrix ) ;
        return 1;
    }

    if( is_empty( matrix , row , col ) == 0 ){
        if( col == ( SIZE - 1 ) ){
            return solve( matrix , row + 1 , 0 );
        }else{
            return solve( matrix , row , col + 1 ) ;
        }
    }
    
    for( int num = 1 ; num <= SIZE ; num++ ){
        if( is_valid( matrix , row , col , num ) == 1 ){
            matrix[ row ][ col ] = num ;
            if( col = ( SIZE -1 ) ){
                solved = solve( matrix , row + 1 , 0 ) ;
            }else{
                solved = solve( matrix , row , col + 1 ) ; 
            }

            if( is_solved( matrix ) == 1 ){
                return 1 ;
            }else{
                matrix[ row ][ col ] = 0 ;
            }
        }
    }
    return solved ; 
}

void print_sudoku( int **matrix ){

    for( int i = 0 ; i < SIZE ; i++ ){
        for( int j = 0 ; j < SIZE ; j++ ){
            printf( "%d " , matrix[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
}

int is_solved( int **matrix ){
    for( int i = 0 ; i < SIZE ; i++ ){
        for( int j = 0 ; j < SIZE ; j++ ){
            if( matrix[ i ][ j ] == 0 ){
                return 0 ;
            }
        }
    }
    return 1 ;
}


int is_valid( int **matrix , int row , int col , int n ){

    // Single value check.
    if( matrix[ row ][ col ] == n ){
        printf( "%d is alrady present in cell %d : %d\n" , n , row , col ) ;
        return 0 ;
    }
    
    // Row check
    for( int j = 0 ; j < SIZE ; j++ ){
        if( matrix[ row ][ j ] == n ){
            printf( "%d cannot stay in row %d\n" , n , row ) ;
            return 0 ;
        }
    }

    // Column check
    for( int i = 0 ; i < SIZE ; i++ ){
        if( matrix[ i ][ col ] == n ){
            printf( "%d cannot stay in col %d\n" , n , col ) ;
            return 0 ;
        }
    }

    // Subsquare check
    int sub_row = row / SUB_SIZE ;
    int sub_col = col / SUB_SIZE ;

    for( int i = 0 ; i < SUB_SIZE ; i++ ){
        for( int j = 0 ; j < SUB_SIZE ; j++ ){
            if( matrix[ sub_row + i ][ sub_col + j ] == n ){
                printf( "%d cannot stay in subblock %d %d\n" , n , sub_row , sub_col ) ;
                return 0 ;
            }
        }
    }
    printf( "%d can stay in %d %d\n" , n , row , col ) ;
    return 1 ;
}

int is_empty( int **matrix , int row , int col ){
    if( matrix[ row ][ col ] == 0 ){
        return 1 ;
    }
    return 0 ;
}

void read_sudoku( int **matrix , char *filename ){
    FILE *ptr = fopen( filename , "r" ) ;
    int i = 0 ;
    int j = 0 ;
    int current_value ;

    if( ptr == NULL ){
        printf( "Unable to open the input file!\n" ) ;
        return ;
    }

    while( fscanf( ptr , "%d" , &current_value ) != EOF ){
        matrix[ i ][ j ] = current_value ;
        if( j == SIZE - 1 ){
            i = i + 1 ;
            j = 0 ; 
        }else{
            j++ ;
        }
    }
    return ; 
}

int** allocate_matrix( void ){
    int **matrix ;
    matrix = ( int** ) malloc( SIZE * sizeof( int* ) ) ;
    for( int i = 0 ; i < SIZE ; i++ ){
        matrix[ i ] = ( int* ) malloc( SIZE * sizeof( int ) ) ;
    }
    return matrix ; 
}