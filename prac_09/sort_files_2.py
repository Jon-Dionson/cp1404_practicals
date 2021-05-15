"""Sort files based user's choice"""
import os
import shutil

os.chdir("FilesToSort")
file_directory = {}
for filename in os.listdir('.'):

    file_type = filename.split(".")[-1]
    print(file_type)
    try:
        os.mkdir(file_type)
    except FileExistsError:
        pass
