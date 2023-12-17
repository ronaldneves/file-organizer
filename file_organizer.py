## modules
import os
import shutil


## globals
compact_formats = ['.zip', '.rar', '.7z']
media_formats = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mkv', '.jfif']
document_formats = ['.doc', '.docx', '.pdf', '.ppt', '.csv', '.log']
installers_formats = ['.exe', '.msi', '.iso']
new_folders_path = ['Instaladores', 'Arquivos de Mídia', 'Documentos', 'Zips e Rars', 'Etc']


## functions
## check if folders exists
def check_folders(path, new_path):
    for folder in new_path:
        if not os.path.exists(path + folder):
            try:
                os.makedirs(path + folder)
                print(f"Folder {folder} created.")
            except OSError as erro:
                print(f"Error trying to create {erro}")

        else:
            print(f"Folder {folder} already exists.")


## sort and move files and folders of the directory to the correct folder
def move_files(path, new_path):
    files_list = os.listdir(path)

    for file in files_list:
        if file.endswith(tuple(document_formats)):
            shutil.move(path + file, path + new_path[2])
            print(f"File {file} moved to new directory: {path + new_path[2]}")

        elif file.endswith(tuple(media_formats)):
            shutil.move(path + file, path + new_path[1])
            print(f"File {file} moved to new directory: {path + new_path[1]}")
        
        elif file.endswith(tuple(compact_formats)):
            shutil.move(path + file, path + new_path[3])
            print(f"File {file} moved to new directory: {path + new_path[3]}")
        
        elif file.endswith(tuple(installers_formats)):
            shutil.move(path + file, path + new_path[0])
            print(f"File {file} moved to new directory: {path + new_path[0]}")

        elif os.path.isdir(os.path.join(path, file)):
            if file not in new_path:
                shutil.move(path + file, path + new_path[4])
    
    print("......")
    print("The files on this directory are already on the correct folders. :)")


def main():
    print("File organizer. Separates files based on their extension and puts on the correspondent folder. ")
    windows_path = input("Insert the path of the folder you want to organize. ") + "/"

    check_folders(windows_path, new_folders_path)
    move_files(windows_path, new_folders_path)

    input("Press enter to leave.")


## main
if __name__ == "__main__":
    main()