#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>
#include "drug_evaluation.h"

int main() {
    struct drug drugs[10];
    populateDrugs(drugs);
    printf("Drug Evaluation Results:\n");

    for (int i = 0; i < 4; i++) {
        if (evaluateDrugs(&drugs[i])) {
            printf("%s: Rejected\n", drugs[i].name);
        } else {
            printf("%s: Accepted\n", drugs[i].name);
        }
    }

    return 0;
}