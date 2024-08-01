#PDF Merger
from PyPDF2 import PdfMerger

def merge_pdfs():
    print("Welcome to the PDF Merger Script!")
    pdf_files = input("Enter the PDF file names to merge (comma separated): ").split(",")

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf.strip())
    
    output_file = input("Enter the name of the output PDF file: ")
    merger.write(output_file)
    merger.close()
    print(f"Merged PDF saved as {output_file}")

if __name__ == "__main__":
    merge_pdfs()
