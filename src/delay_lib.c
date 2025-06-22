// Simple delay library implementation
#include "delay_lib.h"
#include <avr/delay.h> // Provides _delay_ms

// Function to provide a delay in milliseconds
void delay_ms(unsigned long ms) {
    _delay_ms(ms);
}
