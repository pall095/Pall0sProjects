#include <stdio.h>
#include <stdlib.h>

char **array_to_histogram (int *vet, int n) {
    
    int i, j, val;
    char **result = (char ** ) malloc (n * sizeof(char *));
    for (i = 0; i < n; i ++) {
        val = vet[i];
        result[i] = (char *) malloc (val * sizeof(char));
        for (j = 0; j < val; j++) {
            result[i][j] = '*';
        }
    }


    return result;
}

int main(void) {
    char **result;
    int n = 5;
    int *vet = (int *) malloc (n * sizeof(int));
    vet[0] = 3; vet[1] = 5; vet[2] = 7; vet[3] = 2; vet[4] = 9;
    result = array_to_histogram(vet, n);

    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < vet[ i ] ; j++ ){
            printf( "%c " , result[ i ][ j ] ) ;
        }
        printf("\n") ; 
    }


    free(vet);
    free(result);
    return 0;
}

