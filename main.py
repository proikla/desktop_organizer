import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")
contents = os.listdir(desktop_path)

# 'organize' folder creation
if not os.path.exists(f'{desktop_path}/organize'):
    os.makedirs(f'{desktop_path}/organize')
else:
    shutil.copy('main.py', f'{desktop_path}/organize')


organize = os.listdir(f'{desktop_path}/organize')

# file extension
def split(filepath):
    return os.path.splitext(filepath)[1].lower()


# folder creation in 'organize' folder
def folder_creation():
    for i in range(len(contents)):
        if split(f'{desktop_path}/{contents[i]}') != '' and not os.path.exists(
                desktop_path + '/organize/' + split(f'{desktop_path}/{contents[i]}')) and not split(f'{desktop_path}/{contents[i]}') == '.lnk' and not split(f'{desktop_path}/{contents[i]}') == '.url':
            os.makedirs(desktop_path + '/organize/' + split(f'{desktop_path}/{contents[i]}'))


# moving the files in its extension folder
def file_move():
    for j in organize:
        if j != '' and os.path.isdir(f'{desktop_path}/organize/{j}'):
            for i in contents:
                try:
                    if split(i) == j and i != '':
                        shutil.move(f'{desktop_path}/{i}', f'{desktop_path}/organize/{j}')
                except IOError as e:
                    print(e)
                    
def main():
    folder_creation()
    file_move()
    print('Done.')
    os.system('pause')

if __name__ == '__main__':
    main()
