from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

im =Image.open("C:\\Users\\Furkan\\Desktop\\OpenCVegitim\\20.klasor\\text.png")

text = pytesseract.image_to_string(im,lang="eng")
print(text)
