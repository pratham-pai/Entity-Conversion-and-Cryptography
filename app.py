from text import convert_text
from unit import convert_unit
from file import convert_file

def main():
    while True:
        print("\nMenu:") 
        print("1. Text Conversion and Cryptography")
        print("2. Unit Conversion")
        print("3. File Format Conversion")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            convert_text()

        elif choice == "2":
            convert_unit()

        elif choice == "3":
            convert_file()
        
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
