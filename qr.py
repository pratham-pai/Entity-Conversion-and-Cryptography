import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    print("Please select the destination folder to save the QR Code:")
    root = tk.Tk()
    root.withdraw()
    try:
        output_dir = filedialog.askdirectory()
        if output_dir:  # Check if a directory is selected
            file_path = output_dir + "/" + file_name  # Combine directory and file name
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(file_path)
            print(f"QR code generated and saved as {file_path}")
        else:
            print("Folder selection cancelled. QR code generation aborted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        root.destroy()


def convert_qr():
    while True:
        print("Welcome to QR Code Generator:") 
        print("1. Generate QR Code")
        print("2. Exit")
        print("Please select an option(1-2):")
        option = int(input())
        if option == 1:
            text = input("Enter the text to be converted: ")
            file_name = "qr_code.jpg"
            generate_qr_code(text, file_name)
        elif option == 2:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

convert_qr()