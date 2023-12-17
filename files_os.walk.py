import os
path = "D:\\AutomateTheBoringStuff"
for folderName, subFolders, fileNames in os.walk(path):
    print("The Folder is " + folderName)
    print("The sub flder in " +folderName + "are" + str(subFolders ))
    print("The file name in" +folderName+ "are" +str(fileNames))
    print()