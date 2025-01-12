#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX 101

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

void print_secondary( list2_t *head ){
    
    while( head != NULL ){
        printf( "%d %d --> " , head->value , head->occurrence ) ;
        head = head->next ;
    }
    printf( "\n" ) ;
    return ;
}

void print_primary( list1_t *head ){
    while( head != NULL ){
        printf( "%s \n" , head->key ) ;
        print_secondary( head->head ) ;
        head = head->next ;
    }
    
}

int is_in1( list1_t *head , char name[ MAX ] ){

    while( head != NULL ){
        if( strcmp( head->key , name ) == 0 ){
            return 1 ;
        }
        head = head -> next ;
    }
    return 0 ;
}

int is_in2( list2_t *head , int value ){

    while( head != NULL ){
        if( head->value == value ){
            return 1 ;
        }
        head = head -> next ;
    }
    return 0 ;
}

list1_t* new_primary( ){
    list1_t *new = ( list1_t* ) calloc( 1 , sizeof( list1_t ) ) ;
    return new ;
}

list2_t* new_secondary( ){
    list2_t *new = ( list2_t* ) calloc( 1 , sizeof( list2_t ) ) ;
    return new ;
}

list1_t* push_primary( list1_t* head , list1_t *new ){

    new->next = head ;
    head = new ;
    return head ;
}


list2_t* push_secondary( list2_t* head , list2_t *new ){

    new->next = head ;
    head = new ;
    return head ;
}

list2_t* update_occurrence( list2_t* head , int value ){

    list2_t *p = head ;

    while( p != NULL ){
        if( p->value == value ){
            p->occurrence++ ;
            break ;
        }
        p = p->next ;
    }
    return head ;
}

list1_t* insert( char *filename ){

    FILE *f_ptr = fopen( filename , "r" ) ;
    int current_value ;
    char current_string[ MAX ] ;
    list1_t *head = NULL ;
    list1_t *traverser ;
    list1_t *new1 ;
    list2_t *new2 ;



    while( fscanf( f_ptr , "%s %d" , current_string , &current_value ) != EOF ){

            if( is_in1( head , current_string ) ==  0){
                new1 = new_primary( ) ;
                new1->key = ( char * ) calloc( strlen( current_string ) , sizeof( char ) ) ;
                new1->head = NULL ;
                strcpy( new1->key , current_string ) ;
                new2 = new_secondary( ) ;
                new2->value = current_value ;
                new2->occurrence = 1 ;
                new1->head = push_secondary( new1->head , new2 ) ;
                head = push_primary( head , new1 ) ;
            }else{

                traverser = head ;
                while( traverser != NULL ){
                    if( strcmp( traverser->key , current_string ) == 0 ){
                        break ;
                    }
                    traverser = traverser->next ;
                }

                
                if( is_in2( traverser->head , current_value ) == 0 ){
                    new2 = new_secondary( ) ;
                    new2->value = current_value ;
                    new2->occurrence = 1 ;
                    traverser->head = push_secondary( traverser->head , new2 ) ;
                }else{
                    traverser->head = update_occurrence( traverser->head , current_value ) ;
                }
            }


    }

    fclose( f_ptr ) ;
    return head ;

}

void main( int argc , char **argv ){

    list1_t *head = insert( argv[ 1 ] ) ;
    print_primary( head ) ;



}

