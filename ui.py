from tkinter import *

class UI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('AeroStats')
        self.parent.geometry('500x300')


def start_ui():
    root = Tk()
    UI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

start_ui()