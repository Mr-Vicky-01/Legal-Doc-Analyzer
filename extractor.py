from PyPDF2 import PdfReader

# PDF Handler Class
class PDFHandler:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def read_pdf(file):
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text