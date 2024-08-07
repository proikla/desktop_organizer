# from tkinter import *
from tkinter import Tk, N, W
import tkinter as tk
from tkinter import ttk
import organize

USEGUI = 'useGUI'
CLONE = 'cloneExecutable'

settings = organize.settings


def launch_gui():
    window = Tk()

    # checkbox variables.
    use_gui_check = tk.BooleanVar(value=settings['useGUI'])
    clone_check = tk.BooleanVar(value=settings['cloneExecutable'])

    def on_button_press():
        from organize import organize
        organize()

    def on_check0():
        settings['useGUI'] = use_gui_check.get()
        organize.write_json_settings()

    def on_check1():
        settings['cloneExecutable'] = clone_check.get()
        organize.write_json_settings()

    # window size
    window_width = 400
    window_height = 250
    window.geometry(f"{window_width}x{window_height}")

    # other window settings
    window.title('organize GUI')
    window.grid_anchor(N)
    window.resizable(False, False)

    # centering the window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # label & button
    ttk.Label(window, text="Would you like to organize desktop?").grid(
        column=0, row=0, pady=(30, 0))

    organize_button = ttk.Button(
        window, text="organize", command=on_button_press, width=25)

    organize_button.grid(column=0, row=1, pady=(10, 0))

    # checkboxes
    checkboxes = ttk.Frame(window, padding=(0, 30, 0, 100))
    checkboxes.grid(sticky=W)

    checkbox0 = ttk.Checkbutton(
        checkboxes, text='use gui', command=on_check0, variable=use_gui_check)
    checkbox0.pack(anchor=W)
    checkbox1 = ttk.Checkbutton(
        checkboxes, text='clone executable', command=on_check1, variable=clone_check)
    checkbox1.pack(anchor=W)

    window.mainloop()


if __name__ == '__main__':
    launch_gui()
    # TODO: add info about each checkbox in the readme or in the program
