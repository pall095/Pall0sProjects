#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>
#include<math.h>


int** allocate_matrix( int , int ) ;
void print_matrix( int** , int , int  ) ;
void initialize_matrix( int** , int , int ) ;
void mirror( int** , int ) ;
void shift_and_insert( int** , int ) ;
void generate_binary( int** , int , int , int ) ;

void main( int argc , char **argv ){


    int col = atoi( argv[ 1 ] ) ;
    int row = pow( 2 , col ) ;
    int **matrix = allocate_matrix( row , col ) ;
    initialize_matrix( matrix , row , col ) ;

    matrix[ 0 ][ 0 ] = 0 ;
    matrix[ 1 ][ 0 ] = 1 ;

    generate_binary( matrix , 1 , row , col ) ;
    print_matrix( matrix , row , col ) ;


}

void shift_and_insert( int **matrix , int depth ){

    int mirror_point = pow( 2 ,  depth );

    for( int j = depth ; j >= 0 ; j-- ){

        for( int i = 0 ; i < 2 * mirror_point ; i++ ){

            matrix[ i ][ j + 1 ] = matrix[ i ][ j ] ;
        }
    }

    for( int i = 0 ; i < 2 * mirror_point ; i ++ ){

        if( i >= mirror_point ){
            matrix[ i ][ 0 ] = 1 ;
        }else{
            matrix[ i ][ 0 ] = 0 ;
        }
    }

}

void generate_binary( int **matrix , int depth , int row , int col ){

    if( depth == col ){
        return ;
    }

    mirror( matrix , depth ) ;
    shift_and_insert( matrix , depth ) ;
    generate_binary( matrix , depth + 1 , row , col ) ;
}


void mirror( int **matrix , int depth  ){

    int mirror_point = pow( 2 ,  depth );
    int mirror_index ;
    for( int i = 0 ; i < depth ; i ++ ){
        for( int j = 0 ; j < mirror_point ; j++ ){     
            mirror_index  = mirror_point - 1 + ( mirror_point - j )  ;
            matrix[ mirror_index  ][ i ] = matrix[ j ][ i ] ; 
        }
    }
}

void initialize_matrix( int **matrix , int row , int col ){

    for( int i = 0 ; i < row ; i++ ){
        for( int j = 0 ; j < col ; j++ ){
            matrix[ i ][ j ] = -1 ;
        } 
    }


}

int** allocate_matrix( int row , int col ){
    int **square ;
    square = ( int** ) malloc( row * sizeof( int* ) ) ;

    for( int i = 0 ; i < row ; i++ ){
        square[ i ] = ( int * ) malloc( col * sizeof( int ) ) ;
    }
    return square ;
} 

void print_matrix( int **square , int row , int col ){

    for( int i = 0 ; i < row ; i ++ ){
        for( int j = 0 ; j < col ; j++ ){
            printf( "%d " , square[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
    printf( "....\n");
}