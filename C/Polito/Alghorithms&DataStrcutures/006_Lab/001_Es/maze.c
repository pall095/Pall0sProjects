#include "maze.h"

void solve_maze( char maze[ ROW ][ COL ] , list_t *visited_head , list_t* stack_head , list_t* solution ){

    node_t *extracted ;
    node_t *moved ;
    node_t *dump ;
    stack_head = pop( stack_head , &extracted ) ;

    if( extracted->key == END ){
        printf( "Solved!" ) ;
        print_list( solution ) ;
        printf( "---\n" ) ;
        scanf( "%c" ) ;
        return ;
    }

    
    // Moving UP
    if( ( extracted->row - 1 ) >= 0 && maze[ extracted->row - 1 ][ extracted -> col ] != WALL ){
        moved = new_node( maze[ extracted->row - 1 ][ extracted -> col ] , extracted->row - 1 , extracted -> col ) ;
        if( in_list( visited_head , moved ) == 0 ){
            visited_head = push( visited_head , moved ) ;
            stack_head = push( stack_head , moved ) ;
            solution = push( solution , moved ) ;
            solve_maze( maze , visited_head , stack_head , solution ) ;
            solution = pop( solution , &dump ) ;
        }
    }

    // Moving DOWN
    if( ( extracted->row + 1 ) < ROW && maze[ extracted->row + 1 ][ extracted -> col ] != WALL ){
        moved = new_node( maze[ extracted->row + 1 ][ extracted -> col ] , extracted->row + 1 , extracted -> col ) ;
        if( in_list( visited_head , moved ) == 0 ){
            visited_head = push( visited_head , moved ) ;
            stack_head = push( stack_head , moved ) ;
            solution = push( solution , moved ) ;
            solve_maze( maze , visited_head , stack_head , solution ) ;
            solution = pop( solution , &dump ) ;
        }
    }

    // Moving LEFT
    if( ( extracted->col - 1 ) >= 0 && maze[ extracted->row ][ extracted -> col - 1  ] != WALL ){
        moved = new_node( maze[ extracted->row ][ extracted -> col - 1 ] , extracted->row , extracted -> col - 1 ) ;
        if( in_list( visited_head , moved ) == 0 ){
            visited_head = push( visited_head , moved ) ;
            stack_head = push( stack_head , moved ) ;
            solution = push( solution , moved ) ;
            solve_maze( maze , visited_head , stack_head , solution ) ;
            solution = pop( solution , &dump ) ;
        }
    }

    // Moving RIGHT
    if( ( extracted->col + 1 ) < COL && maze[ extracted->row ][ extracted -> col + 1  ] != WALL ){
        moved = new_node( maze[ extracted->row ][ extracted -> col + 1 ] , extracted->row , extracted -> col + 1 ) ;
        if( in_list( visited_head , moved ) == 0 ){
            visited_head = push( visited_head , moved ) ;
            stack_head = push( stack_head , moved ) ;
            solution = push( solution , moved ) ;
            solve_maze( maze , visited_head , stack_head , solution ) ;
            solution = pop( solution , &dump ) ;
        }
    }
    
    



}

void find_start( char maze[ ROW ][ COL ] , int *s_row , int *s_col ){
    for( int i = 0 ; i < ROW ; i++ ){
        for( int j = 0 ; j < COL ; j++ ){

            if( maze[ i ][ j ] == START ){
                *s_row = i ;
                *s_col = j ;
                return ;
            }
        }
    }
}

void print_maze( char maze[ ROW ][ COL ] ){
    for( int i = 0 ; i < ROW ; i++ ){
        for( int j = 0 ; j < COL ; j++ ){
            printf( "%c" , maze[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
}


void read_maze( char *filename , char maze[ ROW ][ COL ] ){
    FILE *ptr = fopen( filename , "r" ) ;
    char current_char ;
    int i = 0 ;
    int j = 0 ;

    while( fscanf( ptr , "%c" , &current_char ) != EOF ){
        
        if( current_char == '\n' ){
            continue ;
        }else{
            maze[ i ][ j ] = current_char ;
        }
        if( j == ( COL - 1 ) ){
            j = 0 ;
            i = i + 1 ;
        }else{
            j = j + 1 ;
        }
    }

    return ;
}