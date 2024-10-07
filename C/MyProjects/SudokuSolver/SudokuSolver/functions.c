
int read_grid( char *filename , int WIDTH ){

    FILE *file_ptr ;
    int grid[ WIDTH ][ WIDTH ] ;
    int i =0 ;
    int j = 0 ;
    char line[ WIDTH ] ;
    file_ptr = fopen( file_name , "r" ) ;

    while( fgets( line , WIDTH + 2 , file_ptr) != NULL ){
        for( j = 0 ; j < WIDTH ; j++ ){
            if( line[ j ] == "\n" ) {
                printf( "found") ;
            }
            printf( "Num: %c , Row: %d , Col: %d \n" , (int)line[ j ] , i , j );
        }
        printf( "---\n") ;
        i++ ;
    }

        return grid ;
}
