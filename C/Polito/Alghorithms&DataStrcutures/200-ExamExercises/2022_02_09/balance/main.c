#include<stdlib.h>
#include<stdio.h>


float* read_flow( char* , int* ) ;
float* balance( float* , int ) ;
void permutate( float* , float* , int* , int , int , float* , float* ) ;
float calculate_min_balance( float* , int ) ;
float calculate_max_balance( float* , int ) ;
void print_sol( float* , int ) ;


void main( int argc , char **argv ){

    int n = 0 ;
    float *flow = read_flow( argv[ 1 ] , &n ) ;
    float *tette = balance( flow , n ) ;
    
}

float* balance( float *flow , int n ){

    int *mark = ( int * ) malloc( n * sizeof( int ) ) ;
    float *sol = ( float* ) malloc( n * sizeof( int ) ) ;
    float *best_sol = ( float* ) malloc( n * sizeof( int ) ) ;
    float min_deltaBalance = 1000 ;

    for( int i = 0 ; i < n ; i++ ){
        mark[ i ] = 0 ;
    }
    permutate( flow , sol , mark , n , 0  , &min_deltaBalance, best_sol ) ;
    print_sol( best_sol , n ) ;
    return 0 ;
}

void print_sol( float *sol, int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%f " , sol[ i ] ) ;
    }
    printf( "\n" ) ;
}

void permutate( float *flow , float *sol , int *mark , int n , int depth , float *min_deltaBalance , float *best_sol ){
    
    float delatBalance ;
    
    if( depth >= n ){
        delatBalance = calculate_max_balance( sol , n ) - calculate_min_balance( sol , n ) ;

        print_sol( sol , n ) ;
        printf( "Delta balance: %f \n---\n" , delatBalance ) ;

        if( delatBalance < *min_deltaBalance ){
            *min_deltaBalance = delatBalance ;
            for( int i = 0 ; i < n ; i++ ){
                best_sol[ i ] = sol[ i ] ;
            }
        }
        return ;
    }


    for( int i = 0 ; i < n ; i++ ){

        if( mark[ i ] == 0 ){
            sol[ depth ] = flow[ i ] ;
            mark[ i ] = 1 ;
            permutate( flow , sol , mark , n , depth + 1 , min_deltaBalance , best_sol ) ;
            mark[ i ] = 0 ;
        }
    }


}


float calculate_min_balance( float *sol , int n ){

    float min_balance = 10000 ;
    float curr_balance = 0  ; 

    for( int i = 0 ; i < n ; i++ ){
        curr_balance = curr_balance + sol[ i ] ;
        if( curr_balance < min_balance ){
            min_balance = curr_balance ;
        }
    }

    return min_balance ;
}

float calculate_max_balance( float *sol , int n ){

    float max_balance = -10000 ;
    float curr_balance = 0  ; 

    for( int i = 0 ; i < n ; i++ ){
    
        curr_balance = curr_balance + sol[ i ] ;
        if( curr_balance > max_balance ){
            max_balance = curr_balance ;
        }
    }
    return max_balance ;
}

float* read_flow( char *filename , int *n ){

    FILE *f_ptr = fopen( filename , "r" ) ;
    char sign ;
    float value ;
    
    if( f_ptr == NULL ){
        printf( "Unable to open the file!\n" ) ;
        return NULL ;
    }
    while( fscanf( f_ptr , "%c %f" , &sign , &value ) != EOF ){
        *n = *n + 1 ;
    }
    fclose( f_ptr ) ;
    f_ptr = fopen( filename , "r" ) ;
    float *flow = ( float * ) malloc( *n * sizeof( float ) ) ;
    int i = 0 ;
    while( fscanf( f_ptr , "%c %f" , &sign , &value ) != EOF ){
        
        if( sign == '-' ){
            flow[ i ] = -value ;
        }else{
            flow[ i ] = value ;
        }

        i = i + 1;
    }

    return flow ;

}