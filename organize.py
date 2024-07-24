import os
import shutil
from time import sleep

desktop_path = os.path.expanduser("~/Desktop")
organize_path = f'{desktop_path}/organize/'
desktop_contents = os.listdir(desktop_path)
IGNORED = ['.lnk','.url']

# 'organize' folder creation and organize.py file update.
if not os.path.exists(organize_path):
    # creating organize folder
    os.makedirs(organize_path)
    # making a copy of python file.
    shutil.copy('organize.py', organize_path)

# if 'organize' folder exists, but organize.py file doesnt.
elif not os.path.exists(f'{organize_path}/organize.py'):
    try:
        shutil.copy('organize.py', organize_path)
    except IOError as e:
        print('an error occured during organize.py file copying.')

organize = os.listdir(organize_path)

# get the file extension
def get_ext(filepath):
    return os.path.splitext(filepath)[1].lower() if not os.path.isdir(filepath) else None

# folder creation in 'organize' folder
def folder_creation():
    for i in desktop_contents:
        ext = get_ext(f'{desktop_path}/{i}')
        if ext and ext not in IGNORED:
            os.makedirs(f'{organize_path}/{ext}', exist_ok=True)
    # after 'organize' folder is ready return true.
    return True


# moving the files to its extension folder
def file_move():
    for file in desktop_contents:
        file_ext = get_ext(file)

        # if file is a file and its folder exist in the /organize/ - move it
        if file_ext and os.path.isdir(f'{organize_path}/{file_ext}'):
            try:
                shutil.move(f'{desktop_path}/{file}', f'{organize_path}/{file_ext}')
            except Exception as e:
                print(e)

def main():
    while not folder_creation():
        sleep(.1)
    file_move()
    print('Done.')
    os.system('pause')

if __name__ == '__main__':
    main()