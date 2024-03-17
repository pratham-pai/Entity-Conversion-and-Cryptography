import pyttsx3
from browse import browse_for_file, browse_for_folder

def convert_speech():
    input_file = browse_for_file("txt")
    if input_file:
        with open(input_file, 'r') as file:
            text = file.read()
            engine = pyttsx3.init()
            output_file = browse_for_folder()
            if output_file:
                output_file += "/output.mp3"
                engine.save_to_file(text, output_file)
                engine.runAndWait()
                print(f"Text converted to speech and saved as {output_file}.")
