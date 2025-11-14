#include <stdio.h>

int main() {
    int arr_len;
    int sum = 0;

    printf("Enter the length of the array: ");
    scanf("%d", &arr_len);
    int arr[arr_len];
    for (int i = 0; i < arr_len; i++) {
        printf("Enter and integer: ");
        scanf("%d", &arr[i]);
    }
    for (int j = 0; j < arr_len; j++) {
        sum += arr[j];
    }
    printf("The sum is: %d\n", sum);
    return 0;
}