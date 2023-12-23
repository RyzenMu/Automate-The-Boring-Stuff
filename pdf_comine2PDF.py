import PyPDF2
pdf1_file = open("C:\\Users\\x\\Desktop\\AutomateTheBoringStuff.pdf", 'rb')
pdf2_file = open("C:\\Users\\x\\Desktop\\BigBookSmallPythonProjects.pdf", 'rb')

reader1 = PyPDF2.PdfReader(pdf1_file)
reader2 = PyPDF2.PdfReader(pdf2_file)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)
    
for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)
    
output_file = open('C:\\Users\\x\\Desktop\\CombinedPdf.pdf', 'wb')
writer.write(output_file)

output_file.close()
pdf1_file.close()
pdf2_file.close()