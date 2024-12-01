#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct list_s2{
    int col ;
    int val ;
    struct list_s2 *next ;

} list_t2 ;

typedef struct list_s1{
    int row ;
    struct list_s1 *next ;
    list_t2 *col ;
} list_t1 ;




void transpose( list_t1 *head1 , list_t1 **head2 ){

    int row = 0 ;
    int col = 0 ;
    int num_row = 0 ;
    int num_col = 0 ;
    list_t1 *ptr1 ;
    list_t2 *ptr2 ;
    list_t1 *head2_local ;



    while( ptr1 != NULL ){
        num_row = num_row + 1;
        ptr2 = ptr2->next ;
    }

    ptr2 = head1->col ;
    while( ptr2 != NULL ){
        num_col = num_col + 1 ;
        ptr2 = ptr2->next ;
    }

    head2_local = ( list_t1* ) malloc( num_col * sizeof( list_t1 ) ) ;
    ptr2 = head2_local ;

    while( ptr2 != NULL ){
        ptr2->col = ( list_t2* ) mallooc( num_row * sizeof( list_t2 ) ) ;
        ptr2 = ptr2->next ; 
    }

    while( head2_local != NULL ){
        head2_local->row = num_row ;


        num_row++ ;
    }

    *head2 = head2_local ;

}