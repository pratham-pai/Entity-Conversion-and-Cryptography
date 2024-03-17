def roman_to_number(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_numerals[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

def number_to_roman(number):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, symbol in roman_numerals:
        while number >= value:
            result += symbol
            number -= value
    return result

def convert_roman():
    while True:
        print("Welcome to the Roman Numeral Converter!")
        print("1. Convert decimal to roman")
        print("2. Convert roman to decimal")
        print("3. Quit")
        mode = input("Enter choice (1-3): ")
        
        
        if mode == "1":
            decimal_number = int(input("Enter a decimal number below 3999: "))
            roman = number_to_roman(decimal_number)
            print(f"The decimal number {decimal_number} is equal to the Roman numeral '{roman}'.")
        elif mode == "2":
            roman_numeral = input("Enter a Roman numeral: ")
            number = roman_to_number(roman_numeral)
            print(f"The Roman numeral '{roman_numeral}' is equal to {number} in decimal.")
        elif mode == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
