#include<stdio.h>
#include<stdlib.h>


int* copy( int *sol , int *best_sol , int n ){

    for( int i = 0 ; i < n ; i++ ){
        best_sol[ i ] = sol[ i ] ;
    }

    return best_sol ;

}

void print_sol( int *best_sol , int n , int k ){
    int base = n / k ;
    int extra = n % k ;
    int j = -1 ;

    for( int i = 0 ; i < k ; i++ ){

        if( extra != 0 ){
            for( j = j + 1  ; j < i * k + k + 1 ; j++ ){
                printf( "%d " , best_sol[ j ] ) ;
            }
        }else{
            for( j = j + 1 ; j < i * k + k ; j++ ){
                printf( "%d " , best_sol[ j ] ) ;
            }
        }

        printf( "\n" ) ;

    }
}


float sol_variance( int *sol , int n , int k ){

    int base = n / k ;
    int extra = n % k ;
    int sums[ k ] ;
    int avg = 0 ;
    float variance = 0 ;
    int j = -1 ; 

    for( int i = 0 ; i < k ; i++ ){

        sums[ i ] = 0 ;
        if( extra != 0 ){
            for( j = j + 1  ; j < i * k + k + 1 ; j++ ){
                sums[ i ] = sums[ i ] + sol[ j ] ;
            }
            extra-- ;
        }else{
            for( j = j + 1  ; j < i * k + k ; j++ ){
                sums[ i ] = sums[ i ] + sol[ j ] ;
            }
        }

        avg = avg + sums[ i ] ; 
    }

    avg = avg / ( k - 1 ) ;

    for( int i = 0 ; i < k ; i++ ){

        variance = variance + ( sums[ i ] - avg ) * ( sums[ i ] - avg ) ;

    }

    variance = variance / ( k - 1 ) ;
    return variance ;

}


void simple_arrangements( int vet[ 5 ] , int n , int k , int *marker , int *sol , int *best_sol , int depth ){

    if( depth >= n ){
        if( sol_variance( sol , n , k ) < sol_variance( best_sol , n , k ) ){
            best_sol = copy( sol , best_sol , n ) ;
        }
        return ;
    }

    for( int i = 0 ; i < n ; i++ ){
        if( marker[ i ] == 0 ){
            sol[ depth ] = vet[ i ] ;
            marker[ i ] = 1 ;
            simple_arrangements( vet , n , k , marker , sol , best_sol , depth + 1 ) ;
            marker[ i ] = 0 ;
        }
    }


}


void partition( int vet[ 5 ] , int n , int k ){

    int *sol = ( int * ) malloc( n * sizeof( int ) ) ;
    int *marker = ( int * ) malloc( n * sizeof( int ) ) ;
    int *best_sol = ( int * ) malloc( n * sizeof( int ) ) ;


    for( int i = 0 ; i < n ; i++ ){
        marker[ i ] = 0 ;
        sol[ i ] = 0 ;
        best_sol[ i ] = 0 ;
    }

    simple_arrangements( vet , n , k , marker , sol , best_sol , 0 ) ;

    print_sol( best_sol , n , k ) ;


}

void main( ){

    int vet[ 5 ] = { 1 , 2 , 3 , 4 , 5 } ;
    int n = 5 ; 
    int k = 3 ;

    partition( vet , n , k ) ;

}