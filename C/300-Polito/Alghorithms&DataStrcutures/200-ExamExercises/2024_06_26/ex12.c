#include <stdio.h>
#include <stdlib.h>
#include<string.h>

#define MAX_CHAR 100 

typedef struct list2_s{
    int val ;
    struct list2_s *next ;
} list2_t ;

typedef struct list1_s{
    char *key ;
    list2_t *head ;
    struct list1_s *next ;
} list1_t ;

list1_t* new_name( ){
    list1_t *ptr ;
    ptr = ( list1_t* ) malloc( sizeof( list1_t ) ) ;
    if( ptr == NULL ){
        printf( "Unable to allocate memory for type 1 item!\n" ) ;
        exit( EXIT_FAILURE ) ; 
    }  
    ptr->key = ( char * ) malloc( ( MAX_CHAR + 1 ) * sizeof( char ) ) ;
    if( ptr->key == NULL ){
        printf( "Unable to allocate memory for key!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }
    return ptr ;
}

list2_t* new_num( ){
    list2_t *ptr ;
    ptr = ( list2_t* ) malloc( sizeof( list2_t ) ) ;

    if( ptr == NULL ){
        printf( "Unable to allocate memory for type 2 item!\n" ) ;
        exit( EXIT_FAILURE ) ; 
    }
    return ptr ;
}   

int in_list1( list1_t *p , char *name ){
    while( p != NULL ){
        if( strcmp( p->key , name ) == 0 ){
            return 1 ;
        }
        p = p->next ;
    }
    return 0 ;
}

int in_list2( list2_t *p , int val ){
    while( p != NULL ){
        if( p->val == val ){
            return 1 ;
        }
        p = p->next ;
    }
    return 0 ;
}

list2_t* push2( list2_t *head , list2_t *new ){
    new->next = head ;
    head = new ;
    return head ;
}

list1_t* push1( list1_t *head , list1_t *new ){
    new->next = head ;
    head = new ;
    return head ;
}

list1_t* find1( list1_t *head , char *key ){
    while( strcmp( head->key , key ) != 0 ){
        head = head->next ;
    }
    if( head == NULL ){
        return NULL ;
    }else{
        return head ;
    }

}

void print_list2( list2_t *head ){

    while( head != NULL ){
        printf( "%d -> " , head->val ) ;
        head = head -> next ;
    }

}

void print_list1( list1_t *head ){

    while( head != NULL ){
        printf( "%s : " , head->key ) ;
        print_list2( head->head ) ;
        printf( "\n" ) ;
        head = head -> next ;
    }

}




list1_t* read_file( char *filename ){

    char *current_name = ( char * ) malloc( ( MAX_CHAR + 1 ) * sizeof( char ) );
    int num_values ;
    int current_value ;
    list1_t *temp_nme ; 
    list2_t *temp_n ;
    list1_t *main_head = new_name( ) ;
    main_head->head = new_num( ) ;
    main_head->head = NULL ;
    main_head = NULL ;
    
    
    FILE *f_ptr = fopen( filename , "r" ) ;

    if( f_ptr == NULL ){
        printf( "Unable to open the input file!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }else{
        printf( "File opened correctly!\n") ;
    }
    

    while( fscanf( f_ptr , "%s %d" , current_name , &num_values ) != EOF ){
        
        if( in_list1( main_head , current_name ) == 0 ){
            temp_nme = new_name( ) ;
            strcpy( temp_nme->key , current_name ) ;
            temp_nme->head = NULL ;

            for( int i = 0 ; i < num_values ; i++ ){
                fscanf( f_ptr , "%d" ,  &current_value ) ;
                temp_n = new_num( ) ;
                temp_n->val = current_value ;
                temp_nme->head = push2( temp_nme->head , temp_n ) ;
            }
        main_head = push1( main_head , temp_nme ) ;
        }else{

            temp_nme = find1( main_head , current_name ) ;

            for( int i = 0 ; i < num_values ; i++ ){
                fscanf( f_ptr , "%d " ,  &current_value ) ;
                if( in_list2( temp_nme->head , current_value ) == 0 ){
                    temp_n = new_num( ) ;
                    temp_n->val = current_value ;
                    temp_nme->head = push2( temp_nme->head , temp_n ) ;
                }
                

            }
        }
    }

    free( temp_nme ) ;
    free( temp_n ) ;
    fclose( f_ptr ) ;
    return main_head ;

}



void main( int argc , char **argv ){

    list1_t *main_head = read_file( argv[ 1 ]  ) ;
    print_list1( main_head ) ;


}
