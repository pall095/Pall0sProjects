#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define MAX_CHAR 101

typedef struct list2_s{

    int value ;
    int occurrence ;
    struct list2_s *next ;
} list2_t ;

typedef struct list1_s{
    char *key ;
    list2_t *head ;
    struct list1_s *next ;
} list1_t ;


list1_t *new_primary( char str[ MAX_CHAR ] ){

    list1_t *ptr = ( list1_t * ) calloc( 1 , sizeof( list1_t ) ) ;
    ptr->key = ( char * ) calloc( strlen( str ) , sizeof( char ) ) ;
    strcpy( ptr->key , str ) ;
    ptr->head = NULL ;
    return ptr ;

}

list2_t* new_secondary( int value ){
    list2_t *ptr = ( list2_t * ) calloc( 1 , sizeof( list2_t ) ) ;
    ptr->value = value ;
    ptr->occurrence = 1 ;
    return ptr ;
}

void print_secondary( list2_t *head ){

    while( head != NULL ){
        printf( "%d %d -> " , head ->value , head->occurrence ) ;
        head = head->next ;
    }
    return ;
}

void print_primary( list1_t *head ){

    while( head != NULL ){
        printf( "%s : " , head ->key ) ;
        print_secondary( head->head ) ;
        printf( "\n" ) ;
        head = head->next ;

    }
    printf( "\n" ) ;
    return ;
}

list1_t* is_in_primary( list1_t *head , list1_t *new ){

    list1_t *traverser = head ;
    while( traverser != NULL ){
        if( strcmp( traverser->key , new->key ) == 0 ){
            return traverser ;
        }
        traverser = traverser -> next ;
    }
    free( traverser ) ;
    return NULL ;
}

list2_t* is_in_secondary( list2_t *head , list2_t *new ){

    list2_t *traverser = head ;

    while( traverser!= NULL ){
        if( traverser->value == new->value ){
            return traverser ;
        }
        traverser = traverser -> next ;
    }
    free( traverser ) ;
    return NULL ;
}


list1_t* push_primary( list1_t *head , list1_t *new ){
    new->next = head ;
    head = new ;
    return head ;
}


list2_t* push_secondary( list2_t *head , list2_t *new ){
    new->next = head ;
    head = new ;
    return head ;
}



list1_t* insert( char *filename ){

    FILE *f_ptr = fopen( filename , "r" ) ;
    char current_name[ MAX_CHAR ] ;
    int current_value ;
    list1_t *head = NULL ;
    list1_t *new_p ;
    list2_t *new_s ;
    list1_t *tmp1;
    list2_t *tmp2 ;

    while( fscanf( f_ptr , "%s %d" , current_name , &current_value ) != EOF ){

        new_p = new_primary( current_name ) ;
        new_s = new_secondary( current_value ) ;        
        tmp1 = is_in_primary( head , new_p ) ;

        if( tmp1 == NULL ){
            new_p->head = push_secondary( new_p->head , new_s) ;
            head = push_primary( head , new_p ) ;
        
        }else{

            tmp2 = is_in_secondary( tmp1->head , new_s ) ;
            if( tmp2 == NULL ){
                tmp1->head = push_secondary( tmp1->head , new_s ) ;
            }else{
                tmp2->occurrence++;
            }
        }
    } 

    free( new_p ) ;
    free( new_s ) ;
    free( tmp1 ) ;
    free( tmp2 ) ;
    return head ;
}

void main( int argc , char **argv ){

    list1_t *head = insert( argv[ 1 ] ) ;
    print_primary( head ) ;

}
