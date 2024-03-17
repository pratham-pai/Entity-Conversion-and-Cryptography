from get import get_integer
def encrypt_rail_fence(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0
    
    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        fence[row][col] = char
        col += 1
        if direction_down:
            row += 1
        else:
            row -= 1
    
    encrypted_text = ''
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                encrypted_text += fence[i][j]
    return encrypted_text


def decrypt_rail_fence(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0
    
    for char in text:
        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False
        
        fence[row][col] = '*'
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if (fence[i][j] == '*') and (index < len(text)):
                fence[i][j] = text[index]
                index += 1
    
    decrypted_text = ''
    row, col = 0, 0
    for _ in range(len(text)):
        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False
        
        if fence[row][col] != '*':
            decrypted_text += fence[row][col]
            col += 1
            
        if direction_down:
            row += 1
        else:
            row -= 1
    
    return decrypted_text


def convert_rail_fence():
    while True:
        print("\nRail Fence Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            rails = get_integer("Enter the number of rails: ")
            encrypted_text = encrypt_rail_fence(text, rails)
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            rails = get_integer("Enter the number of rails: ")
            decrypted_text = decrypt_rail_fence(text, rails)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

