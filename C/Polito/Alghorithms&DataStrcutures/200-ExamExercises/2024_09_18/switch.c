#include<stdio.h>
#include<stdlib.h>
#include<string.h>


#define SW 4
#define BULB 5 

int is_final( int *state , int bulb ){

    for( int i = 0 ; i < bulb ; i++ ){
        if( state[ i ] != 1 ){
            return 0 ;
        }
    }
    return 1 ;
}


void permuatate( int mat[ SW ][ BULB ]  , int *sol , int *state , int sw , int bulb , int depth , int start ){

    if( depth >= sw ){
        return ;
    }

    for( int i = start ; i < sw ; i++ ){

            sol[ depth ] = i ;

            for( int j = 0 ; j < bulb ; j++ ){  
                if( state[ j ] == 0 && mat[ i ][ j ] == 1 ){
                    state[ j ] = 1 ;
                    continue ;
                }

                if( state[ j ] == 1 && mat[ i ][ j ] == 1 ){
                    state[ j ] = 0 ;
                    continue ;
                }

            }

            if( is_final( state , bulb ) == 1 ){
                printf( "Sol found:\n" ) ;
                for( int k = 0 ; k < sw ; k++ ){
                    printf( "%d " ,  sol[ k ] ) ;
                }
            }


            permuatate( mat ,  sol , state , sw , bulb , depth + 1 , i + 1 ) ;
            sol[ depth ] = 0 ;

            for( int j = 0 ; j < bulb ; j++ ){
                if( state[ j ] == 1 && mat[ i ][ j ] == 1 ){
                    state[ j ] = 0 ;
                    continue ;
                }
                if( state[ j ] == 0 && mat[ i ][ j ] == 1 ){
                    state[ j ] = 1 ;
                    continue ;
                }
            }
        }

}


void switches( int mat[ SW ][ BULB ] , int sw , int bulb ){

    int *sol = ( int * ) malloc( sw * sizeof( int ) ) ;
    int *state = ( int * ) malloc( bulb * sizeof( int ) ) ;
    
    for( int i = 0 ; i < sw ; i++ ){
        sol[ i ] = 0 ;
    }

    for( int i = 0 ; i < bulb ; i++ ){
        state[ i ] = 0 ;
    }

    permuatate( mat , sol , state , sw , bulb , 0 , 0 ) ;
}

int main( ){

    int mat[ SW ][ BULB ] = { { 1 , 1 , 0 , 0 , 1 } ,
                  { 1 , 0 , 1 , 0 , 0 } ,
                  { 0 , 1 , 1 , 1 , 0 } ,
                  { 1 , 0 , 0 , 1 , 0 } } ;



    switches( mat , SW , BULB ) ;


}