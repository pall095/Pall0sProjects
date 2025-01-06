#include<stdio.h>
#include<stdlib.h>
#include<float.h>
#include<string.h>
#include<math.h>


int num_colors( int *sol , int n ){
    
    int *color_mask = ( int * ) calloc( n , sizeof( int ) ) ;

    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < n ; j++ ){
            if( sol[ j ] == i + 1  ){
                color_mask[ i ] = 1 ;
            }
        }
    }

    int sum = 0 ;
    for( int i = 0 ; i < n ; i++ ){
        sum = sum + color_mask[ i ] ;
    }

    free( color_mask ) ;
    return sum ;
}

void print_sol( int *sol , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%d " , sol[ i ] ) ;
    }
    printf( " - colors %d\n" ,  num_colors( sol , n ) )  ; 
    return ;
}



int is_valid( int graph[ 4 ][ 4 ] , int *sol , int n ){


    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < n ; j++ ){

            if( graph[ i ][ j ] == 1 && sol[ i ] == sol[ j ] ){
                return 0 ;
            }
        }
    }

    return 1 ; 
}

void color_r( int graph[ 4 ][ 4 ] , int n , int *sol , int depth ){

    if( depth >= n ){
        if( is_valid( graph , sol , n ) == 1 ){
            print_sol( sol , n ) ; 
        }
        return ;
    }

    for( int i = 0 ; i < n ; i++ ){
        sol[ depth ] = i + 1 ;
        color_r( graph , n , sol , depth + 1 ) ;
    }
    return ;

}


void color( int graph[ 4 ][ 4 ] , int n ){


    int *sol = ( int * ) calloc( n , sizeof( int ) ) ;

    color_r( graph , n , sol , 0 ) ;

}

void main( ){

    int graph[ 4 ][ 4 ] = {{ 0 , 1 , 0 , 1 } , { 1 , 0 , 1 , 0 } , { 0 , 1 , 0 , 1 } , { 1 , 0 , 1 , 0 } } ;
    int n = 4 ;
    color( graph , n ) ;


}