#include "node.h" 
#include "maze.h"


void main( int argc , char **argv ){


    list_t *visited_list_head = NULL ;
    list_t *stack_head = NULL ;
    list_t *solution = NULL ;
    char maze[ ROW ][ COL ] ;

    read_maze( argv[ 1 ] , maze  ) ;
    int start_row , start_col ;
    find_start( maze , &start_row , &start_col ) ;
    
    node_t *start_node = new_node( '@' , start_row , start_col ) ;
    visited_list_head = push( visited_list_head , start_node ) ;
    stack_head = push( stack_head , start_node ) ;
    solution = push( solution , start_node ) ;

    solve_maze( maze , visited_list_head , stack_head , solution ) ;


}