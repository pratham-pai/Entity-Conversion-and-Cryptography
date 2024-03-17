def atbash(text):                
    result = ""
    for char in text:
        # For uppercase letters
        if char.isupper():
            result += chr(90 - (ord(char) - 65))
        # For lowercase letters
        elif char.islower():
            result += chr(122 - (ord(char) - 97))
        # For non-alphabetic characters
        else:
            result += char
    return result

def convert_atbash():
    while True:
        print("Welcome to the Atbash Cipher Tool!")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Quit")
        mode = input("Enter choice (1-3): ")

        if mode == '1':
            text = input("Enter any string to encrypt: ")
            encrypted_text = atbash(text)
            print("Encrypted:", encrypted_text)
            
        elif mode == '2':
            text = input("Enter any string to decrypt: ")
            decrypted_text = atbash(text)
            print("Decrypted:", decrypted_text)
            
        elif mode == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

# No key required, atbash is just reverse alphabet 
