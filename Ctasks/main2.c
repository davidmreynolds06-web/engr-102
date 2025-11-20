 #include "stm32f4xx.h"
 void initializeLED() {
 // Initialize PA5 as output
 RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN; // Enable clock for GPIOA
 GPIOA->MODER |= GPIO_MODER_MODER5_0; // Set PA5 as output
 }
 void setLED(int state) {
 if (state) {
 GPIOA->ODR |= GPIO_ODR_OD5; // Turn on LED
 } else {
 GPIOA->ODR &= ~GPIO_ODR_OD5; // Turn off LED
 }
 }
 void delay(int milliseconds) {
 // Simple software delay
 for (volatile int i = 0; i < milliseconds * 1000; i++);
 }
int main(void) {
 initializeLED();
 while (1) {
 // Implement slow blinking for 5 seconds
    setLED(1);
    delay(5000);
    setLED(0);
    delay(5000);

 // Implement fast blinking for 5 seconds
    for (int i = 0; i < 5; i++) {
        setLED(1);
        delay(500);
        setLED(0);
        delay(500);
    }

 }
 }