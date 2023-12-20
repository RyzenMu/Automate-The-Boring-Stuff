import requests

res = requests.get("https://nosweatshakespeare.com/wp-content/uploads/2020/09/The-Merchant-of-Venice-PDF.pdf")

pdf_file = open("MerchantofVenice.pdf", "wb")

for chunk in res.iter_content(100000):
    pdf_file.write(chunk)
    
pdf_file.close()    