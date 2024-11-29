import fitz  # PyMuPDF module used

def merge(directories, save_path):
    print("Running merge() function")
    doc = fitz.open()

    for file in directories:
        if file.endswith(".pdf"):
            pdf_document = fitz.open(file) # open current file and store it in pdf_document
            doc.insert_pdf(pdf_document) # insert the pdf_document into the doc
            print(f"Merging {file}")
        else:
            print("{file} is not a PDF file")

    try:
        doc.save(save_path)
        print("Successful merging of files")
        doc.close()
    except Exception as e:
        print("Error occurred in saving merged file")
        doc.close()