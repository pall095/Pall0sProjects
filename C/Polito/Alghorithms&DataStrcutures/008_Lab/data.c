#include "data.h"
#include <stdlib.h>

char *toString(data_t data) {
    char buff[256];
    sprintf(buff,"%s (%d)",data.reg,data.name);
    return strdup(buff);
}

int
readData (
  FILE *fp,
  data_t *data
  )
{
  char reg[ MAX_REGISTER ] ;
  char name[ MAX_NAME ] ;
  int loaded_credit ;
  int passed_credit ;
  int retValue;

  retValue = fscanf (fp, "%s %s %d %d", reg , name , &loaded_credit , &passed_credit );
  if( retValue == EOF )
      return retValue;


  printf("debug pops: %s %s %d %d\n", reg , name , loaded_credit , passed_credit );
  data->name = name ;
  data->reg = reg ;

  return (retValue);
}


void
writeData (
  FILE *fp,
  data_t data
  )
{
  fprintf(fp, "%s - %d\n", data.reg, data.name);

  return;
}


int
compare (
  data_t d1,
  data_t d2
  )
{
  return (d1.name - d2.name );
}

