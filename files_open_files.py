helloFile = open("D:\\AutomateTheBoringStuff\\files_helloFile.txt")
text = helloFile.read() # returns the string in the helloFile.txt
print(text)
helloFile.close() # once the job is finished it should be closed to reduce the ram usage
