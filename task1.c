#include <stdio.h>

int main() {

char food_choice, combo_choice;
int quantity;
float total;

printf("Select your food (A-Hamburger, B-Pizza, C-Salad): ");
scanf(" %c", &food_choice);
printf("You selected: %c\n", food_choice); // Echo print
printf("Make it a combo? (Y/N): ");
scanf(" %c", &combo_choice);
printf("Combo choice: %c\n", combo_choice); // Echo print
printf("Enter quantity: ");
scanf("%d", &quantity);
printf("Quantity entered: %d\n", quantity); // Echo print
// Calculate total based on selections
if (food_choice == 'A' || food_choice == 'a') {
    if (combo_choice == 'Y' || combo_choice == 'y') {
        total = 8.99 * quantity; // Combo price
    } else if (combo_choice == 'N' || combo_choice == 'n') {
        total = 6.99 * quantity; // Regular price
    } else {
        printf("Invalid combo choice.\n");
        return 1;
    }
} else if (food_choice == 'B' || food_choice == 'b') {
    if (combo_choice == 'Y' || combo_choice == 'y') {
        total = 5.99 * quantity; // Combo price
    } else if (combo_choice == 'N' || combo_choice == 'n') {
        total = 3.99 * quantity; // Regular price
    } else {
        printf("Invalid combo choice.\n");
        return 1;
    }
} else if (food_choice == 'C' || food_choice == 'c') {
    if (combo_choice == 'Y' || combo_choice == 'y') {
        total = 7.99 * quantity; // Combo price
    } else if (combo_choice == 'N' || combo_choice == 'n') {
        total = 5.99 * quantity; // Regular price
    } else {
        printf("Invalid combo choice.\n");
        return 1;
    }
} else {
    printf("Invalid food choice.\n");
    return 1;
}
printf("Your total is: $%.2f\n", total);

return 0;
}