#include <stdio.h>
//#include <stdlib.h>
#include <math.h>
#include <stdlib.h>


int* getNumbers(int* size_ptr){
/*     int size_input;
    scanf("%d", &size_input);
    *size_ptr = size_input; */

    int* arr = (int*)calloc(*size_ptr,sizeof(int));
    if (arr == NULL){
        fprintf(stderr,"Failed to allocate memory");
        exit(EXIT_FAILURE);
    }

    for (int i = 0 ; i < *size_ptr; i++){
        scanf("%d", arr+i);
    }
    return arr;
}

int count_Divisor(int num){
    int cnt = 0;
    int upper_bound = sqrt(num);
    for (int i = 1; i <= upper_bound; i++){
        if(num % i == 0) cnt++;
    }
    return cnt;
}

int is_Prime(int num){
    if (num == 1) return 0;
    else if(count_Divisor(num) == 1) return 1;
    else return 0;
}

int main(void){
    int size;                                       // the number of numbers to input
    scanf("%d",&size);
    int* arr_Number = getNumbers(&size);            // get the numbers from the input
    int cnt = 0;                                    // the number of prime numbers
    for (int i = 0; i < size; i++)                // check if the number is prime
        cnt += is_Prime(arr_Number[i]);
    printf("%d", cnt);                              // print the number of prime numbers
    free(arr_Number);
    return 0;
}