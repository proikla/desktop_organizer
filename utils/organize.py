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
IGNORED = ['.lnk', '.url']  # TODO: add IGNORED to json


# create /organize/ if doesnt it exist, clone organize.py into it if needed. #todo create link to start.py in the organize folder
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
            except Exception:
                pass
                # todo logging
        else:
            ...

    create_ext_folders_and_move()


# get extension of the file
def get_ext(filepath):
    return os.path.splitext(filepath)[1].lower() if not os.path.isdir(filepath) else None


# folder creation in 'organize' folder
def create_ext_folders_and_move():

    desktop_contents = os.listdir(desktop_path)
    
    for file in desktop_contents:
        file_ext = get_ext(file)

        if file_ext and file_ext not in IGNORED:
            os.makedirs(f'{organize_path}{file_ext}', exist_ok=True)

        # if file is a file and its folder exist in the /organize/ - move it
        if file_ext and os.path.isdir(f'{organize_path}{file_ext}'):
            try:
                shutil.move(f'{desktop_path}/{file}',
                            f'{organize_path}{file_ext}')
            except Exception:
                # todo add logging functionality and logging check in the gui
                pass

# all functionality combined
def organize():
    setup_organize_folder()


def main():
    organize()


if __name__ == '__main__':
    main()
