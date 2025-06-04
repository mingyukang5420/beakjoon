#include <stdio.h>

int main(void){
    int num;
    int result = 0;
    scanf("%d", &num);
    for (int i = 1; i <= num; i++)
        result += i;
    printf ("%d", result);
    return 0;
}