#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define N 8

// PRESO DA SOLUZIONI MA è SBAGLIAT PERCHé NON CONTROLLI CHE LA CELLA SIA VUOTA

const int offset_x[N] = {-1, -2, -2, -1, 1, 2, 2, 1};
const int offset_y[N] = {-2, -1, 1, 2, -2, -1, 1, 2};

void knight(int mat[N][N], int *r, int *c) {
    int i, j, sum, max_sum = INT_MIN, k;

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            sum = 0;
            for (k = 0; k < N; k++) {
                int nx = i + offset_x[k];
                int ny = j + offset_y[k];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    sum += mat[nx][ny];
                }
            }
            if (sum > max_sum) {
                max_sum = sum;
                *r = i;
                *c = j;
            }
        }
    }
    printf("%d is the max sum obtained at (%d,%d)\n", max_sum, *r, *c);
}

int main(void) {
    int mat[N][N] = {
        {1, 2, 3, 4, 5, 6, 7, 8},
        {8, 7, 6, 5, 4, 3, 2, 1},
        {1, 2, 3, 4, 5, 6, 7, 8},
        {8, 7, 6, 5, 4, 3, 2, 1},
        {1, 2, 3, 4, 5, 6, 7, 8},
        {8, 7, 6, 5, 4, 3, 2, 1},
        {1, 2, 3, 4, 5, 6, 7, 8},
        {8, 7, 6, 5, 4, 3, 2, 1}
    };

    int r = 0, c = 0;
    knight(mat, &r, &c);

    return 0;
}