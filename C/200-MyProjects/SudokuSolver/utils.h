#include<stdio.h>
#include<stdlib.h>

#define SIZE 9

void display_grid( int **grid ) ;
int** read_file( char *filename ) ;
int is_valid( int **grid , int r , int c , int num , int verbose ) ;
int is_solved( int **grid ) ;
void solve_r( int **grid , int r , int c ) ;