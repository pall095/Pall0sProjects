#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

void A(int, int);
void B(int, int);
void C(int, int);
void D(int, int);
int main() {
A(3, 3);
return 0;
}
void A(int counterA, int counterB) {
if (counterA <= 0) return;
printf("A");
B(counterB, counterA - 1);
}
void B(int counterB, int counterC) {
if (counterB <= 0) return;
printf("B");
C(counterC, counterB - 1);
D(counterC - 1, counterB - 1);
}
void C(int counterC, int counterD) {
if (counterC <= 0) return;
printf("C");
D(counterD, counterC - 1);
}
void D(int counterD, int counterA) {
if (counterD <= 0) return;
printf("D");
A(counterA, counterD - 1);
}