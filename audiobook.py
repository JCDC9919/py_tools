import pyttsx3
import pdfplumber
import PyPDF2
global pageNums

file = "sample.pdf"

pdfFile = open(file, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

pages = pdfReader.numPages

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()