#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

void print_mat( int **mat  , int row , int col ){
    for( int i = 0 ; i < row ; i++ ){
        for( int j = 0 ; j < col ; j++ ){
            printf( "%d " , mat[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
    printf( "\n" ) ;
    return ;
}



int eval( int mat[ 3 ][  3 ]  , int **path , int r , int c , int depth ){

    int sum = 0 ;   
    int k = 1 ;

    

    while( k <= depth ){

        for( int i = 0 ; i < r ; i++ ){
            for( int j = 0 ; j < c ; j++ ){

                if( path[ i ][ j ] == k ){
                    sum = sum + mat[ i ][ j ] ;
                    k++ ;
                }
            }
        }
    }

    return sum ;

}

void copy( int **path , int ***best_path , int r , int c ){

    int **best_path_local = ( int ** ) calloc( r , sizeof( int ) ) ;

    for( int i = 0 ; i < r ; i++ ){
        best_path_local[ i ] = ( int * ) calloc( c , sizeof( int ) ) ;
    }

    for( int i = 0 ; i < r ; i++ ){
        for( int j = 0 ; j < c ; j++ ){
            best_path_local[ i ][ j ] = path[ i ][ j ] ;
        }
    }

    *best_path = best_path_local ;

    return ;


}

void mat_visit_r( int mat[ 3 ][  3 ]  , int r , int c , int f , int **path , int ***best_path , int cur_row , int cur_col , int depth , int *best_weight ){

    path[ cur_row ][ cur_col ] = depth ;

    if( cur_row == r - 1 && cur_col == c - 1 ){

        int path_weight = eval( mat , path , r , c , depth ) ;

        if( path_weight > *best_weight   ){
            *best_weight = path_weight ;
            copy( path , best_path , r , c ) ;
            return ;
        }

        if( path_weight == *best_weight ){

            // *( *( *best_path + r - 1 ) + c - 1 ) this accesses the end element of the best path.
            // since the path is marked with a series of number ( 1 to n ), the number in the end point is the amount of steps taken to get there.
            // Since the depth of the current path is the amount of step taken to reach the end point in the current call.
            // I can just compare the two based on the flag "f" (i.e. if I want shortst or longest )

            if( f == 0 ){
                if( depth < *( *( *best_path + r - 1 ) + c - 1 ) ){ 
                    copy( path , best_path , r , c ) ;
                }
            }

            if( f == 1 ){
                if( depth > *( *( *best_path + r - 1 ) + c - 1 ) ){
                    copy( path , best_path , r , c ) ;
                } 
            }


        }

        return ;
    }


    for( int i = -1 ; i <= 1 ; i++ ){
        for( int j = -1 ; j <= 1 ; j++ ){

            if( ( cur_row + i ) >= 0 && ( cur_row + i ) < r && ( cur_col + j ) >= 0 && ( cur_col + j ) < c  ){

                if( path[ cur_row + i ][ cur_col + j ] == -1 ){
                    mat_visit_r( mat , r , c , f , path , best_path , cur_row + i , cur_col + j , depth + 1  , best_weight ) ;
                    path[ cur_row + i ][ cur_col + j ] = -1 ;
                }
            }

        }
    }

}


void mat_visit( int mat[ 3 ][  3 ]  , int r , int c , int f ){

    int **path = ( int ** ) calloc( r , sizeof( int ) ) ;
    int **best_path = ( int ** ) calloc( r , sizeof( int ) ) ;
    int best_weight = INT_MIN ;

    for( int i = 0 ; i < r ; i++ ){
        path[ i ] = ( int * ) calloc( c , sizeof( int ) ) ;
        best_path[ i ] = ( int * ) calloc( c , sizeof( int ) ) ;
    }

    for( int i = 0 ; i < r ; i++ ){
        for( int j = 0 ; j < c ; j++ ){
            path[ i ][ j ] = -1 ;
        }
    }

    mat_visit_r( mat , r , c , f , path , &best_path , 0 , 0 , 1 , &best_weight ) ;
    print_mat( best_path , r , c ) ;



}


void main( int argc , char **argv ){

    int mat[ 3 ][ 3 ] = { { 1 , 2 , -3 } , { 9 , -9 , 7 }  , { 0 , 1 , 4 } } ; 
    mat_visit( mat , 3 , 3 , 1 ) ;
    
}