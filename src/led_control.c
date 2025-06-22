// LED control library implementation for ATmega328P (PB5)
#include "led_control.h"
#include <avr/io.h> // For DDRB, PORTB

// Initialize the LED pin as an output
void LED_init(void) {
    // Set PB5 (digital pin 13 on Arduino Uno) as an output
    DDRB |= (1 << PB5);
}

// Toggle the state of the LED pin
void LED_toggle(void) {
    // Toggle PB5 using XOR assignment
    PORTB ^= (1 << PB5);
}
