#include "drug_evaluation.h"

#define dn1 "UN001"
#define dn2 "UN2134"
#define dn3 "UN009"
#define dn4 "UN3453"

#define dd1 30.0
#define dd2 25.0
#define dd3 30.0
#define dd4 35.0

#define dr1 true
#define dr2 true
#define dr3 false
#define dr4 true

#define db1 false
#define db2 true
#define db3 false
#define db4 true

void populateDrugs(struct drug *drugs) {
    // Populate the drug data
    strcpy(drugs[0].name, dn1);
    drugs[0].dose = dd1;
    drugs[0].reaction = dr1;
    drugs[0].booster = db1;

    strcpy(drugs[1].name, dn2);
    drugs[1].dose = dd2;
    drugs[1].reaction = dr2;
    drugs[1].booster = db2;

    strcpy(drugs[2].name, dn3);
    drugs[2].dose = dd3;
    drugs[2].reaction = dr3;
    drugs[2].booster = db3;

    strcpy(drugs[3].name, dn4);
    drugs[3].dose = dd4;   
    drugs[3].reaction = dr4;
    drugs[3].booster = db4;
}

bool evaluateDrugs(struct drug *drugs) {
    if (drugs->reaction && drugs->dose > 30.0) {
        return true;
    } else if (drugs->reaction && drugs->booster) {
        return true;
    } else {
        return false;
    }
}