#include<stdio.h>
#include<stdlib.h>

void hanoi( int , int , int , int ) ;

void main (int argc , char **argv ){
    hanoi( 3 , 3 , 0 , 2 ) ;
    return ;
}


void hanoi( int N , int n , int src , int dest ){

    if( n <= 0 ){
        return ;
    }

    int aux = N - ( src + dest ) ;
    hanoi( N , n - 1 , src , aux ) ;
    printf( "Moving peg %d from %d to %d\n" , n , src , dest ) ;
    hanoi( N , n - 1 , aux , dest ) ;

    return  ;
}