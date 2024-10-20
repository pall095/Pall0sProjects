#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 100
#define MAX_ID 4

typedef struct{

    char ID[ MAX_ID + 1 ] ;
    float base_x ;
    float height_y ;
    float area ;
    float perimeter ;


} rectangle ;

void read_file( char * , rectangle * , int * ) ;
void print_rect( rectangle ) ;
int find_reactangle( rectangle * , rectangle , int ) ;
void print_database( rectangle * ,  int ) ;
void sort_by( rectangle * , int , int ) ;
void save_output( char * , rectangle * , int n ) ;


int main()
{
    char file_name[ ] = "rect.txt" ;
    char output_area[ ] = "sorted_area.txt" ;
    char output_perim[ ] = "sorted_perim.txt" ;
    rectangle rectangle_db[ MAX_ROWS ] ;
    int num_rectangle = 0 ;
    read_file( file_name , rectangle_db , &num_rectangle ) ;
    sort_by( rectangle_db , num_rectangle , 0 ) ;
    print_database( rectangle_db , num_rectangle ) ;
    save_output( output_area , rectangle_db , num_rectangle ) ;
    sort_by( rectangle_db , num_rectangle , 1 ) ;
    print_database( rectangle_db , num_rectangle ) ;
    save_output( output_area , rectangle_db , num_rectangle ) ;

}

// Saving output.
void save_output( char *filename , rectangle *database , int n ){

    FILE *ptr = fopen( filename , "w" ) ;
    int i = 0 ;

    if( ptr == NULL ){
        printf( "Unable to open output file %s!\n" , filename ) ;
        return ; 
    }

    for( i = 0 ; i < n ; i++ ){
        fprintf( ptr , "ID: %s - Area: %f - Perimeter: %f \n" , ( database + i )->ID , ( database + i )->area , ( database + i )->perimeter ) ;
    }

    fclose( ptr );
    return ; 



}

// Sorts in place the rectangle database by a given method.
// Enum:
// 0 = Sort by area.
// 1 = Sort by perimeter.
// Database is passed by reference therefore no need to return it (modified in place).
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

// Reads the input file. 
// Already implements logic to pupulate the struct correctly.
// If it is the first time a rectangle has been seen, it adds it to the database and initialize base and heigth to the cooridantes.
// If a rectangle has already been seen updates base and heigth given the second coordinates and calculates area and perimeter.
void read_file( char *file_name , rectangle *database , int *num_rectangle ){

    FILE *file_ptr = fopen( file_name , "r" ) ;
    rectangle temp_rect ;
    int found_index = 0 ;
    float dx , dy ;

    
    if( file_ptr == NULL ){
        printf( "Unable to read file %s!\n" , file_name );
        return ;
    }
    

    while( fscanf( file_ptr , "%s  %f %f" , temp_rect.ID , &temp_rect.base_x , &temp_rect.height_y ) != EOF ){

        found_index = find_reactangle( database , temp_rect , *num_rectangle ) ;
        if( found_index == -1 ){
            database[ *num_rectangle ] = temp_rect ;
            *num_rectangle = *num_rectangle + 1 ;
        } else{

            dx = database[ found_index ].base_x - temp_rect.base_x ;
            dy = database[ found_index ].height_y - temp_rect.height_y ;
            if( dx < 0 ){
                database[ found_index ].base_x = -dx ;
            }else{
                database[ found_index ].base_x = dx ;
            }
            if( dy < 0 ){
                database[ found_index ].height_y = -dy ;
            }else{
                database[ found_index ].height_y = dy ;
            }

            database[ found_index ].area = database[ found_index ].base_x *  database[ found_index ].height_y ;
            database[ found_index ].perimeter = 2 * ( database[ found_index ].base_x + database[ found_index ].height_y ) ;
        }
    }

    fclose( file_ptr );
    return ;


}

// Helper function to print a single rectangle field.
void print_rect( rectangle r ){
    printf( "ID: %s - " , r.ID );
    printf( "Base X: %f - " , r.base_x );
    printf( "Heigth: %f - " , r.height_y );
    printf( "Area : %f - " , r.area );
    printf( "Perimeters: %f \n" , r.perimeter );
    return ;
}

// Helper function to print to standard output the database.
void print_database( rectangle *database , int n ){

    int i = 0 ;
    for( i = 0 ; i < n ; i ++ ){
        print_rect( *( database + i ) ) ;
    }

}

// Finds a rectangle, by ID, in the database.
// If founds, return the index.
// If not found returns -1.
int find_reactangle( rectangle *database , rectangle r , int num_rectangle ){

    int found = - 1 ;
    int i = 0 ;

    for( i = 0 ; i < num_rectangle ; i++){
        if( strcmp( ( database + i )->ID , r.ID ) == 0 ) {
            return i ;
        }
    }
    return found ;
}
