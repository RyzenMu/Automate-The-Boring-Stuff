import PyPDF2
import os

os.chdir("C:\\Users\\x\\Desktop")
pdfFile = open('BigBookSmallPythonProjects.pdf', 'rb')

reader = PyPDF2.PdfReader(pdfFile)
print(len(reader.pages))

# reader = PyPDF2.PdfFileReader(pdfFile)
# print(len(reader.numPages())) # prints number of pages

page_10 = reader.pages[10]
print(page_10.extract_text())
