#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {

    unsigned int* p = malloc(0x123);

    free(p);

    printf("%p \n", p);

    return 0;
}