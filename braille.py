# Dictionary mapping English letters to Braille
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
    'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
    'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
    's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵',
    
    '0': '⠚', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊',
    
    '.': '⠲', ',': '⠂', ';': '⠆', ':': '⠒', '?': '⠢', '!': '⠖',
    "'": '⠄', '"': '⠐', '-': '⠤', '(': '⠴', ')': '⠶', '[': '⠦',
    ']': '⠲', '{': '⠐⠣', '}': '⠐⠜', '*': '⠔', '/': '⠤⠖', '\\': '⠤⠦',
    '@': '⠈⠢', '&': '⠈⠯', '#': '⠼⠴', '%': '⠼⠶', '+': '⠤⠤', '=': '⠤⠤⠤',
    '<': '⠤⠞', '>': '⠤⠘', '$': '⠸⠌', '^': '⠸⠡', '_': '⠤⠤⠤⠤'
}


# Function to convert text to Braille
def text_to_braille(text):
    braille_text = ''
    for char in text:
        if char.lower() in braille_dict:
            braille_text += braille_dict[char.lower()]
        else:
            braille_text += char  # Preserve characters not found in the dictionary
    return braille_text

# Function to convert Braille to text
def braille_to_text(braille_text):
    braille_reverse_dict = {value: key for key, value in braille_dict.items()}
    text = ''
    for char in braille_text:
        if char in braille_reverse_dict:
            text += braille_reverse_dict[char]
        else:
            text += char  # Preserve characters not found in the dictionary
    return text

def convert_braille():
    while True:
        print("Welcome to the Braille Conversion Tool!")
        print("1. Text to Braille")
        print("2. Braille to Text")
        print("3. Exit")
        
        mode = input("Enter choice (1-3): ")
        
        if mode == "1":
            text = input("Enter the text: ")
            braille_text = text_to_braille(text)
            print("Text to Braille:", braille_text)
        elif mode == "2":
            braille_text = input("Enter the braille text: ")
            text = braille_to_text(braille_text)
            print("Braille to Text:", text)
        elif mode == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
