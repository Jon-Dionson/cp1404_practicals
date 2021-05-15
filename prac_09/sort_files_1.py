"""Sort files based on file type"""
import os
import shutil

os.chdir("FilesToSort")

for filename in os.listdir('.'):
    file_type = filename.split(".")[-1]
    try:
        os.mkdir(file_type)
    except FileExistsError:
        pass
    print(f"{file_type}/{filename}")
    shutil.move(filename, file_type)


