import requests

respon = requests.get("https://www.goodreads.com/author/quotes/947.William_Shakespeare")
print(respon.status_code)
print(len(respon.text)) # length of the pdf file
print(respon.text[:500]) # prints first 500 characters
print(respon.raise_for_status()) # raises exception if download fails