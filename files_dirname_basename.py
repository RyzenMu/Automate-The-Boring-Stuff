import os
path = "c:\\folder1\\folder2\\spam.png"
directory_name = os.path.dirname(path)
base_name = os.path.basename(path)
print(directory_name)
print(base_name)