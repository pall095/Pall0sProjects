#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD_LENGTH 20
#define MAX_NUM_WORD 100
#define MAX_LINE_LENGTH  100



typedef struct{
    char word[ MAX_WORD_LENGTH + 1 ] ;
    int occurrence ;
} word_data ;

void read_word_list( char *file_path , word_data *database , int *n , bool verbose ){

    FILE *file_ptr = fopen( file_path , "r");
    int total_words = 0 ;

    if( file_ptr == NULL ){
        printf( "Unable to open file!" );
        return ;
    }

    while( fscanf( file_ptr , "%s" , ( database + total_words )->word  ) != EOF ){
        ( database + total_words )->occurrence = 0 ;

        if( verbose ){
                printf( "%s\n" , ( database + total_words )->word )  ;
        }
        total_words++ ;
    }
    *n = total_words ;
    return ;


}

void read_text( char *text_file_path , word_data *database , int *database_length , bool verbose ){

    FILE *file_ptr = fopen( text_file_path , "r" );
    char word[ MAX_LINE_LENGTH + 1 ] ;
    int j = 0 ;

    if( file_ptr == NULL ){
        printf( "Unable to open file!" ) ;
        return ;
    }

    while( fscanf( file_ptr , "%s" , word ) != EOF ){

        if( verbose ){
            printf( "%s \n" , word ) ;
        }
        for( j = 0 ; j < database_length ; j++ ){
            if( compare( word , ( database + j )->word ) == 1 ){
                (database + j)->occurrence++ ;
            }
        }
    }
    return ;
}

int compare( char *word_in_file , char *word_in_database ){

    if( strlen( word_in_file ) != strlen( word_in_database) ){
        return 0 ;
    }

    for( int i = 0 ; i < strlen( word_in_database) ; i++ ){
        if( tolower( word_in_database[ i ] ) != tolower( word_in_file[ i ] ) ){
            return 0 ;
           }
    }
    return 1 ;
}

void print_occuerences( word_data *database , int database_length ){
    for( int i = 0 ; i < database_length ; i++ ){
        printf( "Word: %s - Occurence: %d \n" , (database + i )->word , (database + i )->occurrence  ) ;
    }
}

int main()
{
    char text_file_path[ ] = "e01inA.txt" ;
    char word_file_path[ ] = "e01inB.txt" ;

    word_data word_database[ MAX_NUM_WORD ] ;
    int database_length = 0 ;

    read_word_list( word_file_path , word_database , &database_length , false ) ;
    read_text( text_file_path , word_database , database_length , false ) ;
    print_occuerences( word_database , database_length ) ;


    return 0 ;
}
