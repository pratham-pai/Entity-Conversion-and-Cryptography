import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image # Image conversion

def convert_image():
    print("Welcome to the Image Conversion Tool!")
    
    # Display the available image formats
    supported_formats = ['.jpg', '.jpeg', '.png', '.pdf', '.webp', '.bmp', '.tiff', '.ico', '.gif']
    print("Supported file formats for conversion:")
    for format in supported_formats:
        print(format)
    print("Please select the image file to convert")
    root = tk.Toplevel()
    root.withdraw()
    input_path = filedialog.askopenfilename()
    root.destroy()  # Close the Tkinter window after file selection

    if not input_path:
        print("No file selected. Please try again.")
        return

    filename, ext = os.path.splitext(input_path)

    supported_formats = ['.jpg', '.jpeg', '.png', '.pdf', '.webp', '.bmp', '.tiff', '.ico', '.gif']

    if ext.lower() not in supported_formats:
        print("Unsupported file format for conversion.")
        return

    output_format = input("Enter the output format (JPEG, PNG, PDF, WEBP, BMP, TIFF, ICO, GIF): ").upper()
    if output_format not in ['JPEG', 'PNG', 'PDF', 'WEBP', 'BMP', 'TIFF', 'ICO', 'GIF']:
        print("Unsupported output format.")
        return

    # Output directory
    print("Please select the destination folder to save the converted image file:")
    root = tk.Tk()
    root.withdraw()
    output_dir = filedialog.askdirectory()
    root.destroy()
    os.makedirs(output_dir, exist_ok=True)

    output_file = f"{os.path.basename(filename)}.{output_format.lower()}"
    output_path = os.path.join(output_dir, output_file)

    try:
        image = Image.open(input_path)
        image.save(output_path, format=output_format, quality=100)
        print(f"Conversion successful: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Conversion failed: {e}")
