#include <stdio.h>
#include <stdlib.h>
#include <string.h> 


#define NUM_ELEMENTS 10
#define COMMAND_LENGTH 10 

typedef struct list_s{

    int key ;
    struct list_s *next ;

} list_t ;

list_t* new_element( ) ;
list_t* push( list_t* , int  ) ;
list_t* pop( list_t* , int* ) ;
list_t* read_from_file( char* ) ;
list_t* find( list_t* , int ) ;
list_t* sort( list_t** ) ;
int is_empty( list_t* ) ;
int find_max( list_t* ) ;
void remove_key( list_t** , int , int ) ;
void print_list( list_t* ) ;


void main( int argc , char **argv ){

    list_t *head = NULL ;
    int STATUS ;
    char command[ COMMAND_LENGTH + 1 ] ;
    int new_value , extracted_value ;

    if( argc < 2 ){
        printf( "Not enough input arguments!" ) ;
        return ;
    }
    head = read_from_file( argv[ 1 ] ) ;
    while( strcmp( command , "stop" ) != 0 ){

        printf( "-------------------------------\n") ;
        printf( "-- COMMAND LIST -- \n" ) ;
        printf( "\n- rm = remove element \n" ) ;
        printf( "- print = print list \n"  ) ;
        printf( "- max = find maximum \n" ) ;
        printf( "- empty = check empty \n" ) ;
        printf( "- sort = sort list \n" ) ;
        printf( "- pop = pop head \n" ) ;
        printf( "- push = push to head \n") ;
        printf( "\nInput a command: " ) ;
        scanf( "%s" , command ) ;

        if( strcmp( command , "rm" ) == 0 ){
            printf( "Input the number to remove: " ) ;
            scanf( "%d" ,  &new_value ) ;
            remove_key( &head , new_value , 1 ) ;
            continue ;
        }

        if( strcmp( command , "print" ) == 0 ){
            print_list( head ) ;
            continue ;
        }
        if( strcmp( command , "max" ) == 0 ){
            printf( "Current max in the list is: %d\n" , find_max( head ) ) ;
            continue ;
        }
        if( strcmp( command , "sort" ) == 0 ){
            head = sort( &head ) ;
            continue ;
        }
        if( strcmp( command , "empty" ) == 0  ){
            
            if( is_empty( head ) == 1 ){
                printf( "List is empty!\n" ) ;
            }else{
                printf( "List is not empty!\n" ) ;
            }
            continue ;
        }

        if( strcmp( command , "push" ) == 0 ){
            printf( "Inser thte value to push: " ) ;
            scanf( "%d" ,  &new_value ) ;
            head = push( head , new_value ) ;
            continue ;
        }

        if( strcmp( command , "pop" ) == 0){
            int extracted_value ;
            head = pop( head , &extracted_value ) ;
            continue ;
        }
    }
}

list_t* new_element( ){
    list_t *ptr ;
    ptr = ( list_t* ) malloc( sizeof( list_t ) ) ;

    if( ptr == NULL ){
        printf( "Memory cannot be allocated for the new element!\n") ;
        return NULL ;
    }
    return ptr ;
}

list_t* sort( list_t **head ){

    list_t *new_head = NULL ;
    int current_max ;

    while( is_empty( *head ) == 0 ){
        current_max = find_max( *head ) ;
        remove_key( head , current_max , 0 ) ;
        new_head = push( new_head , current_max ) ;
    }
    return new_head ;
}

int is_empty( list_t* head ){
    if( head == NULL ){
        return 1 ;
    }
    return 0 ;
}

int find_max( list_t* head ){
    int max = 0 ;
    while( head != NULL ){

        if( head->key > max ){
            max = head->key ;
        }
        head = head->next ;
    }
    return max ; 
}

void remove_key( list_t **head , int k  , int verbose ){
    
    list_t *q = *head ;
    list_t *traversing_p = *head ;

    while( traversing_p != NULL ){
        if( traversing_p->key == k ){
            if( q == traversing_p ){
                (*head) = q->next ; 
            }else{
                q->next = traversing_p->next ;
            }
            if( verbose == 1 ){
                printf( "Remotion of key %d OK!\n" , k ) ;
            }
            return ;
        }else{
            q = traversing_p ;
            traversing_p = traversing_p->next ;
        }
    }
    if( verbose == 1){
        printf( "Remotion of key %d KO - Element not found!\n" , k ) ;
    }
}

list_t* find( list_t *p , int key ){

    printf( "Looking for %d...\n" , key ) ;
    while( p != NULL ){
        if( p->key == key ){
            printf( "Found!\n" ) ;
            return p;
        }else{
            p = p->next ;
        }
    }
    printf("Key not present!\n") ;
    return NULL ;
}

list_t* read_from_file( char* filename ){
    list_t *head = NULL ;
    int current_key ;
    FILE *file_p = fopen( filename , "r" ) ;

    if( file_p == NULL ){
        printf("Unable to open file!" ) ;
        return head ;
    }
    while( fscanf( file_p , "%d" , &current_key ) != EOF ){
        head = push( head , current_key ) ;
    }
    return head ;
}


void print_list( list_t* head ){
    int cnt = 1 ;
    while( head != NULL ){
        printf( "%d --> " , head->key );
        cnt++ ;
        head = head ->next ;
    }
    printf( "\n") ;
}


list_t* push( list_t* head , int value ){
    list_t *new = new_element( value ) ;
    new->key = value ;
    new->next = head ;
    head = new ;
    return head ;
}

list_t* pop( list_t* top , int *extraxed_value ){
    list_t* ptr ;
    if( top != NULL ){
        *extraxed_value = top->key ;
        ptr = top ;
        top = ptr->next ;
    }
    return top ;
}


