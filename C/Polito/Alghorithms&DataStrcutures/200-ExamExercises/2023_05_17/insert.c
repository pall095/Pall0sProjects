#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

#define MAX_CHAR 100 

typedef struct list_s2{
    int key ;
    int row ;
    struct list_s2 *next ;
} list_t2 ;

typedef struct list_s1{
    char key[ MAX_CHAR + 1 ] ;
    list_t2 *head ;
    struct list_s1 *next ;
} list_t1 ;



list_t1* new_main( ){

    list_t1 *ptr = ( list_t1 *) malloc( sizeof( list_t1 ) ) ;
    ptr->head = new_sub( ) ;
    return ptr ;
}

list_t2* new_sub( ){
    return ( list_t2 *) malloc( sizeof( list_t2 ) ) ;
}

int in_main( list_t1 *head , char *key ){

    while( head != NULL ){

        if( strcmp( head->key , key ) != 0 ){
            return 0 ;
        }
    }
    return 1 ;
}

list_t1* insert( char *filename ){

    FILE *ptr = fopen( filename , "r" ) ;
    char curr_key[ MAX_CHAR + 1 ] ;
    int curr_int ; 

    list_t1 main_head = new_main( ) ;
    main_head = NULL ;


    while( fscanf( ptr , "%s %d" , curr_key , &curr_int ) != EOF ){




    }



}