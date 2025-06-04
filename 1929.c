#include <stdio.h>
//#include <stdbool.h>
#include <math.h>

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
    int num1, num2;
    scanf("%d %d",&num1, &num2);
    for (int i = num1; i <= num2; i++){
        if(is_Prime(i) == 1)
            printf("%d\n",i);
    }
    
    return 0;
}