import tkinter as tk
from tkinter import filedialog #tkinter module]
import os
import filesMerger

# main window
window = tk.Tk()
window.title("PDF Merger")
window.geometry("800x400")

# label
label = tk.Label(window, text="Add files to merge", font=('Arial', 14), fg="black")
label.pack(pady=10)

# label for chosen files
attached_files_label =tk.Label(window, text="Attached Files", font=('Arial', 14), fg="black")
label.pack(pady=10)

# list label for chosen files
attached_files_list =tk.Label(window, text="Attached Files", font=('Arial', 14), fg="black")
label.pack(pady=10)

file_paths = []
save_path = ""

# button event listener
def chooseFiles():
    global file_paths
    file_paths = filedialog.askopenfilenames(title="Choose files", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    if file_paths:
        file_names = [os.path.basename(path) for path in file_paths]
        print("Selected files:", file_names)
        attached_files_label.config(text="Attached Files: " + ", ".join(file_names))
        attached_files_label.pack()
        

def chooseSavePath():
    global save_path

    # ask filename and filepath
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if save_path:
        print("Selected save path:", save_path)

chooseFileButton = tk.Button(window, text="Choose Files", command=chooseFiles)
chooseFileButton.pack(pady=20)

chooseSaveLocButton = tk.Button(window, text="Choose Save Path", command=chooseSavePath)
chooseSaveLocButton.pack(pady=20)

mergeButton = tk.Button(window, text="Merge Files", command=lambda: filesMerger.merge(file_paths, save_path))
mergeButton.pack(pady=20)


# Run the application
window.mainloop()