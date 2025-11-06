#include <stdio.h>

int main() {
    int sum;
    int upper;
    printf("Please enter an upper limit: ");
    scanf("%d", &upper);
    for (int i = 1; i <= upper; i++) {
        if (i % 2 == 0) {
            sum += i;
        }
    }
    printf("The sum of even numbers up to %d is %d\n", upper, sum);
    return 0;
}

int main2() {
    int sum = 0;
    int lower, upper;
    printf("Please enter a lower limit: ");
    scanf("%d", &lower);
    printf("Please enter an upper limit: ");    
    scanf("%d", &upper);
    for (int i = lower; i <= upper; i++) {
        if (i % 2 == 0) {
            sum += i;
        }
    }
    printf("The sum of even numbers between %d and %d is %d\n", lower, upper, sum);
    return 0;
}