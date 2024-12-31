#include <stdio.h>
#include <stdlib.h>

#define N 3

static void mat_copy(int [N][N], int [N][N], int);

void path(int mat[N][N], int matSize, int r, int c, int visitedBest[N][N], int visited[N][N],
          int *pathSumMax, int pathSumCurrent, int *pathLenMax, int pathLenCurrent) {
    int dx[8] = {1,1,1,0,0,-1,-1,-1};
    int dy[8] = {1,0,-1,1,-1,1,0,-1};
    int i, v1 = 0, v2 = 0;

    if (r < 0 || r >= matSize || c < 0 || c >= matSize) return;

    if (visited[r][c] > 0) return;

    v1 = pathSumCurrent + mat[r][c];
    v2 = pathLenCurrent + 1;

    if (r == (matSize - 1) && c == (matSize - 1)) {
        if ((v1 > *pathSumMax) || (v1 == *pathSumMax && v2 < *pathLenMax)) {
            *pathSumMax = v1;
            *pathLenMax = v2;
            mat_copy(visitedBest, visited, matSize);
            visitedBest[r][c] = *pathLenMax;
        }
        return;
    }

    visited[r][c] = v2;

    for (i = 0; i < 8; i++) {
        path(mat, matSize, r+dx[i], c+dy[i], visitedBest, visited, pathSumMax, v1, pathLenMax, v2);
    }


    visited[r][c] = 0;
}

static void mat_copy(int m1[N][N], int m2[N][N], int n) {
    int r, c;
    for (r = 0; r < n; r++) {
        for (c = 0; c < n; c++) {
            m1[r][c] = m2[r][c];
        }
    }
}

int main(void) {
    int mat[N][N] = {{1,2,-3},
                     {9,-9,7},
                     {0,1,4}};
    int matSize = N, visited[N][N], visitedBest[N][N], pathSumMax = INT_MIN, pathLenMax = INT_MIN;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            visited[i][j] = 0;
            visitedBest[i][j] = 0;
        }
    }

    path(mat, matSize, 0, 0, visitedBest, visited, &pathSumMax, 0, &pathLenMax, 0);

    printf("Best Path Length: %d\n", pathLenMax);
    printf("Best Path Sum: %d\n", pathSumMax);

    printf("Best Path Matrix (visitedBest):\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", visitedBest[i][j]);
        }
        printf("\n");
    }
}