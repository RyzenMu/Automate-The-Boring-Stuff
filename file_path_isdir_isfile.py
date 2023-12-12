import os
path = "c:\\windows\\system32\\calc.exe"
print(os.path.isfile(path))
path = "c:\\windows\\system32"
print(os.path.isdir(path))