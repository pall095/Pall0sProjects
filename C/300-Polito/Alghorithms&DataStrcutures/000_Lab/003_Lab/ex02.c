#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>

#define MAX_NAME 51
#define MAX_ID 17
#define MAX_DATE 11


typedef struct list_s{

    char name_surname[ MAX_NAME ] ;
    char ID[ MAX_ID ] ;
    char hiring_date[ MAX_DATE ] ;
    int salary ;
    struct list_s* left ;
    struct list_s* right ; 

} employee_t ;

employee_t* read_file( employee_t* , char* ) ;
employee_t* new_element( void ) ; 
employee_t* insert_head( employee_t* , employee_t* ) ;
void print_list( employee_t* ) ;
void print_item( employee_t* ) ;
void find_and_shift( employee_t* , char* , char* ) ;

void main( int argc , char **argv ){

    employee_t* list_head = NULL ;
    list_head = read_file( list_head , argv[ 1 ] ) ;
    print_list( list_head ) ;
    printf( "---\n" ) ;
    find_and_shift( list_head , argv[ 2 ] , argv[ 3 ] ) ;  
}


employee_t* new_element( void ){
    employee_t* ptr ;
    ptr = ( employee_t* ) malloc( sizeof( employee_t ) ) ;
    if( ptr == NULL ){
        printf( "Unable to allocate memory! \n" ) ;
        return NULL ;
    }
    return ptr ;
}


employee_t* read_file( employee_t* head , char *file_name ){

    FILE *ptr = fopen( file_name , "r" ) ;
    employee_t* new_employee ;
    char current_name_surname[ MAX_NAME ] ;
    char current_ID[ MAX_ID ] ;
    char current_hiring_date[ MAX_DATE ] ;
    int current_salary ;

    if( ptr == NULL ){
        printf( "Unable to open file!\n" ) ;
        return NULL ;
    }
    while( fscanf( ptr , "%s %s %s %d" , current_name_surname , current_ID , current_hiring_date , &current_salary ) != EOF ){
        new_employee = new_element( ) ;
        strcpy( new_employee->name_surname , current_name_surname ) ;
        strcpy( new_employee->ID , current_ID ) ;
        strcpy( new_employee->hiring_date , current_hiring_date ) ;
        new_employee->salary = current_salary ;
        head = insert_head( head , new_employee ) ;
    }
    return head ;
}

employee_t* insert_head( employee_t* head , employee_t* new_employee ){
    if( head == NULL ){
        new_employee->right = head ;
        return new_employee  ;
    }
    head->left = new_employee ;
    new_employee->right = head ;
    return new_employee ;
} 

void find_and_shift( employee_t *head , char *name , char *shifter ){
    employee_t* p = head ; 
    while( p != NULL ){
        if( strcmp( p->name_surname , name ) == 0 ){
            print_item( p ) ;
            break ;
        }
        p = p->right ; 
    }
    while( *shifter != '\0' ){
        if( *shifter == '+' ){
            if( p->right != NULL ){
                p = p->right ;
            }
        }else{
            if( p != head ){
                p = p->left ;
            }
        }
        print_item( p ) ;
        shifter = shifter + 1 ;
    }
}

void print_item( employee_t* p ){
    printf( "%s - %s - %s - %d \n" , p->name_surname , p->ID , p->hiring_date , p->salary ) ;
}

void print_list( employee_t* p ){
    while( p != NULL ){
        print_item( p  ) ;
        p = p->right ;
    }
    return ;
}