#include <stdio.h>

int main() {
    int arr[5];
    int ray[5];
    printf("Enter and integer: ");
    scanf("%d", &arr[0]);
    for (int i = 1; i < 5; i++) {
        printf("\nEnter an integer: ");
        scanf("%d", &arr[i]);
    }
    for (int i = 0; i < 5; i++) {
        ray[i] = arr[i];
    }
    for (int i = 0; i < 5; i++) {
        printf("\nray[%d] = %d", i, ray[i]);
    }
    return 0;
}