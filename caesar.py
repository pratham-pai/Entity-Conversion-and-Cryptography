from get import get_integer

def encrypt_caesar(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65) # add the key
            else:
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - key) % 26 + 65) # subtract the key
            else:
                decrypted_text += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text 

def convert_caesar():
    while True:
        print("Welcome to the Caesar Cipher Tool!")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Quit")
        mode = input("Enter choice (1-3): ")
        
        if mode == '1':
            text = input("Enter the text to encrypt: ")
            key = get_integer("Enter any number as key: ")
            encrypted_text = encrypt_caesar(text, key) 
            print("Encrypted text:", encrypted_text)
            
        elif mode == '2':
            text = input("Enter the text to decrypt: ")
            key = get_integer("Enter any number as key: ")
            decrypted_text = decrypt_caesar(text, key)
            print("Decrypted text:", decrypted_text)
            
        elif mode == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")
