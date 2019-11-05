from tkinter import *
import tkinter.ttk as ttk


class Profile(ttk.Frame):
    def __init__(self, parent,profile, **options):
        super().__init__(parent, **options)
        self.profile = profile
        self.init_content()

    def init_content(self):

        canvas = Canvas(self)
        canvas.grid()
        canvas.create_oval(5, 25, 195, 215, fill='gray', outline="")
        canvas.create_text(100,130, text="MK", fill="lightgray", font=("Helvetica", 80), width=200)
