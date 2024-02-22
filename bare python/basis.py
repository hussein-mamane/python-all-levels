# Define numbers in different bases
binary_number = 0b1010
octal_number = 0o123
hexadecimal_number = 0xABCD
decimal_number = 1234

# Convert between bases
print("Binary:", bin(decimal_number))  # Convert decimal to binary
print("Octal:", oct(decimal_number))  # Convert decimal to octal
print("Hexadecimal:", hex(decimal_number))  # Convert decimal to hexadecimal
print("Decimal:", int('1010', 2))  # Convert binary to decimal

# Bitwise operations
num1 = 0b1010
num2 = 0b1100

print("Bitwise AND:", bin(num1 & num2))  # Bitwise AND
print("Bitwise OR:", bin(num1 | num2))  # Bitwise OR
print("Bitwise XOR:", bin(num1 ^ num2))  # Bitwise XOR
print("Bitwise NOT:", bin(~num1))  # Bitwise NOT
print("Left Shift:", bin(num1 << 2))  # Left shift
print("Right Shift:", bin(num1 >> 2))  # Right shift

# set some bits to 0 according to a mask where we put
# 1 on the wanted bits position bs=bit_set
import sys


def bs(x, bitmask):
    return bin(x & (~bitmask))


# extract the values of some bits be = bit_ext


def be(x, bitmask):
    return bin(x & bitmask)


x = 0b1010
# print(be(x, 0b0010))
# print(bs(x, 0b1101))

print(int('0b1101', base=2))
print(int('234', base=8))
