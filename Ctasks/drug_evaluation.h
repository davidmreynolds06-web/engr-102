#ifndef DRUG_EVALUATION_H
#define DRUG_EVALUATION_H

struct drug {
    char name[50];
    float dose;
    bool reaction;
    bool booster;

};

void populateDrugs(struct drug *drugs) {
}

bool evaluateDrugs(struct drug *drugs) {
}
#endif // DRUG_EVALUATION_H