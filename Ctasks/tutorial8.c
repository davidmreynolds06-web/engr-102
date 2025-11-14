#include <stdio.h>

int main() {
    int num;
    int fact[100];
    printf("Enter an integer: ");
    scanf("%d", &num);
    for (int i = 1; i <= num; i++) {
        if (num % i == 0) {
            fact[i - 1] = i;
            printf("Factor: %d\n", fact[i - 1]);
        }
    }
    return 0;
}