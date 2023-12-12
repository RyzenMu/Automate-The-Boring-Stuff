import os

rel_path = os.path.relpath("c:\\folder1\\folder2\\spam.png", "c:\\folder1")
print(rel_path)