import os
import shutil
import tkinter as tk
from tkinter import filedialog

import zipfile # Zip Conversion
import rarfile # Rar Conversion
import py7zr # 7z Conversion
import tarfile # Tar Conversion
import gzip # Gzip Conversion
import bz2 # Bzip2 Conversion
import pycabinet # Cab Conversion

def convert_archive():
    print("Welcome to the Archive Conversion Tool!")
    
    # Browse for input file
    print("Please select the input archive file to convert")
    root = tk.Tk()
    root.withdraw()
    input_path = filedialog.askopenfilename()
    root.destroy()  # Close the Tkinter window after file selection

    if not input_path:
        print("No input file selected. Please try again.")
        return

    output_format = input("Enter the output format (ZIP, RAR, 7Z, TAR, GZIP, BZIP2, CAB): ").upper()

    # Browse for the output folder
    print("Please select the destination folder to save the converted archive file:")
    root = tk.Tk()
    root.withdraw()
    output_folder = filedialog.askdirectory()
    root.destroy()  # Close the Tkinter window after folder selection

    if not output_folder:
        print("No output folder selected. Please try again.")
        return
    
    supported_formats = ['ZIP', 'RAR', '7Z', 'TAR', 'GZIP', 'BZIP2', 'CAB']
    if output_format not in supported_formats:
        print("Unsupported output format.")
        return

    try:
        # Construct the output file path
        output_extension = output_format.lower()
        output_file = os.path.splitext(os.path.basename(input_path))[0] + '.' + output_extension
        output_path = os.path.join(output_folder, output_file)

        # Perform the archive conversion
        if output_extension == 'zip':
            with zipfile.ZipFile(output_path, 'w') as zipf:
                zipf.write(input_path, os.path.basename(input_path))
        elif output_extension == 'rar':
            with rarfile.RarFile(output_path, 'w') as rarf:
                rar_info = rarfile.RarInfo(input_path)
                rar_info.filename = os.path.basename(input_path)
                rar_info.file_size = os.path.getsize(input_path)
                rar_info.compress_size = rar_info.file_size
                rar_info.flag_bits = 0x20
                rar_info.create_system = 3
                rar_info.volume = 1
                rar_info.CRC = rarfile._CRC32(input_path)
                rar_info.compress_type = rarfile.RAR_COMPRESSION_STORE
                rar_info.header_crc = rarfile._CRC32(input_path)
                rar_info.compress()
                rar_info.create_header()
                rar_info.write_header(rarf)
                with open(input_path, 'rb') as file:
                    rar_info.file.seek(0, 2)
                    rar_info.data_position = rar_info.file.tell()
                    rar_info.file.seek(rar_info.header_offset, 0)
                    rar_info.file.write(file.read())
        elif output_extension == '7z':
            with py7zr.SevenZipFile(output_path, 'w') as szf:
                szf.write(input_path, os.path.basename(input_path))
        elif output_extension == 'tar':
            with tarfile.open(output_path, 'w') as tarf:
                tarf.add(input_path, arcname=os.path.basename(input_path))
        elif output_extension == 'gzip':
            with open(input_path, 'rb') as f_in, gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        elif output_extension == 'bzip2':
            with open(input_path, 'rb') as f_in, bz2.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        elif output_extension == 'cab':
            pycabinet.create_cabinet(input_path, output_path)
        else:
            print("Unsupported output format.")
            return

        print(f"Conversion successful: {os.path.basename(input_path)} -> {output_path}")
    except Exception as e:
        print(f"Conversion failed: {e}")

