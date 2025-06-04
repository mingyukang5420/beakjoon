#include <stdio.h>
#include <stdlib.h>

int getNumber(void){
    int num;
    scanf("%d", &num);
    return num;
}

int factorial(int n){
    if (n == 0) return 1;
    return n * factorial(n-1);
}

int* makeNumbers(int N, int M){ 
    int number = 0;
    int usedNumber[N], unUsedNumber[N];
    int size = factorial(N) / factorial(M);
    int* madeArr = (int*)calloc(size, sizeof(int)); // dynamic allocating
    
    for (int i = 0; i < N; i++){
        usedNumber[i] = 0;
        unUsedNumber[i] = i+1;
    }   

    for(int i = 0; i < size; i++) {
        madeArr[i] = 0; // initializing the array
    }

    for(int i = 0; i < N; i++) {
        if(!usedNumber[i]) {
            number = number * 10 + unUsedNumber[i];
        }
    }
    
    madeArr[0] = number; // 첫번째 순열 저장
    return madeArr;
    }


int makePermutationArray(int *arr, int N, int M){
    int size = factorial(N) / factorial(M);
    for (int i = 0; i < size; i++){
        arr[i] = makeNumber(N, M);
    } 
    return arr;
}


int main(void){
    int N = getNumber();
    int M = getNumber();
    int size = factorial(N) / factorial(M);
    int *arr = (int *)malloc(size * sizeof(int));
    arr = makePermutationArray(arr, N, M);


    return 0;
}