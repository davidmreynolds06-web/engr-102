#include <stdio.h>

 // Example code structure
 float getRadius() {
 // Prompt user for radius and return the value
 printf("Enter radius: ");
 float radius;
 scanf("%f", &radius);
 printf("You entered radius: %.2f\n", radius);
 return radius;
 }
 float calculate(float radius, int choice) {
 // Calculate and return the result based on the user's choice
    float result = 0.0;
    if (choice == 1) {
        result = 3.14159 * radius * radius * radius * (4.0 / 3.0); // Volume of sphere
    }
    else if (choice == 2) {
        result = radius * radius * 3.14159; // Area of circle
    }
    return result;
 }
 int main() {
 // Use the getRadius and calculate functions to get input and perform calculations
 float radius = getRadius();
 int choice;
 printf("Enter your choice (1 for sphere volume, 2 for circle area): ");
 scanf("%d", &choice);
 float result = calculate(radius, choice);
 printf("Result: %.2f\n", result);
 return 0;
}
// Print the result based on the user's choice