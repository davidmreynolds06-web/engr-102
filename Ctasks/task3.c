#include <stdio.h>

int main() {
    int sec1[8] = {80, 99, 100, 60, 90, 74, 88, 85};
    int sec2[8] = {100, 88, 75, 70, 61, 55, 89, 90};
    int sec3[8] = {55, 76, 50, 80, 88, 100, 100};
    int total1 = 0, total2 = 0, total3 = 0;
    float avg1, avg2, avg3;
    int a = 0, b = 0, c = 0, d = 0, f = 0;
    for (int i = 0; i < 8; i++) {
        total1 += sec1[i];
        if (sec1[i] >= 90) {
            a++;
        } else if (sec1[i] >= 80) {
            b++;
        } else if (sec1[i] >= 70) {
            c++;
        } else if (sec1[i] >= 60) {
            d++;
        } else {
            f++;
        }
        total2 += sec2[i];
        if (sec2[i] >= 90) {
            a++;
        } else if (sec2[i] >= 80) {
            b++;
        } else if (sec2[i] >= 70) {
            c++;
        } else if (sec2[i] >= 60) {
            d++;
        } else {
            f++;
        }
        if (i < 7) {
            total3 += sec3[i];
            if (sec3[i] >= 90) {
                a++;
            } else if (sec3[i] >= 80) {
                b++;
            } else if (sec3[i] >= 70) {
                c++;
            } else if (sec3[i] >= 60) {
                d++;
            } else {
                f++;
            }
        }
    }
    avg1 = total1 / 8.0;
    avg2 = total2 / 8.0;
    avg3 = total3 / 7.0;
    printf("Section 101 average: %.2f\n", avg1);
    printf("Section 102 average: %.2f\n", avg2);
    printf("Section 103 average: %.2f\n", avg3);
    printf("Grade distribution:\n");
    printf("A: %d\n", a);
    printf("B: %d\n", b);
    printf("C: %d\n", c);
    printf("D: %d\n", d);
    printf("F: %d\n", f);
    return 0;

}