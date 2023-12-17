# shelves is used to store nbinary version of dictionries, variables, alists
import shelve

shelve_file = shelve.open('mydata')
shelve_file['cats'] = ['zophie', 'pooka', 'flattail', 'simon', 'cleo']
shelve_file.close()


