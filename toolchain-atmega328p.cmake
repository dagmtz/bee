# CMake toolchain file for AVR (ATmega328P) cross-compilation

# Specify the system name as Generic for cross-compilation
set(CMAKE_SYSTEM_NAME Generic)
# Specify the processor architecture
set(CMAKE_SYSTEM_PROCESSOR avr)

# Do not search for programs and libraries in the build tree
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# Only search for libraries and headers in the target environment
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# Define the paths to the AVR GNU toolchain executables
# These paths assume avr-gcc is in your system's PATH.
# If not, you might need to specify full paths, e.g., /usr/bin/avr-gcc
set(CMAKE_C_COMPILER   avr-gcc)
set(CMAKE_CXX_COMPILER avr-g++) # Even if only C is used, it's good to define
set(CMAKE_ASM_COMPILER avr-gcc) # For assembly files
set(CMAKE_OBJCOPY      avr-objcopy)
set(CMAKE_SIZE         avr-size)
set(CMAKE_AR           avr-ar)

# Set common flags for the C compiler for AVR
set(CMAKE_C_FLAGS_INIT "${CMAKE_C_FLAGS_INIT} -std=gnu11") # Use GNU C11 dialect
set(CMAKE_C_FLAGS_INIT "${CMAKE_C_FLAGS_INIT} -fpack-struct -fshort-enums") # Optimization
set(CMAKE_C_FLAGS_INIT "${CMAKE_C_FLAGS_INIT} -funsigned-char -funsigned-bitfields") # Treat char as unsigned

# Set common flags for the linker for AVR
# -Wl,--gc-sections is added in CMakeLists.txt target_link_options
set(CMAKE_EXE_LINKER_FLAGS_INIT "${CMAKE_EXE_LINKER_FLAGS_INIT} -fuse-linker-app=avr") # For avr-gcc linker

