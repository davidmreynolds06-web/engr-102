#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

 #define MAX_LENGTH 100

 // Function to flush ITM buffers
 void flushITM(void) {
 fflush(stdout);
 fflush(stderr);
}
 
 // Function to read a character from ITM and echo it back
int readCharITM(void) {
    int c = getchar();
    if (c != EOF && c != '\n' && c != '\r') {
        putchar(c); // Echo the character
    }
    flushITM();
    return c;
}
 



 
 // Function to read a string from ITM with a maximum length
void readStringITM(char* str, int maxLen) {
    int i = 0;
    int c;
    printf("Start typing (press Enter when done):\n");
    flushITM();
    while (i < maxLen - 1) {
        c = readCharITM();
        if (c == '\n' || c == '\r' || c == EOF) {
            break;
        }
        str[i++] = (char)c;
    }
    str[i] = '\0';
    flushITM();
}

// Function to process the string based on the user's option
void processString(int option, char* str) {
    // Implement string processing logic based on the selected option
    switch (option) {
        case 1: // Capital all letters
            for (int i = 0; str[i] != '\0'; i++) {
                str[i] = toupper(str[i]);
            }
            printf("Capitalized String: %s\n", str);
            flushITM();
            break;
        case 2: { // Count number of letters
            int count = 0;
            for (int i = 0; str[i] != '\0'; i++) {
                if (isalpha(str[i])) {
                    count++;
                }
            }
            printf("Number of letters: %d\n", count);
            flushITM();
            break;
        }
        case 3: // Lowercase all letters
            for (int i = 0; str[i] != '\0'; i++) {
                str[i] = tolower(str[i]);
            }
            printf("Lowercased String: %s\n", str);
            flushITM();
            break;
        case 4: { // Replace String
            char newStr[MAX_LENGTH];
            printf("Enter new string to replace the current one:\n");
            flushITM();
            readStringITM(newStr, MAX_LENGTH);
            strcpy(str, newStr);
            printf("String replaced. New String: %s\n", str);
            flushITM();
            break;
        }
        default:
            printf("Invalid option selected.\n");
            flushITM();
            break;
    }
    // Remember to use flushITM() after printf statements
}

// Function to read menu option from ITM
int readOptionITM(void) {
    char optionStr[10] = {0};
    int i = 0, c;
    printf("Enter option (1-5): ");
    flushITM();
    while (i < 9) {
        c = readCharITM();
        if (c == '\n' || c == '\r' || c == EOF) {
            break;
        }
        optionStr[i++] = (char)c;
    }
    optionStr[i] = '\0';
    flushITM();
    return atoi(optionStr);
}
int main() {
    char str[MAX_LENGTH];
    int option;
    printf("Enter a string:\n");
    flushITM();
    readStringITM(str, MAX_LENGTH);
    do {
        // Display menu
        printf("\nMenu:\n");
        printf("1. Capital all letters\n");
        printf("2. Count number of letters\n");
        printf("3. Lowercase all letters\n");
        printf("4. Replace String\n");
        printf("5. Exit\n");
        flushITM();
        // Use readOptionITM() to get user's choice
        option = readOptionITM();
        // Call processString() if option is not exit
        if (option >= 1 && option <= 4) {
            processString(option, str);
        }
        // Remember to use flushITM() after printf statements
    } while (option != 5);
    return 0;
}
