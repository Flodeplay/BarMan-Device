from tkinter import *
from tkinter import ttk


class BottomFrame(ttk.Frame):
    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        self.init_content()

    def init_content(self):
        ttk.Style().configure('mainscreen.bottomFrame.TLabel',
                              background=ttk.Style().lookup("mainscreen.bottomFrame.TFrame", "background"),
                              font="Helvetica 15", foreground="white")

        #label = ttk.Label(self, text="Status", style="mainscreen.bottomFrame.TLabel")
        #label.pack(side="left")
