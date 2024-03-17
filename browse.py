from tkinter import filedialog, Tk

def browse_for_file(file_type):
    print("Please select the input file to convert")
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[(f"{file_type.upper()} files", f"*.{file_type}")])
    root.destroy()
    return file_path

def browse_for_folder():
    print("Please select the folder to save the converted output file")
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    root.destroy()
    return folder_path