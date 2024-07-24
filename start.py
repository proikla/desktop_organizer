from utils.gui import settings, USEGUI
import subprocess

if __name__ == '__main__':
    if settings[USEGUI]:
        subprocess.Popen(["python", "utils/gui.py"])
    else:
        from utils.organize import organize
        organize()
        ...


# TODO: delete executable in organize folder if needed
