import os
import shutil

print("_____FILE ORGANIZER TOOL_____")

run_flag = True

while run_flag:
    SRC = input("Enter your source path: ")  # source path C:\Users\user\Downloads

    DEST = input("Enter your root destination path: ")  # root destination path C:\Users\user\Documents

    files = os.listdir(SRC)

    subfolders = input("Enter a list of destination subfolders: ")  # ["wpm", "ee213", "ma238", "mu100"]  list of keywords/folder names

    for file in files:
        for subfolder in subfolders:
            if subfolder.lower() in file.lower().replace(" ", ""):
                print(file)
                file_path = os.path.join(SRC, file)
                dest_path = os.path.join(DEST, subfolder.upper())

                if os.path.exists(dest_path) == False:
                    os.makedirs(dest_path)

                shutil.move(file_path, dest_path)

    response = input("Would you like to make another selection? (y/n) ")

    if response.lower() != "y":
        run_flag = False
