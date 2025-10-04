#include <stdio.h>

int main() {

    int SBP, DBP, PP;
    float MAP;
    printf("Enter systolic blood pressure: ");
    scanf("%d", &SBP);
    printf("You entered SBP: %d\n", SBP); // echo print

    printf("Enter diastolic blood pressure: ");
    scanf("%d", &DBP);
    printf("You entered DBP: %d\n", DBP);

    PP = SBP - DBP;
    MAP = (2.0 * DBP + SBP) / 3.0;
    printf("Pulse Pressure: %d\n", PP);
    printf("Mean Arterial Pressure: %.2f\n", MAP);

    // Determine blood pressure category
    if (SBP < 120 && DBP < 80) {
        printf("Blood Pressure Category: Normal\n");
    }
    else if (120 <= SBP && SBP <= 129 && DBP < 80) {
        printf("Blood Pressure Category: Elevated\n");
    }
    else if ((SBP >= 130 && SBP <= 139) || (DBP >= 80 && DBP <= 89)) {
        printf("Blood Pressure Category: Hypertension Stage 1\n");
    }
    else if (SBP >= 140 || DBP >= 90) {
        printf("Blood Pressure Category: Hypertension Stage 2\n");
    }
    else if (SBP > 180 || DBP > 120) {
        printf("Blood Pressure Category: Hypertensive Crisis\n");
    }
    return 0;

}