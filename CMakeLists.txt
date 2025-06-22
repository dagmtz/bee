# Root CMake file for the ATmega328P blink project

# Minimum CMake version required
cmake_minimum_required(VERSION 3.10)

# Define the project name and language(s)
project(ATmegaBlink C)

# Specify the toolchain file for cross-compilation
# This file tells CMake how to find the AVR-GCC compiler and tools
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_CURRENT_SOURCE_DIR}/toolchain-atmega328p.cmake)

# Set the C standard (optional, but good practice)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Add the include directory for our custom libraries
include_directories(src/include)

# Add the executable target. This defines the final firmware file (.elf)
# We list all source files that make up our application
add_executable(blink.elf
    src/main.c
    src/delay_lib.c
    src/led_control.c
)

# --- AVR-Specific Compiler and Linker Options ---

# Common compiler options for ATmega328P
# -mmcu=atmega328p: Specifies the target microcontroller
# -DF_CPU=16000000UL: Defines the CPU frequency for delay functions (16MHz for Arduino Uno)
# -Os: Optimize for size (important for embedded systems with limited memory)
# -Wall -Wextra: Enable common warnings for better code quality
target_compile_options(blink.elf PRIVATE
    -mmcu=atmega328p
    -DF_CPU=16000000UL
    -Os
    -Wall
    -Wextra
)

# Common linker options for ATmega328P
# -mmcu=atmega328p: Specifies the target microcontroller
# -Wl,-gc-sections: Garbage collection of unused sections (reduces final binary size)
# -Wl,-Map=blink.map: Generates a map file showing memory usage
target_link_options(blink.elf PRIVATE
    -mmcu=atmega328p
    -Wl,--gc-sections
    -Wl,-Map=blink.map
)

# --- Post-Build Commands for Firmware Generation ---

# Add a custom command to generate the Intel HEX file (.hex) from the .elf
# This .hex file is what you typically flash to the microcontroller
add_custom_command(
    TARGET blink.elf
    POST_BUILD
    COMMAND avr-objcopy -O ihex -R .eeprom $< TARGET_FILE_DIR>/blink.hex
    COMMENT "Generating blink.hex from blink.elf"
)

# Optionally, add a command to generate the EEPROM file (.eep) if your project uses EEPROM
# For a simple blink, this might not be strictly necessary, but it's good practice.
add_custom_command(
    TARGET blink.elf
    POST_BUILD
    COMMAND avr-objcopy -O ihex -j .eeprom --no-change-warnings --change-section-lma .eeprom=0 $< TARGET_FILE_DIR>/blink.eep
    COMMENT "Generating blink.eep from blink.elf (if EEPROM is used)"
)

# Add a custom command to get the size information of the generated firmware
# This helps in knowing how much flash/RAM the code consumes
add_custom_command(
    TARGET blink.elf
    POST_BUILD
    COMMAND avr-size --format=avr --mcu=atmega328p $<
    COMMENT "Getting size information for blink.elf"
)
