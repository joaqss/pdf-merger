import PyPDF2 # a module for PDF merge
import sys # a module for runtime environment
import os # a module to interact with the operating system (CRUD, paths, etc.)

filepath_input = input("Where are your files located? Please paste the filepath here: ") # Filepath will be determined
print("Thank you.")
output_path = input("Where do you want to save the merged PDF files?") # Filepath on where it will be saved
filename = input("What filename do you want? No spaces and add .pdf at the end of the name. ") #filename will be determined here

folder = filepath_input #filepath input will be converted into a 'folder' string
merger = PyPDF2.PdfMerger() 

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        file_path = os.path.join(folder, file)
        merger.append(file_path)
    else:
        print("No PDF file/s available")
try: 
    merger.write(output_path + "/" + filename)
    print("good!")
    merger.close()
except:
    print("Error occured")


