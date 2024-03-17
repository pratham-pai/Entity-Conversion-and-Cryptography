from image import convert_image
from audio import convert_audio
from video import convert_video
from documents import convert_doc
from archive import convert_archive

def main():
    while True:
        print("\nFile Conversion Menu:") 
        
        print("1. Image Conversion")
        print("2. Audio Conversion")
        print("3. Video Conversion")
        print("4. Document Conversion")
        print("5. Archive Conversion")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            convert_image()

        elif choice == "2":
            convert_audio()

        elif choice == "3":
            convert_video()

        elif choice == "4":
            convert_doc()

        elif choice == "5":
            convert_archive()
        
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")