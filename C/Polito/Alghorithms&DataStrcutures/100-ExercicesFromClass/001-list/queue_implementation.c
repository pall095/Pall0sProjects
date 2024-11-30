#include <stdio.h>
#include <stdlib.h>

typedef struct list_s{

    int key ;
    struct list_s* next ;
} list_t ;


list_t* read_from_file( char* ) ;
list_t* enqueue( list_t* , int ) ;
list_t* new_element( void ) ;
list_t* dequeue( list_t* , int* ) ;
void print_list( list_t* ) ; 

void main( int arcg , char **argv ){
    list_t* tail = NULL ;
    int tmp ;
    tail = read_from_file( argv[ 1 ] ) ;
    print_list( tail ) ; 
    tail = dequeue( tail , &tmp ) ;
    printf( "Dequeued value: %d\n" , tmp ) ;
    print_list( tail ) ;
}


list_t* read_from_file( char *filename ){

    FILE *fp = fopen( filename , "r" ) ;
    int key ;
    list_t* tail = NULL ; 

    if( fp == NULL ){
        printf( "Unable to read the file! \n" ) ;
    }

    while( fscanf( fp , "%d" , &key ) != EOF){
        tail = enqueue( tail , key ) ;
    } 

    return tail ;

}

list_t* dequeue( list_t* tail , int *val ){

    list_t* head = tail->next ;
    *val = head->key ;

    if( head == tail ){
        free( tail ) ;
        return NULL ;
    }else{
        tail->next = head->next ;
        free( head ) ;
    }
    
    return tail ;

}

list_t* enqueue( list_t* tail , int key ){

    list_t* new  = new_element( ) ;
    new->key = key ;

    if( tail == NULL ){
        tail = new ;
        tail->next = tail ;
    }else{
        new->next = tail->next ;
        tail->next = new ;
        tail = new ;
    }

    return tail;
}

list_t* new_element( void ){

    list_t* p = NULL ;
    p = ( list_t* ) malloc( sizeof( list_t ) ) ;
    if( p == NULL ){
        printf( "Unable to allocate memory! \n" ) ;
        return NULL ;
    }
    return p ;
}

void print_list( list_t* tail ){
    int cnt = 1 ;
    list_t* p = tail->next ;

    while( p != tail ){
        printf( " %d --> " , p->key );
        cnt++ ;
        p = p -> next ;
    }

    printf( " %d\n" , p->key );

}




