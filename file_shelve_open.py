import shelve

shelve_file = shelve.open('mydata')
data = shelve_file['cats']
print(data)