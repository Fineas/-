#include <stdio.h>
#include "diymalloc.h"

int main(void)
{
    char *pcon;

    pcon = malloc(10*sizeof(char));
    if (!pcon)
        fprintf(stderr, "malloc failed!\n");

        if (pcon != NULL) {
                free(pcon);
                pcon = NULL;
        }
    fprintf(stderr, "main end!\n");
    return 0;
}
