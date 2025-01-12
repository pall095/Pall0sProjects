#include<stdio.h>
#include<stdlib.h>


#define N 4 

void print_sol( int *sol , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%d " , sol[ i ] ) ;
    }
    printf( "\n" ) ;
}

int* copy( int *sol , int *best_sol , int n ){

    for( int i = 0 ; i < n ; i++ ){
        best_sol[ i ] = sol[ i ] ;
    }

    return best_sol ;
}

int find_delta( int *sol , int n ){

    int min = INT_MAX ;
    int max = INT_MIN ;
    int balance = 0 ;

    for( int i = 0 ; i < n ; i++ ){
        
        balance = balance + sol[ i ] ;
        
        if( balance < min ){
            min = balance ;
        }

        if( balance > max ){
            max = balance ;
        }
    }

    printf( "With sol: \n" ) ;
    print_sol( sol , n ) ;
    printf( "The delta is : %d \n" , max - min ) ;

    return ( max - min ) ;


}

int *find_best( int flow[ N ] , int *marker , int *sol , int n , int depth , int *min_diff , int *best_sol ){


    if( depth >= n ){
        int current_delta = find_delta( sol , n ) ; 
        if( current_delta < *min_diff ){
            printf( "Updating min diff from %d to %d\n" , *min_diff , current_delta ) ;
            *min_diff = current_delta ;
            best_sol = copy( sol , best_sol , n ) ;
        }
    }

    for( int i = 0 ; i < n ; i++ ){
        if( marker[ i ] == 0 ){
            marker[ i ] = 1 ;
            sol[ depth ] = flow[ i ] ;
            find_best( flow , marker , sol , n , depth + 1 , min_diff , best_sol ) ;
            marker[ i ] = 0 ;
            sol[ depth ] = 0 ;
        }
    }


    return best_sol ;

}

int *balance( int flow[ N ] , int n ){


    int *marker = ( int * ) malloc( sizeof( int ) ) ;
    int *sol = ( int * ) malloc( sizeof( int ) ) ;
    int *best_sol = ( int * ) malloc( sizeof( int ) ) ;
    int min_dif = INT_MAX ;

    for ( int i = 0 ; i < n ; i++ ){
        marker[ i ] = 0 ;
        sol[ i ] = 0 ;
        best_sol[ i ] = 0 ;
    }

    find_best( flow , marker , sol , n , 0 , &min_dif , best_sol ) ; 
    return best_sol ;

}

void main( ){

    int flow[ N ] = { -5 , 10 , 7 , -8 } ;
    int *best_sol = balance( flow , N ) ;

    printf( "Best is: \n" ) ;
    for( int i = 0 ; i < N ; i++ ){
        printf( "%d " , best_sol[ i ] ) ; 
    }



}