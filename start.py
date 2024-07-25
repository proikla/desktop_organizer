import subprocess
from utils.organize import settings

if __name__ == '__main__':
    if settings['cloneExecutable']:
        subprocess.Popen(["python", "utils/gui.pyw"])
    else:
        from utils.organize import organize
        organize()
        ...

        # TODO: delete executable in organize folder if needed
