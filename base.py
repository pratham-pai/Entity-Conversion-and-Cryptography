def text_to_binary(text):
    binary_str = ' '.join(format(ord(char), '08b') for char in text)
    return binary_str

def binary_to_text(binary_str):
    text = ''.join(chr(int(binary, 2)) for binary in binary_str.split())
    return text

def text_to_hexadecimal(text):
    hex_str = ''.join(format(ord(char), '02x') for char in text)
    return hex_str

def hexadecimal_to_text(hex_str):
    text = ''.join(chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2))
    return text

def binary_to_hexadecimal(binary_str):
    text = binary_to_text(binary_str)
    hex_str = text_to_hexadecimal(text)
    return hex_str

def hexadecimal_to_binary(hex_str):
    text = hexadecimal_to_text(hex_str)
    binary_str = text_to_binary(text)
    return binary_str


def is_binary(input_str):
    return all(bit == '0' or bit == '1' or bit == " " for bit in input_str)

def get_binary_input():
    while True:
        binary_input = input("Enter a binary number: ")
        if is_binary(binary_input):
            return binary_input
        else:
            print("Error: Input must contain only 0s and 1s. Please try again.")


def is_hexadecimal(input_str):
    hexadecimal_digits = set('0123456789ABCDEF')
    return all(char.upper() in hexadecimal_digits for char in input_str)

def get_hexadecimal_input():
    while True:
        hexadecimal_input = input("Enter a hexadecimal number: ")
        if is_hexadecimal(hexadecimal_input):
            return hexadecimal_input
        else:
            print("Error: Input must contain valid hexadecimal digits (0-9, A-F). Please try again.")


def convert_base():
    while True:
        print("Welcome to the Base Converter!")
        print("1. Decimal (Base 10) to Binary (Base 2)")
        print("2. Binary (Base 2) to Decimal (Base 10)")
        print("3. Decimal (Base 10) to Hexadecimal (Base 16)")
        print("4. Hexadecimal (Base 16) to Decimal (Base 10)")
        print("5. Binary (Base 2) to Hexadecimal (Base 16)")
        print("6. Hexadecimal (Base 16) to Binary (Base 2)")
        print("7. Exit")
        
        mode = input("Enter choice (1-7): ")

        if mode == "1":
            text = input("Enter normal text: ")
            binary = text_to_binary(text)
            print("Text to Binary:", binary)
        elif mode == "2":
            binary = get_binary_input()
            text_decoded = binary_to_text(binary)
            print("Binary to Text:", text_decoded)
        elif mode == "3":
            text = input("Enter normal text: ")
            hexadecimal = text_to_hexadecimal(text)
            print("Text to Hexadecimal:", hexadecimal)
        elif mode == "4":  
            hexadecimal = get_hexadecimal_input()
            text_decoded_hex = hexadecimal_to_text(hexadecimal)
            print("Hexadecimal to Text:", text_decoded_hex)
        elif mode == "5":
            binary = get_binary_input()
            binary_to_hex = binary_to_hexadecimal(binary)
            print("Binary to Hexadecimal:", binary_to_hex)
        elif mode == "6":
            hexadecimal = get_hexadecimal_input()
            hex_to_binary = hexadecimal_to_binary(hexadecimal)
            print("Hexadecimal to Binary:", hex_to_binary)
        elif mode == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
