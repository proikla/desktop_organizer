import utils.gui as gui
from utils.organize import organize

if __name__ == '__main__':
    if gui.settings[gui.USEGUI]:
        gui.launch_gui()
    else:
        organize()
        ...


# TODO: delete executable in organize folder if needed
