import subprocess
from utils.organize import settings

# settings = utils.organize.settings

if __name__ == '__main__':
    if settings['cloneExecutable']:
        subprocess.Popen(["python", "utils/gui.pyw"])
    else:
        print('wtf')
        from utils.organize import organize
        organize()
        ...

        # TODO: delete executable in organize folder if needed
