#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>


bool is_Prime(int num){
    int upper_bound = (int)sqrt(num);
    if (num == 1) return false;
    for (int i = 2; i <= upper_bound; i++){
        if (num % i == 0) return false;
    }
    return true;
}

int* getNumbers(int* size_ptr){
    int* arr = (int*)calloc(*size_ptr,sizeof(int));
    for (int i = 0; i < *size_ptr; i++){
        scanf("%d", arr+i);
    }
    return arr;
}

int main(void){
    int num;
    scanf("%d", &num);
    int* arr = (int*)calloc(num,sizeof(int));
    for (int i = 0; i < num; i++){
        scanf("%d", arr+i);
    }
    return 0;
}