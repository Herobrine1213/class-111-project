import os
import shutil
from_dir="C:/Users/Admin/Downloads"
to_dir="C:/Users/Admin/Documents/Document_files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    root,extension=os.path.splitext(file)
    print(root)
    print(extension)