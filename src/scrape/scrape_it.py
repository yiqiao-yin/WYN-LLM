from typing import List
from PyPDF2 import PdfReader


def extract_pdf_text(filepath: str) -> List[str]:
    """
    Extracts text from each page of a PDF file using PyPDF2 and returns it as a list of strings.

    Parameters:
    filepath (str): The file path or URL of the PDF file to extract text from.

    Returns:
    List[str]: A list of strings containing the extracted text from each page of the PDF.
    """
    pdf_file = open(filepath, 'rb')
    status = True
    try:
        pdf_reader = PdfReader(pdf_file)
        pages = len(pdf_reader.pages)

        text_list = []
        for page in range(pages):
            pdf_page = pdf_reader.pages[page]
            text = pdf_page.extract_text()
            text_list.append(text)
    except Exception as e:
        status = False

    if status == False:
        try:
            text_list = []
            for i in PdfReader(open(name, 'rb')).pages:
                text_list.append(i.extract_text())
        except Exception as e:
            text_list = "Failed."
    else:
        print(f"Task status: {text_list}")

    pdf_file.close()
    return text_list