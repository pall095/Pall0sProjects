#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define MAX_NAME 30 

typedef struct{

    char name[ MAX_NAME + 1 ] ;
    int ID ;
    int num_lamps ;
    float *lap_times ;
    float avg ;

} cyclist ;


cyclist* read_file( char * , cyclist* , int * ) ;
void print_athlets( cyclist* , int ) ;
void search_by_name( char * , cyclist * , int ) ;
void print_best( cyclist* , int ) ;


int main( ){

    char file_name[ ] = "e03in.txt" ;
    cyclist *database ;
    int num_entries ;
    database = read_file( file_name , database , &num_entries ) ;

    print_athlets( database , num_entries ) ;
    search_by_name( "Neri" , database , num_entries ) ;
    print_best( database , num_entries ) ;

    for( int i = 0 ; i < num_entries ; i++ ){
        free( database[ i ].lap_times ) ;
    }
    
    free( database ) ;
    return 0 ;

}

void print_best( cyclist *db , int num_entries ){

    int i = 0 ;
    float tmp_min = db[ i ].avg ;
    int min_index = 0 ; 

    for( i = 0 ; i < num_entries ; i++ ){

        if( db[ i ].avg < tmp_min ){
            tmp_min = db[ i ].avg ;
            min_index = i ;
        }

    }

    search_by_name( db[ min_index ].name , db , num_entries ) ;

}

void print_athlets( cyclist *db , int num_entries ){

    int i = 0 ;

    printf( "Number of athlets: %d\n" , num_entries) ;

    for( i = 0 ; i < num_entries ; i++ ){
        printf( "Name: %s - ID: %d - Num Laps: %d \n" , db[ i].name , db[ i ].ID , db[ i ].num_lamps ) ;
    }

    return ;

}


void search_by_name( char *query_name , cyclist *db , int num_entries ){

    for( int i = 0 ; i < num_entries ; i++ ){

        if( strcmp( query_name , db[ i ].name ) == 0 ){

            printf( "Name: %s - ID: %d - Num Laps: %d - Avg: %f\n" , db[ i].name , db[ i ].ID , db[ i ].num_lamps ,db[ i ].avg ) ;

            for( int j = 0 ; j < db[ i ].num_lamps ; j++ ){
                printf( "Lap %d : %f\n" , j , db[ i ].lap_times[ j ] );
                
            }


            break ;

        }

    }


}

cyclist* read_file( char *filename , cyclist *db , int *num_entries ){

    FILE *fp = fopen( filename , "r" );
    int i = 0 ;

    if( fp == NULL ){
        printf( "Unable to open source file\n" ) ;
        return db;
    }

    if( fscanf( fp , "%d" , num_entries) == EOF ){
        printf( "File format not correct\n" ) ;
        return db;
    }

    db = ( cyclist * ) malloc( *num_entries * sizeof( cyclist ) ) ;

    if( db == NULL ){
        printf( "Unable to allocate memory! \n" );
        return db;
    }

    while( fscanf( fp , "%s %d %d" , db[ i ].name , &db[ i ].ID , &db[ i ].num_lamps ) != EOF ){

        db[ i ].lap_times = (float * ) malloc( db[ i ].num_lamps *sizeof( float ) ) ;

        if( db[ i ].lap_times == NULL ){
            printf( "Unable to allocate memory for laps!\n" );
            return db; 
        }

        db[ i ].avg = 0 ;

        for( int j = 0 ; j < db[ i ].num_lamps ; j++ ){

            fscanf( fp , "%f" , &db[ i ].lap_times[ j ] ) ;
            db[ i ].avg = db[ i ].avg + db[ i ].lap_times[ j ] ;
        }

        db[ i ].avg = db[ i ].avg / db[ i ].num_lamps ;
        i++ ;

    }

    *num_entries = i ;

    fclose( fp ) ;
    return db ; 


}