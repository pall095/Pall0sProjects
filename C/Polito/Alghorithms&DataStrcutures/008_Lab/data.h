#ifndef _DATA_INCLUDED
#define _DATA_INCLUDED

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_REGISTER 9
#define MAX_NAME 100

struct data_s {
    char *reg;
    char *name ;
    int credit_loaded ;
    int credit_passed ;
};
typedef struct data_s data_t;

int readData (FILE *, data_t *);
void writeData (FILE *, data_t);
int compare (data_t, data_t);
char *toString(data_t);

#endif
