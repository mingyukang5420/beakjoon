#include <stdio.h>
#include <stdbool.h>
#include <math.h>

// Bertrand's postulate


bool is_Prime(int num){ // check if num is prime
    int upper_bound = (int)sqrt(num); // sqrt(num) is the upper bound of the factors
    if (num == 1) return false; // 1 is not prime
    for (int i = 2; i <= upper_bound; i++){
        if (num % i == 0) return false; // if num is divisible by i, then num is not prime
    }
    return true;
}

int range_Bertrand(int num){
    int start = num; // start from num+1
    int end = 2*num; // end at 2*num
    int cnt = 0; // count the number of primes
    for (int i = start+1; i <= end; i++){ // check if i is prime
        if (is_Prime(i)) cnt++; // if i is prime, then cnt++
    }
    return cnt;
}

int main(void){
    int arr_num[BUFSIZ]; // input number
    int i = 0;
    while (scanf("%d", arr_num+i) != EOF){ // read input until EOF
        if (arr_num[i] == 0) break; // if num is 0, break
        i++;
    }
    for (int j = 0; j < i; j++){
        printf("%d\n", range_Bertrand(arr_num[j])); // print the number of primes
    }
    return 0;
}