helloFile = open("D:\\AutomateTheBoringStuff\\files_helloFile.txt")
readLines = helloFile.readlines() # returns a array of strings
print(readLines)
helloFile.close()