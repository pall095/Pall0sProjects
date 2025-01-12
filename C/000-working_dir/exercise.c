#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define MAX 101

typedef struct list2_s{
    int value ;
    struct list2_s *next ;
} list2_t ;

typedef struct list1_s{
    char name[ MAX ] ;
    list2_t *head ;
    struct list1_s *next ;
} list1_t ;


void print_secondary( list2_t *head ){
    while( head != NULL ){
        printf( "%d -> " , head->value ) ;
        head = head->next ;
    }
    printf( "NULL" ) ;
    return ;
}

void print_primary( list1_t *head ){
    while( head != NULL ){
        printf( "%s :\n" , head->name ) ;
        print_secondary( head->head ) ;
        printf( "\n" ) ;
        head = head->next ;
    }
    return ;
}

list1_t* new_primary( ){
    list1_t *ptr = ( list1_t* ) calloc( 1 , sizeof( list1_t ) ) ;
    return ptr ;
}


list2_t* new_secondary( ){
    list2_t *ptr = ( list2_t* ) calloc( 1 , sizeof( list2_t ) ) ;
    return ptr ;
}

int is_in1( list1_t *head , char name[ MAX ] ){

    while( head != NULL ){
        if( strcmp( head->name , name ) == 0 ){
            return 1;
        }
        head = head->next ;
    }
    return 0 ;
}

int is_in2( list2_t *head , int value ){

    while( head != NULL ){
        if( head->value == value ){
            return 1;
        }
        head = head->next ;
    }
    return 0 ;
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


list1_t* file_to_list_of_lists( char *filename ){
    
    FILE *ptr = fopen( filename , "r" ) ;
    list1_t *head = NULL ;
    list1_t *new1 ;
    list2_t *new2 ;
    list1_t *traverser ;
    char current_name[ MAX ] ;
    int num_values ;
    int current_value ;
    int i ;


    while( fscanf( ptr , "%s %d" , current_name , &num_values ) != EOF ){


        if( is_in1( head , current_name ) == 0 ){

            new1 = new_primary( ) ;
            strcpy( new1->name , current_name ) ;
            new1->head = NULL ;
    
            for( i = 0 ; i < num_values ; i++ ){
                fscanf( ptr , "%d" , &current_value ) ;
                new2 = new_secondary( ) ;
                new2->value = current_value ;
                new1->head = push_secondary( new1->head , new2 ) ;
            }

            head = push_primary( head , new1 ) ;

        }else{

            traverser = head ;
            while( strcmp( traverser->name , current_name ) != 0 ){
                traverser = traverser->next ;
            }

            for( i = 0 ; i < num_values ; i++ ){
                fscanf( ptr , "%d" , &current_value ) ;
                if( is_in2( traverser->head , current_value ) == 0 ){
                    new2 = new_secondary( ) ;
                    new2->value = current_value ;
                    traverser->head = push_secondary( traverser->head , new2 ) ;
                }
                
            }
        }
    } 

    fclose( ptr ) ;
    return head ;

}


void main( int argc , char **argv ){

    list1_t *head = file_to_list_of_lists( argv[ 1 ] ) ;
    print_primary( head ) ;




}