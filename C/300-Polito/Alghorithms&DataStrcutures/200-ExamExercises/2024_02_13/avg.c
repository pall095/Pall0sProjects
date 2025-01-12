#include<stdio.h>
#include<stdlib.h>
#include<math.h>


#define R 3 
#define C 5 

void avg( int matI[ R ][ C ] , float matO[ R ][ C ] ){

    float mean ;
    int num_valid ;
    int r , c ; 

    for( int i = 0 ; i < R ; i++ ){
        for( int j = 0 ; j < C ; j++ ){

            mean = 0 ;
            num_valid = 1 ;
            mean = mean + matI[ i ][ j ] ;

            r = i + 1 ;
            c = j + 1 ;


            while( r < R && c < C ){
                mean = mean + matI[ r ][ c ] ;
                num_valid++ ;
                r++ ;
                c++ ;
            }
            r = i - 1 ;
            c = j - 1 ;

            
            while( r >= 0 && c >= 0 ){

                mean = mean + matI[ r ][ c] ;
                num_valid++ ;
                r-- ;
                c-- ;
            }

            r = i + 1 ;
            c = j - 1 ;

            while( r < R && c >= 0 ){
                mean = mean + matI[ r ][ c] ;
                num_valid++ ;
                r++ ;
                c-- ;
            }

            r = i - 1 ;
            c = j + 1 ;

            while( r >= 0 && c < C ){
                mean = mean + matI[ r ][ c] ;
                num_valid++ ;
                r-- ;
                c++ ;
            }

            printf( "Total valid for %d %d are %d \n" , i , j , num_valid ) ;
            matO[ i ][ j ] = mean / num_valid ;
        }
    }


    for( int i = 0 ; i < R ; i++ ){
        for( int j = 0 ; j < C ; j++ ){
            printf( "%.2f " ,  matO[ i ][ j ] ) ;
        }
        printf( "\n" ) ;
    }
}


void main( ){

    int matI[ R ][ C ] = { { 2 , 3 , 4 , 5 , 0 } ,
                           { 4 , 1 , 7 , 3 , 3 } ,
                           { 2 , 9 , 8 , 1 , 0 } } ;
    
    float matO[ R ][ C ] ;
    avg( matI , matO ) ;
}