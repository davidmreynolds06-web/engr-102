#include <stdio.h>

int main() {

int number, sum;do {printf("Enter a positive number (1-10): \n");
scanf("%d", &number);
if (number <= 0 || number > 10) {
printf("Invalid number. Please try again.\n");
}
} while (number <= 0 || number > 10);

sum = 0;
for (int i = 1; i <= number; i++) {
    sum += i;
}
printf("The sum of all integers from 1 to %d is %d\n", number, sum);

for (int i = 1; i <= 10; i++) {
    printf("%d x %d = %d\n", number, i, number * i);
}

return 0;
}