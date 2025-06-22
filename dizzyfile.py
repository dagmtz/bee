# Dizzy configuration for the ATmega328P blink project
import os
import subprocess
import shutil

# Define the build directory
BUILD_DIR = "build"

def clean():
    """
    Cleans the build directory.
    """
    print(f"Cleaning build directory: {BUILD_DIR}")
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    print("Clean complete.")

def build():
    """
    Configures the project with CMake and builds it with Ninja.
    """
    print("Starting build process...")

    # Create the build directory if it doesn't exist
    os.makedirs(BUILD_DIR, exist_ok=True)

    # Step 1: Configure CMake
    # CMake will generate the Ninja build files in the BUILD_DIR
    print("Configuring CMake...")
    cmake_command = [
        "cmake",
        "-S", ".",  # Source directory (current directory)
        "-B", BUILD_DIR, # Binary (build) directory
        "-G", "Ninja"   # Generator: Use Ninja
    ]
    try:
        subprocess.run(cmake_command, check=True, cwd=os.getcwd())
        print("CMake configuration successful.")
    except subprocess.CalledProcessError as e:
        print(f"CMake configuration failed: {e}")
        return

    # Step 2: Build the project using Ninja
    print("Building with Ninja...")
    ninja_command = [
        "ninja",
        "-C", BUILD_DIR # Change directory to BUILD_DIR for ninja
    ]
    try:
        subprocess.run(ninja_command, check=True, cwd=os.getcwd())
        print("Ninja build successful. Firmware generated in 'build' directory.")
    except subprocess.CalledProcessError as e:
        print(f"Ninja build failed: {e}")
        return

def flash():
    """
    Flashes the compiled firmware (blink.hex) to the ATmega328P using avrdude.
    This assumes you have avrdude installed and your programmer/USB-to-serial is correctly set up.
    You might need to adjust the programmer type (-c) and port (-P).
    Common values for Arduino Uno: -c arduino -P /dev/ttyUSB0 or /dev/ttyACM0
    """
    print("Attempting to flash firmware...")
    hex_file = os.path.join(BUILD_DIR, "blink.hex")

    if not os.path.exists(hex_file):
        print(f"Error: {hex_file} not found. Please build the project first.")
        return

    # Example avrdude command for Arduino Uno (check your port and programmer type)
    # Common programmer types: 'arduino' (for serial bootloader), 'usbasp', 'avrisp', 'stk500v1'
    # Common ports: '/dev/ttyUSB0', '/dev/ttyACM0' (Linux), 'COMx' (Windows)
    avrdude_command = [
        "avrdude",
        "-C", "/etc/avrdude.conf", # Path to avrdude.conf (might be different on your system)
        "-v",                      # Verbose output
        "-patmega328p",            # Microcontroller part
        "-c", "arduino",           # Programmer type (e.g., 'arduino' for Uno bootloader)
        "-P", "/dev/ttyACM0",      # Port (check your system: ls /dev/tty* or dmesg after plugging in)
        "-b", "115200",            # Baud rate (for serial programmers)
        "-D",                      # Disable auto erase for flash
        "-U", f"flash:w:{hex_file}:i" # Write flash memory with the hex file
    ]

    print(f"Executing: {' '.join(avrdude_command)}")
    try:
        subprocess.run(avrdude_command, check=True)
        print("Flashing successful!")
    except subprocess.CalledProcessError as e:
        print(f"Flashing failed: {e}")
    except FileNotFoundError:
        print("Error: avrdude command not found. Please ensure avrdude is installed and in your PATH.")


# Dizzy entry points
# You can run 'dizzy clean', 'dizzy build', 'dizzy flash'
commands = {
    "clean": clean,
    "build": build,
    "flash": flash,
}
