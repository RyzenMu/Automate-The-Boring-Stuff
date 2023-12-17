import shelve
shelve_file = shelve.open('mydata')
print(list(shelve_file.keys()))
print(list(shelve_file.values()))
print(list(shelve_file.items()))
shelve_file.close()