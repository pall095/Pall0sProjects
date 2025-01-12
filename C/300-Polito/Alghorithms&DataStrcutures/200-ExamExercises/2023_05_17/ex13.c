#include<stdio.h>
#include<stdlib.h>


void print_sol( int *sol , int n){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%d " , sol[ i ] ) ;
    }
    printf( "\n" ) ;
    return ;
}

void print_operation_sol( char *operation_sol , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%c " , operation_sol[ i ] ) ;
    }
    printf( "\n" ) ;
    return ;
}

int eval( int *sol , char *operation_sol , int n ){

    int value = sol[ 0 ] ;

    for( int i = 0 ; i < n - 1 ; i++ ){

        switch( operation_sol[ i ] ){

            case '+' :
                value = value + sol[ i + 1 ] ;
                break ;
            case '-' :
                value = value - sol[ i + 1 ] ;
                break ;
            case '/' :
                value = value / sol[ i + 1 ] ;
                break ;
            case '*' :
                value = value * sol[ i + 1 ] ;
                break ;
            default :
                printf( "\n") ;
        }
    }

    return value ;

}

void pretty_print_result( int *sol , char *operation_sol , int result , int n ) {

    for( int i = 0 ; i < n - 1 ; i++ ){
        printf( "%d %c " , sol[ i ] , operation_sol[ i ] ) ;
    }
    printf( "%d = %d\n" , sol[ n - 1 ]  , result ) ;
    return ;


}

void permutate_operations_r( char operations[ 4 ] , int *sol , char *operation_sol , int depth , int result , int n ){

    if( depth >= n - 1 ){

        if( eval( sol , operation_sol , n ) == result ){
            pretty_print_result( sol , operation_sol , result , n ) ;
        }
        
        return ;
    }

    for( int i = 0 ; i < 4 ; i++ ){
        operation_sol[ depth ] = operations[ i ] ;
        permutate_operations_r( operations , sol , operation_sol , depth + 1 , result , n ) ;
    }


}

void permutate_operations( int *sol , int result , int n ){

    char operations[4 ] = { '+' , '-' , '*' , '/' } ;
    char *operation_sol = ( char * ) calloc( n - 1 , sizeof( char ) ) ;

    permutate_operations_r( operations , sol , operation_sol , 0 , result , n ) ;

}

void generate( int *v , int n , int *sol , int *marker , int depth , int result ){

    if( depth >= n ){
        permutate_operations( sol , result , n ) ;
        return ;
    }


    for( int i = 0 ; i < n ; i++ ){

        if( marker[ i ] == 0 ){
            marker[ i ] = 1 ;
            sol[ depth ] = v[ i ] ;
            generate( v , n , sol , marker , depth + 1 , result ) ;
            marker[ i ] = 0 ;
            sol[ depth ] = 0 ;
        }

    }
}



void calculator( int *v , int n , int result ){


    
    int *sol = ( int * ) calloc( n , sizeof( int ) ) ;
    int *marker = ( int * ) calloc( n , sizeof( int ) ) ;


    generate( v , n , sol , marker , 0 , result ) ;

}

void main( ){
    int n = 4 ;
    int *v = ( int * ) calloc( n , sizeof( int ) ) ;
    int result = 12000 ;

    v[ 0 ] = 3 ; v[ 1 ] = 2 ; v[ 2 ] = 25 ; v[ 3 ] = 5 ;
    calculator( v , n , result ) ;
}