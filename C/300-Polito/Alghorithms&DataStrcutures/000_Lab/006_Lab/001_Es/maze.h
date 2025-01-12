#ifndef MY_MAZE_H
#define MY_MAZE_H

#include <stdio.h>
#include <stdlib.h>
#include "node.h"

#define ROW 12
#define COL 10
#define START '@'
#define END '#' 
#define WALL '*'
#define EMPTY ' '


void read_maze( char* , char[ ROW ][ COL ] ) ;
void print_maze( char[ ROW ][ COL ] ) ;
void find_start( char[ ROW ][ COL ] , int* , int* ) ;
void solve_maze( char[ ROW ][ COL ] , list_t* , list_t* , list_t* ) ;

#endif 