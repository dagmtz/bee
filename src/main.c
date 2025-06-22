// Main application for blinking an LED on ATmega328P (like Arduino Pin 13)
#include <avr/io.h>
#include "delay_lib.h"
#include "led_control.h"

int main(void) {
    // Initialize the LED pin (PB5, equivalent to Arduino digital pin 13)
    LED_init();

    while (1) {
        // Toggle the LED on
        LED_toggle();
        // Wait for 500 milliseconds
        delay_ms(500);

        // Toggle the LED off (it's a toggle, so calling it again turns it off)
        LED_toggle();
        // Wait for another 500 milliseconds
        delay_ms(500);
    }
    return 0; // Should never be reached
}
