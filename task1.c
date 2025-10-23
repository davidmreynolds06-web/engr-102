#include <stdio.h>

int is_valid_password(char* password) {
    int has_upper = 0, has_lower = 0, has_digit = 0, has_symbol = 0, length = 0;
    for (int i = 0; password[i] != '\0'; i++) {
        if (password[i] >= 'A' && password[i] <= 'Z') 
            {has_upper = 1;}
        else if (password[i] >= 'a' && password[i] <= 'z')
            {has_lower = 1;}
        else if (password[i] >= '0' && password[i] <= '9') 
            {has_digit = 1;}
        else if ((password[i] == 63) || (password[i] == 95) || (password[i] == 36) || (password[i] == 33)) 
            {has_symbol = 1;}
        length++;
    }
    return has_upper && has_lower && has_digit && has_symbol && (length >= 8);
}

int main() {
    char password[100];
    int valid = 0;
    while (!valid) {
        printf("Enter password: ");
        scanf("%99s", password);
        printf("You entered: %s\n", password);
        if (is_valid_password(password)) {
            printf("Password is valid.\n");
            valid = 1;
        } else {
            printf("Password is invalid.\n");
        }
    }
    return 0;
}