#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <ctype.h>

#define MAX_WORD 1001

typedef struct list_s{

    int occurence ;
    char word[ MAX_WORD ] ;
    struct list_s* next ;

} word_t ;


word_t* read_file( word_t* , char* ) ;
word_t* new_element( void ) ;
word_t* insert_head( word_t* , word_t* ) ;
void print_list( word_t* ) ;
int find( word_t* , char* ) ;
int compare( char* , char* ) ;

void main( int argc , char **argv ){

    word_t* list_head = NULL ;
    list_head = read_file( list_head , argv[ 1 ] ) ;
    print_list( list_head );
    
}


word_t* read_file( word_t *head , char *file_name ){

    FILE *ptr = fopen( file_name , "r" ) ;
    char word[ MAX_WORD ] ;
    word_t *new_word ;   

    if( ptr == NULL ){
        printf( "Unable to open input file! \n" ) ;
        return head;
    }

    while( fscanf( ptr , "%s" ,  word ) != EOF) {

        if( head == NULL ){
            new_word = new_element( );
            new_word->occurence = 0 ;
            strcpy( new_word->word , word ) ; 
            head = insert_head( head , new_word ) ;
        }

        if( find( head , word ) == 0 && head != NULL ){
            new_word = new_element( ) ;
            new_word->occurence = 1  ;
            strcpy( new_word->word , word ) ; 
            head = insert_head( head , new_word ) ;
        }

    }
    
    return head ;
}

word_t* new_element( void ){
    word_t* ptr ;
    ptr = ( word_t* ) malloc( sizeof( word_t ) ) ;
    if( ptr == NULL ){
        printf( "Unable to allocate memory!\n" ) ;
    }
    return ptr ;
} 

word_t* insert_head( word_t *head , word_t* new_head ){
    new_head->next = head ;
    return new_head ;
}

void print_list( word_t* head ){
    while( head != NULL ){
        printf( "W : %s - Occ: %d --> " , head->word , head->occurence ) ;
        head = head->next ;
    }
    printf( "\n" ) ;
}

int find( word_t *head , char* word ){

    while( head != NULL ){
        if( compare( head->word , word ) == 1 ){
            head->occurence = head->occurence +  1 ;
            return 1 ;
        }
        head = head->next ;
    }
    return 0 ;
}

int compare( char *w1 , char *w2 ){

    if( strlen( w1 ) != strlen( w2 ) ){
        return 0 ;
    }
    for( int i = 0 ; i < strlen( w1 ) ; i++ ){

        if( tolower( w1[ i ] ) != tolower( w2[ i ] ) ){
            return 0 ;
        }
    }
    return 1 ;
}
