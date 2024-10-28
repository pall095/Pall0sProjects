#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD 20 

typedef struct list_s{
    char word[ MAX_WORD + 1 ] ;
    int occurrence ;
    struct list_s* next ;
} word ;


word* read_database( char* ) ;
word* new_word( char* ) ;
word* append( word* , char* ) ;
int compare( char* , char* ) ;
void find_and_update( word* , char* ) ;
void read_text( word* , char* ) ;
void print_db( word* ) ;


void main( int argc , char **argv ){

    word* db = read_database( argv[ 1 ] ) ; 
    print_db( db ) ;
    read_text( db , argv[ 2 ] ) ;
    printf( "--------\n" ) ;
    print_db( db ) ;

}

void read_text( word* db_tail , char *filename ){

    FILE *fp = fopen( filename , "r" ) ;

    if( fp == NULL ){
        printf( "Unable to open text file!\n" ) ;
        return ;
    }

    char current_word[ MAX_WORD + 1 ] ;
    word* found_p = NULL ;

    while( fscanf( fp , "%s" , current_word ) != EOF ){
        find_and_update( db_tail , current_word ) ;
    }

}

void find_and_update( word* db_tail , char *w ){

    word *p = db_tail -> next ;

    while( p != db_tail ){

        if( compare(  p->word , w ) == 1 ){
            p->occurrence++;
        }
        p = p->next ;
    }

    if( compare(  p->word , w ) == 1 ){
        db_tail->occurrence++ ;
    }
}

void print_db( word* tail ){
    if( tail == NULL ){
        printf( "Nothing to print!\n " );
        return ;
    }
    word* head = tail->next ;
    while( head != tail ){
        printf( "W: %s O: %d --> " , head->word , head->occurrence ) ;
        head = head -> next ;
    }
    printf( "W: %s O: %d \n" , tail->word , tail->occurrence ) ;
    return ;
}

word* read_database( char* db_file ){
    FILE *fp = fopen( db_file , "r" ) ;
    char current_word[ MAX_WORD + 1 ] ; 
    word* tail = NULL ;
    if( fp == NULL ){
        printf( "Unable to open file!\n" ) ;
        return NULL ;
    }
    while( fscanf( fp ,  "%s" , current_word ) != EOF ){
        tail = append( tail , current_word ) ;
    }
    return tail ;
}

word* append( word* tail , char* w ){
    word* new = new_word( w ) ;
    if( tail == NULL ){
        tail = new ;
        tail->next = tail ;
    }else{
        new->next = tail->next ;
        tail->next = new ;
        tail = new ;
    }
    return tail ;
}


word* new_word( char* input_word ){
    word *word_p = NULL ;
    word_p = ( word* ) malloc( sizeof( word ) ) ;
    if( word_p == NULL ){
        printf( "Unable to allocate memory!\n" ) ;
        return NULL ;    
    }
    word_p -> occurrence = 0 ;
    strcpy( word_p -> word , input_word ) ;
}


int compare( char* db_word , char* w ){

    if( strlen( db_word ) != strlen( w ) ){
        return 0 ;
    }

    for( int i = 0 ; i < strlen( db_word ) ; i++ ){

        if( tolower( db_word[ i ] ) != tolower( w[ i ] ) ){
            return 0 ;
        }
    }

    return 1 ; 
}

