#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

#define MAX_NUM 5 

typedef struct list_s{
    int val ;
    struct list_s* next ;
} list_t ;


list_t* new_element( int val ){
    list_t* ptr = ( list_t* ) malloc( sizeof( list_t ) ) ;
    ptr->val = val ;
    ptr->next = NULL ;
}

list_t* insert( list_t* head , list_t* new ){
    new->next = head ;
    head = new ;
    return head ;
}

void print_sol( int *sol , int n ){
    for( int i = 0 ; i < n ; i++ ){
        printf( "%d" , sol[ i ] ) ;
    }
    printf( "\n" ) ;
}

int is_valid( int *sol , int n ){
    int odd_sum = 0 ;
    int even_sum = 0 ;
    for( int i = 0 ; i < n ; i++ ){
        if( i%2 == 0 ){
            even_sum = even_sum + sol[ i ] ;
        }else{
            odd_sum = odd_sum + sol[ i ] ;
        }
    }
    if( odd_sum == even_sum ){
        return 1 ;
    }
    return 0 ;
}

void mult_princ( int even[ MAX_NUM ] , int odd[ MAX_NUM ] ,  int *sol , list_t **generated , int n , int depth ){
    if( depth >= n ){
        if( is_valid( sol , n ) ){
            int num = 0 ;
            for( int i = 0 ; i < n ; i++ ){
                num = num + sol[ i ] * pow( 10 , i );
            }
            *generated = insert( *generated , new_element( num ) ) ;
        } 
        return ;
    }
    for( int i = 0 ; i < MAX_NUM ; i++ ){
        if( depth%2 == 0 ){
            sol[ depth ] = even[ i ] ;
            mult_princ( even , odd , sol , generated , n , depth + 1 ) ;
        }else{
            sol[ depth ] = odd[ i ] ;
            mult_princ( even , odd , sol , generated , n , depth + 1 ) ;
        }
    }
}

void generate( char *name , int n ){
    int even[ ] = { 0 , 2 , 4 , 6 , 8 } ;
    int odd[ ] = { 1 , 3 , 5 , 7 , 9 } ;
    list_t *generated = NULL ;
    int *sol = ( int * ) malloc( n * sizeof( int ) ) ;

    mult_princ( even , odd , sol , &generated , n , 0 ) ;

    FILE *ptr = fopen( name , "w" ) ;

    while( generated != NULL ){
        fprintf( ptr , "%d \n" , generated->val ) ;
        generated =generated->next ;
    } 
    fclose( ptr ) ;
}

void main( ){
    int n = 4 ;
    generate( "otuput.txt" , n ) ;
}

