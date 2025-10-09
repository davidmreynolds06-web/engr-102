#include <stdio.h>

int main() {
    
 #define PIN 6457
 #define INITIAL_BALANCE 5000
 int entered_pin, choice;
 float balance = INITIAL_BALANCE;

    printf("Enter your PIN: ");
    scanf("%d", &entered_pin);

    if (entered_pin != PIN) {
        printf("Invalid PIN. Access denied.\n");
        return 1;
    }
    else {
        printf("\n1. Withdraw\n");
        printf("2. Deposit\n");
        printf("3. Quit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
				printf("You selected: %d", choice);
        while (choice != 3) {
			if (choice == 1) {
                float amount;
                printf("Enter amount to withdraw: ");
                scanf("%f", &amount);
                if (amount > balance) {
                printf("Insufficient funds. Transaction cancelled.\n");
            } else {
                printf("$Amount to withdraw: $%.2f\n", amount);
                balance -= amount;
                printf("Withdrawal successful. New balance: $%.2f\n", balance);
            }
			} else if (choice == 2) {
                float amount;
                printf("Enter amount to deposit: ");
                scanf("%f", &amount);
				printf("$Amount to deposit: $%.2f\n", amount);
                balance += amount;
                printf("Deposit successful. New balance: $%.2f\n", balance);
			} else {
                printf("Invalid choice. Please try again.\n");
            }
			printf("Enter your choice: ");
			scanf("%d", &choice);
			printf("You selected: %d", choice);
        } printf("Thank you for using the ATM. Goodbye!\n");
        
    }

  return 0;
}