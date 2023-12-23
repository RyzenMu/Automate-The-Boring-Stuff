import docx

def getText(document):
    doc = docx.Document(document)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)    

print(getText("C:\\Users\\x\\Desktop\\demo.docx"))