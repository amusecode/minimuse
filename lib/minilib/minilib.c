#include <stdio.h>

void add1(int *i){
  printf("library function called");
  (*i)+=1;
}

