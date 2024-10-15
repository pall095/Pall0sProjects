# include<stdio.h>
# include<stdlib.h>
# include<string.h>
# include<math.h>

#define MAX_ID 4 

typedef struct{

    float b ;
    float h ;
    char ID[ MAX_ID + 1 ] ;
    float area ;
    float perimeter ;
} rectangle ;


void read_database( char * , rectangle ** , int * ) ;
void print_reactangle( rectangle ) ;
int find_reactangle( char * , rectangle * , int ) ;
void print_database( rectangle * , int ) ;
void sort_by( rectangle * , int , int ) ;
void save( char * , rectangle * , int ) ;

int main( ){

    char input_file[ ] = "e02in.txt" ;
    char output_area[ ] = "area.txt" ;
    char output_perim[ ] = "perimeter.txt" ;
    rectangle *db ; 
    int db_len ; 
    read_database( input_file , &db , &db_len ) ;
    print_database( db , db_len ) ;
    sort_by( db , db_len , 0 ) ;
    save( output_area , db , db_len ) ;
    print_database( db , db_len ) ;
    sort_by( db , db_len , 1 ) ;
    save( output_perim , db , db_len ) ;
    print_database( db , db_len ) ;
    
}

void save( char *output_file , rectangle *db , int len ){

    FILE *ptr = fopen( output_file , "w" ) ;

    if( ptr == NULL ){
        printf( "Unable to open output file %s\n" , output_file ) ;
    }

    for( int i = 0 ; i < len ; i++ ){
        fprintf( ptr , "ID: %s - Base: %f - Heigth: %f - Area: %f - Perimeter: %f \n" , db[ i ].ID , db[ i ].b , db[ i ].h , db[ i ].area , db[ i ].perimeter ) ; 
    }

    fclose( ptr ) ;
    return ;


}

void sort_by( rectangle *db , int len , int method ){

    rectangle temp_rect ;
    int i , j ; 
    float current_max = 0 ;
    int max_index = 0 ;
    float compare_item ;

    if( method == 0 ){
        printf( "Sorting by area!\n" ) ;
    }

    if( method == 1 ){
        printf( "Sorting by perimeter!\n" ) ;
    }

    for( i = 0 ; i < len ; i++ ){

        current_max = 0 ;
        max_index = 0 ;

        for( j = i ; j < len ; j++ ){

            if( method == 0 ){
                compare_item = db[ j ].area ;
            }

            if( method == 1 ){
                compare_item = db[ j ].perimeter ;
            }

            if( compare_item > current_max ){
                current_max = compare_item ;
                max_index = j ;
            }
        }

        temp_rect = db[ i ] ;
        db[ i ] = db[ max_index ] ;
        db[ max_index ] = temp_rect ;
    }


}

void print_database( rectangle *db , int len ){
    for( int i = 0 ; i < len ; i++ ){
        print_reactangle( db[ i ] ) ;
    }
}

void read_database( char *input_file , rectangle **db , int *len ){

    FILE *ptr = fopen( input_file , "r" ) ;
    int i = 0 ;
    char curr_id[ MAX_ID + 1 ] ;
    float curr_x , curr_y ;

    if( ptr == NULL ){
        printf( "Unable to open input file!\n" ) ;
        return ;
    }

    if( fscanf( ptr , "%d" , len ) == EOF ){
        printf( "Input file not in the correct format!\n" ) ;
        return ;
    }

    *db = ( rectangle *) malloc( *len * sizeof( rectangle ) ) ;
    if( *db == NULL ){
        printf( "Unable to allocate memory!\n" ) ;
        return ;
    }

    int found_index = -1 ;

    while( fscanf( ptr , "%s %f %f" , curr_id , &curr_x , &curr_y ) != EOF ){
        
        
        found_index = find_reactangle( curr_id , *db , i ) ;
        if( found_index == -1 ){

            strcpy( ( *db + i )->ID , curr_id );
            (*db + i )->b = curr_x ;
            (*db + i )->h = curr_y ;
            (*db + i )->area = 0 ;
            (*db + i )->perimeter = 0 ;
            i++ ;
        }else{

            ( *db + found_index )->b = fabs( (*db + found_index )->b - curr_x ) ;
            ( *db + found_index )->h = fabs( (*db + found_index )->h - curr_y ) ;
            (*db + found_index )->area = (*db + found_index )->b * (*db + found_index )->h ;
            (*db + found_index )->perimeter= 2 * ( (*db + found_index )->b + (*db + found_index )->h ) ;
        }

    }
    
    *len = i ;
    fclose( ptr ) ;
    return ;

}

int find_reactangle( char *ID , rectangle *db , int len ){

    for( int i = 0 ; i < len ; i++ ){

        if( strcmp( ID , db[ i ].ID ) == 0 ){
            return i ;
        }
    }

    return -1 ;

}

void print_reactangle( rectangle r ){

    printf( "ID: %s - Base: %f - Heigth: %f - Area: %f - Perimeter: %f \n" , r.ID , r.b , r.h , r.area , r.perimeter ) ;
    return ;

}