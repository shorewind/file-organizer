import os
import shutil

DEST = ''  # root destination path

SRC = ''  # source path

files = os.listdir(SRC)

subfolders = []  # list of keywords/folder names

for file in files:
    for subfolder in subfolders:
        if subfolder.lower() in file.lower().replace(" ", ""):
            print(file)
            file_path = os.path.join(SRC, file)
            dest_path = os.path.join(DEST, subfolder.upper())

            if os.path.exists(dest_path) == False:
                os.makedirs(dest_path)

            shutil.move(file_path, dest_path)
            