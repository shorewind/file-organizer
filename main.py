import os
import shutil


def settings():
    print(f'\n--------SETTINGS---------\n'
        f'Source Path: {src}\n'
        f'Destination Path: {dest}\n'
        f'Subfolders: {subfolders}\n')


def options():
    print(f'--------OPTIONS----------\n'
        f'1. Set Source Path\n'
        f'2. Set Destination Path\n'
        f'3. Add Subfolder\n'
        f'4. MOVE FILES\n'
        f'5. Exit\n')
        

run_flag = True

print("***FILE ORGANIZER TOOL***")

while run_flag:
    fr = open("user-info.txt", "r")
    lines = fr.readlines()
    print(len(lines))
    if len(lines) < 3:
        fw = open("user-info.txt", "w")
        fw.write('\n\n\n')
        fw.close()
    fr.seek(0)
    src = lines[0].strip()
    dest = lines[1].strip()
    subfolders = lines[2].strip()

    settings()
    options()

    selection = input("Enter your selection: ")
    
    fw = open("user-info.txt", "w")

    if selection == '1':
        src = input("Enter your source path: ")
        lines[0] = f'{src}\n'
    elif selection == '2':
        dest = input("Enter your root destination path: ")
        lines[1] = f'{dest}\n'
    elif selection == '3':
        sf_list = subfolders.split(', ')
        sf_list = [x for x in sf_list if x]
        name = input("Enter a subfolder name: ")
        if len(sf_list) > 0:
            subfolders = subfolders + ", " + name
            lines[2] = subfolders
        else:
            subfolders = name
            lines[2] = name
        sf_list.append(name)
    elif selection == '4':
        try:
            files = os.listdir(src)

            moved_files = ''

            for file in files:
                for subfolder in sf_list:
                    if subfolder.lower() in file.lower().replace(" ", ""):
                        moved_files = f'{moved_files}\n{file}\n'
                        file_path = os.path.join(src, file)
                        dest_path = os.path.join(dest, subfolder.upper())

                        if os.path.exists(dest_path) == False:
                            os.makedirs(dest_path)

                        shutil.move(file_path, dest_path)
            print(f'_______MOVED FILES_______'
                f'{moved_files}\n')
        except:
            print("Failed to move files. Please check your settings.")
    else:
        break

    fw.writelines(lines)
    fw.close()
    fr.close()

    response = input("Would you like to make another selection? (y/n) ")

    if response.lower() != "y":
        run_flag = False
        settings()
