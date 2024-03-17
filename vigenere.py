def encrypt_vigenere(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - 65
            if char.islower():
                ciphertext += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                ciphertext += chr(((ord(char) - 65 + shift) % 26) + 65)
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - 65
            if char.islower():
                plaintext += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                plaintext += chr(((ord(char) - 65 - shift) % 26) + 65)
            key_index += 1
        else:
            plaintext += char
    return plaintext

def convert_vigenere():
    while True:
        print("Welcome to the Caesar Cipher Tool!")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Quit")
        mode = input("Enter choice (1-3): ")
        if mode == '1':
            text = input("Enter the text to encrypt: ")
            key = input("Enter any string as key:")
            
            encrypted_text = encrypt_vigenere(text, key)
            
            print("Encrypted text:", encrypted_text)
            
        elif mode == '2':
            text = input("Enter the text to decrypt: ")
            key = input("Enter any string as key:")
            
            decrypted_text = decrypt_vigenere(text, key)
            
            print("Decrypted text:", decrypted_text)
            
        elif mode == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")