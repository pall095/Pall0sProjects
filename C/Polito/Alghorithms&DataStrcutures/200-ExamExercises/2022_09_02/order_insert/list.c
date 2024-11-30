#include "listPrivate.h" 


void print_list( list_t* head ){

    while( head != NULL ){
        printf( "%s -> " , head->surname );
        head = head->next ;
    }

    printf( "\n"  ) ;

}

list_t* new_element( char *name , char *surname ){
    list_t *ptr = ( list_t* ) malloc( sizeof( list_t ) ) ;

    if( ptr == NULL ){
        printf( "Unable to allocate memory!\n" ) ;
        exit( EXIT_FAILURE ) ;
    }

    ptr->name = ( char * ) malloc( MAX_STR * sizeof( char ) ) ;
    ptr->surname = ( char * ) malloc( MAX_STR * sizeof( char ) ) ;

    if( ptr->name != NULL ){
        strcpy( ptr->name , name ) ;
    }

    if( ptr->surname != NULL ){
        strcpy( ptr->surname , surname ) ;
    }

    return ptr ;

}

list_t* order_insert( list_t* head , char *name , char *surname ){

    list_t *item = new_element( name , surname ) ;
    int cmp ;
    list_t *trv ;

    trv = head ;
    
    if( head == NULL ){
        item->next = head ;
        head = item ;
        return head ;
    }
    
    cmp = strcmp( head->surname , surname );
    if( cmp == 0){
        printf( "Fail\n" ) ;
        return head ;
    }
    
    if( cmp > 0 ){
        item->next = head ;
        head = item ;
        printf( "Inserted at head\n" );
        return head ;
    }else{

        while( trv != NULL ){

            if( trv->next == NULL ){
                item->next = trv->next ;
                trv->next = item ;
                printf( "Append case\n" ) ;
                return head ;
            }

            cmp = strcmp( trv->next->surname , surname ) ;
            
            if( cmp == 0 ){
                printf( "Name already present!\n" ) ;
                return head ;
            }

            if( cmp > 0 ){
                item->next = trv->next ;
                trv->next = item ;
                printf( "Inserted\n" );
                return head ;
            }

            if( cmp < 0 ){
                trv = trv->next ;
            }

        }
    }

}