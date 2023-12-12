import os

path = os.getcwd()
print(path)
for i in range(5):
    print(path, i)
    
# to change the current working directory use os.chdir('c:\\Documents\\..') 
# to get the absolute path use os.path.abspath()
abspath = os.path.abspath(path)
print(abspath)
# isabs() function gives the boolean value whether it is absolute path 
# to create a new folder use os.path.mkdirs(absolutepath)
   