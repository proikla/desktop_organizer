import os
from os import path
import shutil

desktop_path = os.path.expanduser("~/Desktop")
contents = os.listdir(desktop_path)

# 'organize' folder creation
if not path.exists(f'{desktop_path}/organize'):
    os.makedirs(f'{desktop_path}/organize')
organize = os.listdir(f'{desktop_path}/organize')


# file extension
def split(filepath):
    return os.path.splitext(filepath)[1].lower()


# folder creation in 'organize' folder
def folder_creation():
    for i in range(len(contents)):
        if path.splitext(f'{desktop_path}/{contents[i]}')[1] != '' and not path.exists(
                desktop_path + '/organize/' + split(f'{desktop_path}/{contents[i]}')) and not split(f'{desktop_path}/{contents[i]}') == '.lnk' and not split(f'{desktop_path}/{contents[i]}') == '.url':
            os.makedirs(desktop_path + '/organize/' + split(f'{desktop_path}/{contents[i]}'))


# moving the files in its extension folder
def file_move():
    for j in organize:
        if j != '' and path.isdir(f'{desktop_path}/organize/{j}'):
            for i in contents:
                if split(i) == j and i != '':
                    shutil.move(f'{desktop_path}/{i}', f'{desktop_path}/organize/{j}')


if __name__ == '__main__':
    folder_creation()
    file_move()
