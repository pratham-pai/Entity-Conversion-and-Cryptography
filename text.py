from qr import convert_qr
from speech import convert_speech
from base import convert_base
from caesar import convert_caesar
from vigenere import convert_vigenere
from rail_fence import convert_rail_fence
from atbash import convert_atbash
from morse import convert_morse
from braille import convert_braille
from roman import convert_roman

def convert_text():
    while True:
        print("Welcome to the Text Conversion Tool!")
        print("1. Text to QR Code")
        print("2. Text to Speech")
        print("3. Base Conversion")
        print("4. Caesar Cipher")
        print("5. Vigenère Cipher")
        print("6. Rail Fence Cipher")
        print("7. Atbash Cipher")
        print("8. Morse Code")
        print("9. Braille")
        print("10. Roman Numerals")
        print("11. Exit")
        
        mode = input("Enter choice (1-10): ")
        
        if mode == "1":
            convert_qr()
        elif mode == "2":
            convert_speech()
        elif mode == "3":
            convert_base()
        elif mode == "4":
            convert_caesar()
        elif mode == "5":
            convert_vigenere()
        elif mode == "6":
            convert_rail_fence()
        elif mode == "7":
            convert_atbash()
        elif mode == "8":
            convert_morse()
        elif mode == "9":
            convert_braille()
        elif mode == "10":
            convert_roman()
        elif mode == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")