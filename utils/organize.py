import os
import shutil
import json


def setup_settings():
    if not os.path.exists('settings.json'):
        default_settings = {'useGUI': True, 'cloneExecutable': True}
        with open('settings.json', 'w') as w:
            w.write(json.dumps(default_settings))
        return default_settings
    else:
        return get_settings()


def get_settings():
    with open('settings.json', 'r') as r:
        data = json.loads(r.read())
    return data


settings = setup_settings()


def write_json_settings():
    with open('settings.json', 'w') as w:
        w.write(json.dumps(settings))
        w.close
    return 1


desktop_path = os.path.expanduser("~/Desktop")
organize_path = f'{desktop_path}/organize/'
desktop_contents = os.listdir(desktop_path)
IGNORED = ['.lnk', '.url']  # TODO: add IGNORED to json


# create /organize/ if doesnt it exist, clone organize.py into it if needed. #FIXME: change organize.py to start.py!
def setup_organize_folder():
    # 'organize' folder creation and organize.py file update.
    if not os.path.exists(organize_path):
        # creating organize folder
        os.makedirs(organize_path)

    # if 'organize' folder exists, but organize.py file doesnt.
    if not os.path.exists(f'{organize_path}organize.py'):
        if settings['cloneExecutable']:
            try:
                shutil.copy('utils/organize.py', organize_path)
            except Exception as e:
                print(f'an error occured during organize.py file copying: {e}')
        else:
            ...

    create_ext_folders()


# get extension of the file
def get_ext(filepath):
    return os.path.splitext(filepath)[1].lower() if not os.path.isdir(filepath) else None


# folder creation in 'organize' folder
def create_ext_folders():
    for i in desktop_contents:
        ext = get_ext(f'{desktop_path}/{i}')
        if ext and ext not in IGNORED:
            os.makedirs(f'{organize_path}{ext}', exist_ok=True)
    return True


# moving the files to its extension folder
def move_files_by_ext():
    for file in desktop_contents:
        file_ext = get_ext(file)

        # if file is a file and its folder exist in the /organize/ - move it
        if file_ext and os.path.isdir(f'{organize_path}{file_ext}'):
            try:
                shutil.move(f'{desktop_path}/{file}',
                            f'{organize_path}{file_ext}')
            except Exception:
                return False
        return True


# all functionality combined
def organize():
    setup_organize_folder()
    move_files_by_ext()
    return True


def main():
    organize()


if __name__ == '__main__':
    main()
