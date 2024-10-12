#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD_LENGTH   20
#define MAX_WORD_NUMBER  100



typedef struct{

    char word[ MAX_WORD_LENGTH + 1 ] ;
    int occurrence ;

} word_data ;

void read_text( char * , word_data * , int ) ;
word_data *read_words( char * , int * ) ;
void print_database( word_data * , int ) ;
int compare( char * , char * ) ;


int main( ){

    char input_file_text[ ] = "e01inA.txt" ;
    char input_file_word[ ] = "e01inB.txt" ;
    word_data *word_db ;
    int num_words ;

    word_db = read_words( input_file_word , &num_words );
    read_text( input_file_text , word_db , num_words ) ;
    print_database( word_db , num_words ) ;

    free( word_db ) ;

    return 0 ;
    

}

int compare( char *w , char *reference_word ){

    if( strlen( w ) != strlen( reference_word ) ){
        return 0 ;
    }

    int i = 0 ;

    for( i =0 ; i < strlen( reference_word ) ; i++ ){
        if( tolower( w[ i ] ) != tolower( reference_word[ i ] ) ){
            return 0 ;
        } 
    }

    return 1 ;

}

void print_database( word_data *word_db , int num_entries ){

    int i = 0 ;
    for( i = 0 ; i < num_entries ; i++ ){
        printf( "Word: %s - Occurrence: %d \n" , ( word_db + i )->word , ( word_db + i )->occurrence ) ;
    }
    return ;
}

void read_text( char *filename , word_data* word_db , int num_entries ){

    FILE *fp = fopen( filename , "r" );
    char curr_word[ MAX_WORD_LENGTH + 1 ] ; 
    int i ; 

    if( fp == NULL ){
        printf( "Unable to open text file! \n" );
        return ;
    }

    while( fscanf( fp , "%s" , curr_word ) != EOF ){

        for( i = 0 ; i < num_entries ; i++ ){
            if( compare( ( word_db + i )->word , curr_word ) == 1 ){
                word_db[ i ].occurrence++  ;
            }
        }

    }

    return ;

}

word_data *read_words( char *input_file , int *num_entries ){

    FILE *file_ptr = fopen( input_file , "r" );
    word_data *word_database ;
    int i = 0 ;

    if( file_ptr == NULL ){
        printf( "Unable to open file!" ) ;
        return word_database ;
    }

    if( fscanf( file_ptr , "%d" , num_entries ) == EOF ){
        printf( "Error reading the number of data!\n" );
    }

    word_database = ( word_data * ) malloc( *num_entries * sizeof( word_data ) ) ;

    if( word_database == NULL ){
        printf( "Memory not avilable! \n" ) ;
    }

    while( fscanf( file_ptr , "%s" , ( word_database + i)->word )!= EOF ){
        ( word_database + i )->occurrence = 0 ;
        i++ ;
    }
    *num_entries = i ;

    fclose( file_ptr );
    return word_database ;

} 