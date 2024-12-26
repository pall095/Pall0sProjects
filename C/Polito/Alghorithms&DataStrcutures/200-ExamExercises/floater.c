#include<stdio.h>
#include<string.h>

void f (int i, int j, int k) {
if (i<0 && j<0 && k<0) {
return;
}
if (i>=0) {
printf ("I");
f (i-1, j, k);
} else {
if (j>=0) {
printf ("J");
f (i, j-1, k);
} else {
if (k>=0) {
printf ("K");
f (i, j, k-1);
}
}
}
return;
}
int main () {
f(5,4,3);
return 1;
}