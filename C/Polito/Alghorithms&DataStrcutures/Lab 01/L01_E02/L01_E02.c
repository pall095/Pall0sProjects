#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define MAX_ID 4

typedef struct{

    char ID[ MAX_ID + 1 ] ;
    float base_x ;
    float heigth_y ;
    float area ;
    float perimeter ;

} rectangle ;


void read_file( char* , rectangle** , int * ); 
int find_rectangle( rectangle , rectangle* , int ) ;
void print_db( rectangle* , int ) ;
void print_rect( rectangle ) ;
void sort_by( rectangle * , int , int ) ;

int main( ){

    char input_file[ ] = "e02in.txt" ;
    rectangle *rectangle_db ;
    int num_entries ;

    read_file( input_file , &rectangle_db , &num_entries ) ;
    sort_by( rectangle_db , num_entries , 0 ) ;
    print_db( rectangle_db , num_entries ) ;
    sort_by( rectangle_db , num_entries , 1 ) ;
    print_db( rectangle_db , num_entries ) ;
    return 0 ;

}

void sort_by( rectangle *database , int n , int method ){

    int i , j ;
    float max;
    int max_index ;
    float compare_item ;
    rectangle temp_r ;

    if( method == 0){
        printf( "Sorting by Area\n" );

    }

    if( method == 1 ){
        printf( "Sorting by Perimeter!\n" );
    }

    for( i = 0 ; i < n ; i ++ ){
        max = 0 ;
        max_index = 0 ;
        for( j = i ; j < n ; j++ ){

            if( method == 0 ){
                compare_item = (database + j ) -> area ;
            }
            if( method == 1 ){
                compare_item = ( database + j )->perimeter ;
            }

            if( compare_item > max ){
                max = compare_item ;
                max_index = j ;
            }
        }

        temp_r = database[ i ] ;
        database[ i ] = database[ max_index ] ;
        database[ max_index ] = temp_r ;

    }

}



int find_rectangle( rectangle r , rectangle *db , int num ){

    for( int i = 0 ; i < num ; i++ ){

        if( strcmp( r.ID , ( db + i )->ID ) == 0 ){
            printf( "Found %s\n" , r.ID ) ;
            return i ;
        }

    }

    return -1 ;

}

void print_rect( rectangle r ){
    printf( "ID: %s - " , r.ID );
    printf( "Base X: %f - " , r.base_x );
    printf( "Heigth: %f - " , r.heigth_y );
    printf( "Area : %f - " , r.area );
    printf( "Perimeters: %f \n" , r.perimeter );
    return ;
}

void print_db( rectangle* db , int num ){

    for( int i = 0 ; i < num ; i++ ){
        print_rect( *( db + i ) ) ;
    }

}

void read_file( char *file_name , rectangle **rectangle_db , int *num_entries ){

    FILE *fp = fopen( file_name , "r" ) ;
    rectangle temp_rect ;
    int found_index = 0 ;
    int i = 0 ; 
    

    if( fp == NULL ){
        printf( "Unable to open file!\n" ) ;
        return ;
    }

    if( fscanf( fp , "%d" , num_entries ) == EOF ){
        printf( "Worng format for input file!\n" ) ;
        return ;
    }

    *rectangle_db = ( rectangle * )malloc( *num_entries * sizeof( rectangle ) ) ;

    if( *rectangle_db == NULL ){
        printf( "Unable to allocate memory!\n") ;
        return ;
    }

    while( fscanf( fp , "%s %f %f" , temp_rect.ID , &temp_rect.base_x , &temp_rect.heigth_y ) != EOF ){

        temp_rect.area = 0 ;
        temp_rect.perimeter = 0 ;
        found_index = find_rectangle( temp_rect , *rectangle_db , i ) ;

        if( found_index == -1 ){
            *( *rectangle_db + i ) = temp_rect ;
            i ++ ; 
        }else{
            ( *rectangle_db + found_index )->base_x = fabs( ( ( *rectangle_db + found_index )->base_x - temp_rect.base_x ) );
            ( *rectangle_db + found_index )->heigth_y = fabs( ( ( *rectangle_db + found_index )->heigth_y - temp_rect.heigth_y ) );
            ( *rectangle_db + found_index )->area = ( *rectangle_db + found_index )->base_x * ( *rectangle_db + found_index )->heigth_y ;
            ( *rectangle_db + found_index )->perimeter = 2 * ( ( *rectangle_db + found_index )->base_x + ( *rectangle_db + found_index )->heigth_y ) ;
        }

    }

    *num_entries = i ;
    fclose( fp ) ;
    return ; 

}