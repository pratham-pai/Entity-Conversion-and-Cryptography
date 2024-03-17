import os
import tkinter as tk
from tkinter import filedialog

from moviepy.editor import AudioFileClip # Audio Conversion

def convert_audio():
    print("Welcome to the Audio Conversion Tool!")
    print("Please select the audio file to convert")
    root = tk.Toplevel()
    root.withdraw()
    input_path = filedialog.askopenfilename()
    root.destroy()  # Close the Tkinter window after file selection

    if not input_path:
        print("No input file selected. Please try again.")
        return

    output_format = input("Enter the output format (MP3, FLAC, WAV, OGG, AAC, M4A): ").upper()

    # Browse for the output folder
    print("Please select the destination folder to save the converted audio file:")
    root = tk.Toplevel()
    root.withdraw()
    output_folder = filedialog.askdirectory()
    root.destroy()  # Close the Tkinter window after folder selection

    if not output_folder:
        print("No output folder selected. Please try again.")
        return
    
    supported_formats = ['MP3', 'FLAC', 'WAV', 'OGG', 'AAC', 'M4A']
    if output_format not in supported_formats:
        print("Unsupported output format.")
        return

    try:
        # Load the input audio clip
        clip = AudioFileClip(input_path)

        # Get the original audio bitrate
        original_bitrate = clip.fps

        # Construct the output file path
        output_extension = output_format.lower()
        output_file = os.path.splitext(os.path.basename(input_path))[0] + '.' + output_extension
        output_path = os.path.join(output_folder, output_file)

        # Set the output format based on the file extension
        codec = None
        if output_extension == 'mp3':
            codec = 'libmp3lame'
        elif output_extension == 'flac':
            codec = 'flac'
        elif output_extension == 'wav':
            codec = 'pcm_s16le'
        elif output_extension == 'ogg':
            codec = 'libvorbis'
        elif output_extension == 'aac' or output_extension == 'm4a':
            codec = 'aac'
        
        if codec:
            clip.write_audiofile(output_path, codec=codec, bitrate=f"{original_bitrate}k")
            print(f"Conversion successful: {input_path} -> {output_path}")
        else:
            print("Unsupported output format.")
    except Exception as e:
        print(f"Conversion failed: {e}")
