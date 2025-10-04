#include <stdio.h>

int main() {
    int height;
    int width;
    
    printf("Please enter the height: ");
    scanf("%d", &height);
    
    printf("Please enter the width: ");
    scanf("%d", &width);
    
    printf("The area is: %d", height * width);
    printf("The perimeter is: %d", 2 * (height + width));
    
    return 0;
}