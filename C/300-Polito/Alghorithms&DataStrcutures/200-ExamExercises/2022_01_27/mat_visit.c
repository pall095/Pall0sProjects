#include<stdio.h>
#include<stdlib.h>
#include<float.h>
#include<string.h>
#include<math.h>


void pretty_print_path( int mat[ 3 ][ 3 ] , int **math_path , int r , int c ){

    int step = 1 ;
    int row = 0 ;
    int col = 0 ;

    while( row != r -1 && col != c -1 ){

        for( int i = 0 ; i < r ; i++ ){
            for( int j = 0 ; j < c ; j++ ){
                if( math_path[ i ][ j ] == step ){
                    printf( "Step %d: r : %d - c : %d - w : %d\n" , step , i , j , mat[ i ][ j ] ) ;
                    row = i ;
                    col = j ;
                    step++;
                }
            }
        }
    }

}

void print_path( int **path_mat , int r , int c ){
    for( int i = 0 ; i < r ; i++ ){
        for( int j = 0 ; j < c ; j++ ){
            printf( "%d " , path_mat[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
    printf( "\n" ) ;
    return ;
}

void copy_mat( int **source , int ***dest , int r , int c ){

    int **dest_local = ( int ** ) calloc( r , sizeof( int* ) ) ;
    for( int i = 0 ; i < r ; i++ ){
        dest_local[ i ] = ( int * ) calloc( c , sizeof( int ) ) ;
    }

    for( int i = 0 ; i < r ; i++ ){
        for( int j = 0 ; j < c ; j++ ){
            dest_local[ i ][ j ] = source[ i ][ j ] ; 
        }
    }

    *dest = dest_local ;
    return ;

}


void visit_r( int mat[ 3 ][ 3 ] , int **path_math , int r , int c , int current_row , int current_col , int f , int depth , int *path_weight , int *best_path_weight , int ***best_path_mat ){


    path_math[ current_row ][ current_col ] = depth ;
    *path_weight = *path_weight + mat[ current_row ][ current_col ] ;


    if( current_row == r - 1 && current_col == c - 1 ){
        print_path( path_math , r , c ) ;
        printf( "Path weight: %d \n" , *path_weight ) ;

        if( *path_weight > *best_path_weight ){
            *best_path_weight = *path_weight ;
            copy_mat( path_math , best_path_mat , r , c ) ;
        }


        return ;
    }

    int offset[ 3 ] = { -1 , 0 , 1 } ;

    for( int i = 0 ; i < 3 ; i++ ){
        for( int j = 0 ; j < 3 ; j++ ){

            if( current_row + offset[ i ] >= 0 && current_row + offset[ i ] < r && current_col + offset[ j ] >= 0 && current_col + offset[ j ] < c ){
                if( path_math[ current_row + offset[ i ] ][ current_col + offset[ j ] ] == -1 ){
                    visit_r( mat , path_math , r , c , current_row + offset[ i ] , current_col + offset[ j ] , f , depth + 1 , path_weight , best_path_weight , best_path_mat ) ;
                    path_math[ current_row + offset[ i ] ][ current_col + offset[ j ] ] = -1 ;
                    *path_weight = *path_weight - mat[ current_row + offset[ i ] ][ current_col + offset[ j ] ] ;
                }
            }
        }
    }

}


void mat_visit( int mat[ 3 ][ 3 ] , int r , int c , int f ){

    int **path_mat = ( int** ) calloc( r , sizeof( int* ) ) ;
    int **best_path_mat = ( int** ) calloc( r , sizeof( int* ) ) ;
    for( int i = 0 ; i < r ; i++ ){
        path_mat[ i ] = ( int * ) calloc( c , sizeof( int ) ) ;
        best_path_mat[ i ] = ( int * ) calloc( c , sizeof( int ) ) ;
    }

    for( int i = 0 ; i < r ; i++ ){
        for( int j = 0 ; j < c ; j++ ){
            path_mat[ i ][ j ] = -1 ;
            best_path_mat[ i ][ j ] = -1 ;
        }
    }

    int path_weight = 0 ;
    int best_path_weight = INT_MIN ;


    visit_r( mat , path_mat , r , c , 0 , 0 , f , 1 , &path_weight , &best_path_weight , &best_path_mat ) ;
    printf( "The best path is: \n" ) ;
    print_path( best_path_mat , r , c ) ;
    pretty_print_path( mat , best_path_mat , r , c ) ;
    printf( "The best path weight is: %d\n" , best_path_weight ) ;


}

void main( ){

    int mat[ 3 ][ 3 ] = {{10,10,10},
                     {10,10,10},
                     {10,10,10}};

    int r = 3 ;
    int c = 3 ;

    mat_visit( mat , r , c , 1 ) ;



}