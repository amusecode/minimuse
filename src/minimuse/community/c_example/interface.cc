#include "minilib.h"

extern int echo(int input);

/*
 * Interface code
 */
 
int echo_int(int input, int * output){
    *output = echo(input);
    return 0;
}

int add_one(int * output){
    add1(output);
    return 0;
}

