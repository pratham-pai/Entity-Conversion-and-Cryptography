morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
        '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char  # Preserve characters not in the dictionary
    return morse_code.strip()

def morse_to_text(morse_code):
    morse_code_reverse_dict = {value: key for key, value in morse_code_dict.items()}
    morse_code_list = morse_code.split(' ')
    text = ''
    for code in morse_code_list:
        if code in morse_code_reverse_dict:
            text += morse_code_reverse_dict[code]
        else:
            text += code  # Preserve Morse code sequences not in the dictionary
    return text


def convert_morse():
    while True:
        print("Welcome to the Morse Code Conversion Tool!")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        mode = input("Enter choice (1-3): ")
        
        if mode == '1':
            text = input("Enter text: ")
            print("Morse code:", text_to_morse(text))
        elif mode == '2':
            morse = input("Enter morse code: ")
            print("Text:", morse_to_text(morse))
        elif mode == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
            