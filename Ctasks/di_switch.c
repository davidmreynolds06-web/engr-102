 #include "stm32f4xx.h"

volatile uint32_t msTicks = 0;
volatile uint8_t ledState = 0;

void SysTick_Handler(void) { 
msTicks++;
}
void initializeSysTick() {
 // Configure SysTick to generate interrupt every 1 ms
    SysTick_Config(SystemCoreClock / 1000);
}
void initializeGPIO(){
 // Initialize PA5 as output for LED
    GPIOA->MODER |= (1 << (5 * 2)); // Set PA5 to output mode
 // Initialize PC13 as input for button
    GPIOC->MODER &= ~(3 << (13 * 2)); // Set PC13 to input mode
    GPIOC->PUPDR |= (2 << (13 * 2)); // Enable pull-down resistor on PC13
}
void checkButton() {
 // Check button state and update ledState
    if (!(GPIOC->IDR & (1 << 13))) { // Button pressed (active low)
        ledState = (ledState + 1) % 3; // Cycle through 3 states
        while (!(GPIOC->IDR & (1 << 13))); // Wait for button release
    }
}
void updateLEDPattern(){
 // Implement LED patterns based on ledState
    static uint32_t lastTick = 0;
    switch (ledState) {
        case 0: // LED off
            GPIOA->ODR &= ~(1 << 5);
            break;
        case 1: // LED on
            GPIOA->ODR |= (1 << 5);
            break;
        case 2: // LED blink
            if (msTicks - lastTick >= 500) { // Toggle every 500 ms
                GPIOA->ODR ^= (1 << 5);
                lastTick = msTicks;
            }
        break;
    }
}
int main(void) {
    initializeGPIO();
    initializeSysTick();
    while (1) {
        checkButton();
        updateLEDPattern();
    }
return 0;
}