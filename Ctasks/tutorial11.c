#include <stdio.h>

int main() {
    int max, min;
    int arr[5];
    printf("Enter an integer: ");
    scanf("%d", &arr[0]);
    max = arr[0];
    min = arr[0];
    for (int i = 1; i < 5; i++) {
        printf("\nEnter an integer: ");
        scanf("%d", &arr[i]);
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    printf("\nMax = %d", max);
    printf("\nMin = %d", min);
    return 0;
}