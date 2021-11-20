#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void){
    FILE *fp;
    char* logtext = "logging...";
    fp = fopen("log.txt", "w");
    fprintf(fp, logtext);
    fclose(fp);
    return 0;
}