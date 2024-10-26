#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FLIGHTS 100

typedef struct {

    char id[ 6 ] ;
    char depAir[ 4 ] ;
    char arrAir[ 4 ] ;
    float depTime ;
    float arrTime ;


} flight_t ;

void print_flight( flight_t flight ){

    printf( "%s %s %s %f %f \n" , flight.id , flight.depAir , flight.arrAir , flight.depTime , flight.arrTime ) ;

    }


int read_flights( flight_t *flights , char *filename ){


    FILE *file_ptr ;
    char line[ 100 ] ;
    int nf = 0 ;

    file_ptr = fopen( filename , "r" );

    if( file_ptr == NULL ){
        printf( "Error opening file! \n" ) ;
        return 1 ;
    }

    while( fgets( line , 100 , file_ptr ) != NULL && nf < MAX_FLIGHTS ){

        sscanf( line , "%s%s%s%f%f" ,  flights[ nf ].id , flights[ nf ].depAir , flights[ nf ].arrAir , &flights[ nf ].depTime , &flights[ nf].arrTime ) ;
        nf++;

    }
    fclose( file_ptr ) ;
    return nf ;
}

void find_flights( flight_t *flights , flight_t request , int nf ){


    for( int i = 0 ; i < nf ; i++ ){
        if( strcmp( flights[ i ].depAir , request.depAir ) == 0 && request.depTime <= flights[ i ].depTime ){
            if( strcmp( flights[ i ].arrAir , request.arrAir ) == 0 ){
                printf( "Found a direct connection: \n" );
                print_flight( flights[ i ] );
            }
        else{
            for( int j = 0 ; j < nf ; j++ ){
                if( strcmp( flights[ i ].depAir , flights[ j].depAir ) == 0 && flights[ i ].arrTime <= flights[ j ].depTime ){
                    if( strcasecmp( flights[ j ].arrAir , request.arrAir ) == 0 ){
                        printf( "Found a one flight connection: \n" ) ;
                        print_flight( flights[ i ] ) ;
                        print_flight( flights[ j ] ) ;
                    }
                }
            }


        }


        }


    }





}


int main()
{

    flight_t flights[ MAX_FLIGHTS ] ;
    int nf = 0 ;
    char file_name[] = "flights.txt" ;

    flight_t request = { "NULL" , "TOR" , "PAL" , 16.00 , 00.00 } ;



    nf = read_flights( flights , file_name ) ;
    find_flights( flights , request , nf ) ;



    return 0 ;
}
