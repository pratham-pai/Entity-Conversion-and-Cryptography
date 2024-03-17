import os
import tkinter as tk
from tkinter import filedialog

from moviepy.editor import VideoFileClip # Video Conversion


def convert_video():
    print("Welcome to the Video Conversion Tool!")

    # Ask for input file path
    print("Please select the input video file to convert")
    root = tk.Toplevel()
    root.withdraw()
    input_path = filedialog.askopenfilename()
    root.destroy()  # Close the Tkinter window after file selection

    if not input_path:
        print("No input file selected. Please try again.")
        return

    # Ask for output format
    output_format = input("Enter the output format (MP4, MKV, MOV, AVI, WEBM, GIF, WMV, FLV): ").upper()

    supported_formats = ['MP4', 'MKV', 'MOV', 'AVI', 'WEBM', 'GIF', 'WMV', 'FLV']
    if output_format not in supported_formats:
        print("Unsupported output format.")
        return

    # Browse for the output folder
    print("Please select the destination folder to save the converted video file:")
    root = tk.Toplevel()
    root.withdraw()
    output_folder = filedialog.askdirectory()
    root.destroy()  # Close the Tkinter window after folder selection

    if not output_folder:
        print("No output folder selected. Please try again.")
        return

    try:
        # Load the input video clip
        clip = VideoFileClip(input_path)

        # Ask for quality/bitrate
        quality = input("Enter the quality (low, medium, high) or bitrate (in kbps) for the output video: ")

        # Set the bitrate for the converted video
        if quality.isdigit():
            bitrate = f'{quality}k'  # Use the specified bitrate
        elif quality.lower() == 'low':
            bitrate = '500k'  # Low quality bitrate
        elif quality.lower() == 'medium':
            bitrate = '1000k'  # Medium quality bitrate
        elif quality.lower() == 'high':
            bitrate = '2000k'  # High quality bitrate
        else:
            print("Invalid quality/bitrate input. Using default bitrate.")
            bitrate = '1000k'  # Default bitrate

        # Construct the output file path
        output_extension = output_format.lower()
        output_file = os.path.splitext(os.path.basename(input_path))[0] + '.' + output_extension
        output_path = os.path.join(output_folder, output_file)

        # Convert the video to GIF
        if output_extension == 'gif':
            clip.write_gif(output_path)
        else:
            # Set the codec based on the output format
            codec = None
            if output_extension == 'mp4' or output_extension == 'mov' or output_extension == 'mkv':
                codec = 'libx264'  # H.264 codec
            elif output_extension == 'avi':
                codec = 'mpeg4'     # MPEG-4 Visual codec
            elif output_extension == 'webm':
                codec = 'libvpx'    # VP8 codec
            elif output_extension == 'flv':
                codec = 'flv'       # Flash Video codec
            
            if codec:
                clip.write_videofile(output_path, codec=codec)
                print(f"Conversion successful: {input_path} -> {output_path}")
            else:
                print("Unsupported output format.")
    except Exception as e:
        print(f"Conversion failed: {e}")
