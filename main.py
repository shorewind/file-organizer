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
        f'3. Subfolder Options\n'
        f'4. Move Files\n'
        f'5. Exit\n')
        

print("***FILE ORGANIZER TOOL***")

run_flag = True
while run_flag:
    fr = open("user-info.txt", "r")  # read user info from text file
    lines = fr.readlines()
    if len(lines) < 2:  # if less than two lines, write three blank lines
        fw = open("user-info.txt", "w")
        fw.write('\n\n\n')
        fw.close()
    fr.seek(0)  # back to beginning of file
    lines = fr.readlines()
    src = lines[0].strip()  # assign source path to line 1
    dest = lines[1].strip()  # assign destination path to line 2
    subfolders = lines[2].strip()  # assign subfolders to line 3
    sf_list = subfolders.split(', ')  # create list from comma-separated variables
    fr.close()  # close file

    settings()
    options()

    selection = input("Enter your number selection: ")
    
    fw = open("user-info.txt", "w")  # write to user info text file

    if selection == '1':
        src = input("Enter your source path: ")
        lines[0] = f'{src}\n'
    elif selection == '2':
        dest = input("Enter your root destination path: ")
        lines[1] = f'{dest}\n'
    elif selection == '3':
        sf_flag = True
        while sf_flag:
            print(f'\n----SUBFOLDER OPTIONS----\n'
                f'1. Add Subfolder\n'
                f'2. Remove Subfolder\n'
                f'3. Clear Subfolders\n'
                f'4. Back\n')
            sf_selection = input("Enter a subfolder option number: ")

            if sf_selection == '1':
                name = input("Enter a subfolder name: ")
                if len(sf_list) > 0:  # if at least one subfolder already exists, add to line
                    subfolders += ", " + name.upper()
                    lines[2] = subfolders
                else:  # otherwise add first subfolder
                    subfolders = name.upper()
                    lines[2] = name.upper()
                sf_list.append(name.upper())  # append subfolder to list
                print(f'Added "{name.upper()}" folder to settings.')
            elif sf_selection == '2':
                name = input("Enter a subfolder name: ")
                if name.upper() in sf_list:  # if subfolder exists in user info
                    sf_list.remove(name.upper())
                    if len(sf_list) >= 1:
                        subfolders = sf_list[0]  # rewrite subfolders
                        for i in range(1, len(sf_list)):
                            subfolders += ", " + sf_list[i]
                    else:
                        subfolders = ''
                    lines[2] = subfolders
                    print(f'Removed "{name.upper()}" folder from settings.')
                else:
                    print(f'Failed to remove "{name.upper()}" folder.')
                    break
            elif sf_selection == '3':
                subfolders = ''  # set subfolders line to blank
                lines[2] = subfolders
                print("Cleared subfolders.")
            else:
                break   

            settings()
            sf_run = input("Would you like to continue managing subfolders? (y/n) ")
        
            if sf_run.lower() != 'y':  # stop looping subfolder options when 'y' is not the response
                sf_flag = False

    elif selection == '4':
        try:
            files = os.listdir(src)  # get all files in source directory
            moved_files = ''  # initialize string of moved files

            for file in files:
                for subfolder in sf_list:
                    short_file = file.lower().replace(" ", "").replace("-", "").replace("_", "")  # shortform name of each file
                    if subfolder.lower() in short_file:  # if subfolder name in file name
                        src_file_path = os.path.join(src, file)
                        dest_path = os.path.join(dest, subfolder.upper())
                        dest_file_path = os.path.join(dest_path, file)

                        if os.path.exists(dest_path) == False:  # if the subfolder doesn't exist yet
                            os.makedirs(dest_path)  # make the subfolder directory

                        if os.path.exists(dest_file_path):  # if the file already exists in the destination
                            os.remove(src_file_path)
                            print(f'\n{file} already exists in destination. Deleted copy in source.\n')
                        else:
                            moved_files = f'{moved_files}\n{file}'
                            shutil.move(src_file_path, dest_path)  # move file
            if moved_files != '':
                print(f'\n_______MOVED FILES_______'
                f'{moved_files}\n')  # output results
            else:
                print("\nNo files to move.\n")
        except Exception as e:
            print(f'\n{e}')
            print("\nFailed to move files. Please check your settings.\n")
    else:
        break

    fw.writelines(lines)  # rewrite new lines to file
    fw.close()  # close file

    response = input("Would you like to make another selection? (y/n) ")

    if response.lower() != "y":  # stop main loop and display settings
        run_flag = False
        settings()
