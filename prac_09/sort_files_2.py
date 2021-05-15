"""Sort files based user's choice"""
import os
import shutil

os.chdir("FilesToSort")
file_directory = {}
for filename in os.listdir('.'):

    file_type = filename.split(".")[-1]
    if file_type not in file_directory:
        category = input(f"What category would you like to sort {file_type} files into? ")
        file_directory[file_type] = category
    try:
        os.mkdir(category)
    except FileExistsError:
        pass

    shutil.move(filename, category)
