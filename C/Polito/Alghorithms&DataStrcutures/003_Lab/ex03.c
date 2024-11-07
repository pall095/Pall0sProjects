#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>

#define MAX 21

typedef struct list_t{

    char product_name[ MAX ] ;
    int price ;
    struct list_t* next ; 

} product ;

typedef struct list_s{

    char name[ MAX ] ;
    char ID[ MAX ] ;
    struct list_s* next ;
    product* product_head ;

} producer ;

producer* read_producer( producer* , char* ) ;
producer* new_producer( void ) ;
producer* insert_producer_head( producer* , producer* ) ;
product* insert_product_head( product* , product* ) ;
product* new_product( void ) ;
void read_product( producer* , char* ) ;
void print_producer( producer* ) ;
void print_product( product* ) ;

void main( int argc , char **argv ){

    producer* producer_head = NULL ;
    producer_head = read_producer( producer_head , argv[ 1 ] ) ;
    read_product( producer_head , argv[ 2 ] ) ;
    print_producer( producer_head ) ;
}

producer* read_producer( producer *producer_head , char *filename ){

    FILE *ptr = fopen( filename , "r" ) ;

    if( ptr == NULL ){
        printf( "Unable to open producer file!\n" ) ;
        return NULL ;
    }

    char current_producer_name[ MAX ];
    char current_producer_id[ MAX ] ;
    producer* current_producer ;

    while( fscanf( ptr , "%s %s" ,  current_producer_name , current_producer_id ) != EOF ){
        current_producer = new_producer( ) ;
        strcpy( current_producer->name , current_producer_name ) ;
        strcpy( current_producer->ID , current_producer_id ) ;
        current_producer->product_head = NULL ;
        producer_head = insert_producer_head( producer_head , current_producer ) ;
    }

    fclose( ptr ) ;
    return producer_head ;
}

producer* new_producer( void ){
    producer* p ;
    p = ( producer* ) malloc( sizeof( producer ) ) ;
    if( p == NULL ){
        printf( "Unable to allocate memory for producer!\n" ) ;
        return NULL ;
    }
    return p; 
}

producer* insert_producer_head( producer* head , producer* new ){
    new->next = head ;
    return new ;
}

void print_producer( producer *p ){

    while( p != NULL ){
        printf( "Producer Name: %s - Prodcuer ID: %s \n" , p->name , p->ID ) ;
        print_product( p->product_head ) ;
        p = p->next ;
    }
    return ;
}

void read_product( producer *producer_head , char *product_filename ){

    FILE *ptr = fopen( product_filename , "r" ) ;
    producer* producer_p = producer_head ;

    if( ptr == NULL ){
        printf( "Unable to open product filname!\n" ) ;
        return ;
    }

    char current_id[ MAX ] ;
    char current_product_name[ MAX ] ;
    int current_price ;
    product* current_product ;

    while( fscanf( ptr , "%s %s %d" ,  current_id ,  current_product_name , &current_price ) != EOF ){

        while( producer_p != NULL ){

            if( strcmp( producer_p->ID , current_id ) == 0 ){

                current_product = new_product( ) ;
                strcpy( current_product->product_name , current_product_name ) ;
                current_product->price = current_price ;
                producer_p->product_head = insert_product_head( producer_p->product_head , current_product ) ;
                producer_p = producer_head ;
                break ;
            }

            producer_p = producer_p->next ;
        }
    }
}

product* insert_product_head( product *product_head , product *new ){
    new->next = product_head ;
    return new ;
}

product* new_product( void ){

    product* p ;
    p = ( product* ) malloc( sizeof( product ) ) ;

    if( p == NULL ){
        printf( "Unable to allocate memory for product!\n" ) ;
        return NULL ;
    }

    return p ;

}

void print_product( product *p ){

    while( p != NULL ){
        printf( "Product Name: %s - Price: %d \n" , p->product_name , p->price ) ;
        p = p->next ;
    }

}