#include <stdio.h>

int main() {
    float r1, r2, r3, r4, area1, area2, area3, area4, sphere1, sphere2, sphere3, sphere4;
    printf("Enter radius 1: ");
    scanf("%f", &r1);
    printf("You entered: %.2f\n", r1);
    printf("Enter radius 2: ");
    scanf("%f", &r2);
    printf("You entered: %.2f\n", r2);
    printf("Enter radius 3: ");
    scanf("%f", &r3);
    printf("You entered: %.2f\n", r3);
    printf("Enter radius 4: ");
    scanf("%f", &r4);
    printf("You entered: %.2f\n", r4);
    area1 = 3.14 * r1 * r1;
    area2 = 3.14 * r2 * r2; 
    area3 = 3.14 * r3 * r3;
    area4 = 3.14 * r4 * r4;
    sphere1 = (4.0/3.0) * 3.14 * r1 * r1 * r1;
    sphere2 = (4.0/3.0) * 3.14 * r2 * r2 * r2;
    sphere3 = (4.0/3.0) * 3.14 * r3 * r3 * r3;
    sphere4 = (4.0/3.0) * 3.14 * r4 * r4 * r4;
    printf("Results:\n");
    printf("Radius %.2f:\n\tSphere volume: %.2f\n\tCircle area: %.2f\n", r1, sphere1, area1);
    printf("Radius %.2f:\n\tSphere volume: %.2f\n\tCircle area: %.2f\n", r2, sphere2, area2);
    printf("Radius %.2f:\n\tSphere volume: %.2f\n\tCircle area: %.2f\n", r3, sphere3, area3);
    printf("Radius %.2f:\n\tSphere volume: %.2f\n\tCircle area: %.2f\n", r4, sphere4, area4);
    return 0;
}