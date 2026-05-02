import fitz
import pytesseract
from PIL import Image

# Windows users (edit path if needed)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_from_image(file):
    img = Image.open(file)
    return pytesseract.image_to_string(img)

def extract_text(file):
    if file.type == "application/pdf":
        return extract_from_pdf(file)
    else:
        return extract_from_image(file)