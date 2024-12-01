#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>


void find_comb( int *v , int n , int result , int depth , int *marker , int *sol_num , int *sol_arr ){


    char operation[ 4 ] = { '*' , '/' , '+' , '- ' } ;
    int num_operations = 4 ;

    if( *sol_num == result ){
        for( int i = 0 ; i < depth ; i++ ){
            printf( "%c " , sol_arr[ i ] ) ;
        }
    }

    if( depth >= 2*n ){
        return ;
    }

    for( int i = 0 ; i < n ; i++ ){

        if( marker[ i ] == 0 ){
            marker[ i ] == 1 ;
            sol_arr[ depth ] = (char)v[ i ] ;



        }


    }




}


void calculator( int *v , int n , int result ){

    int *marker = ( int* ) malloc( n * sizeof( int ) ) ;
    char *sol_array = ( char * ) malloc( 2 * n *sizeof( char ) ) ;

    for( int i = 0 ; i < n ; i++ ){
        marker[ i ] = 0 ; 
    }
    


}