#include <stdio.h>
#include <string.h>

int main() {
    char login_name[20], password[20], correct_login[] = "Admin", correct_password[] = "PASS";
    printf("Enter login name: ");
    scanf("%s", login_name);
    printf("Enter password: ");
    scanf("%s", password);
    // Compare input with correct credentials
    if (strcmp(login_name, correct_login) == 0 && strcmp(password, correct_password) == 0) {
        printf("Login Complete\n");
    } else {
        // Display appropriate error message
        printf("Login Failed\n");
    }

}