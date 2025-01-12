#include "data.h"
#include <stdlib.h>

char *toString(data_t data) {
    char buff[256];
    sprintf(buff,"%s (%d)",data.name,data.population);
    return strdup(buff);
}

int
readData (
  FILE *fp,
  data_t *data
  )
{
  char name[MAXC],pops[MAXC];
  int retValue;

  retValue = fscanf (fp, "%s - %s", name, pops);
  if( retValue == EOF )
      return retValue;
  // clear the ',' from pops
  int c = 0;
  while( pops[c] != '\0' ) {
      if( pops[c] == ',' ) {
          // shift!
          for( int cc = c; pops[cc] != '\0'; cc++ ) {
              pops[cc] = pops[cc+1];
          }
      }
      c++;
  }
  data->name = strdup(name);
  data->population = atoi(pops);

  return (retValue);
}


void
writeData (
  FILE *fp,
  data_t data
  )
{
  fprintf(fp, "%s - %d\n", data.name, data.population);

  return;
}


int
compare (
  data_t d1,
  data_t d2
  )
{
  return (d1.population - d2.population);
}

