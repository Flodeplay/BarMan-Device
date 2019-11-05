from tkinter import *
from tkinter import ttk


class TopFrame(ttk.Frame):
    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        self.init_content()

    def init_content(self):
        ttk.Style().configure('mainscreen.topframe.TLabel', background="#87014F",font="Helvetica 20", foreground="white")
        label = ttk.Label(self, text="Barman", width=8,style="mainscreen.topframe.TLabel")
        label.pack(side="left")
        button = Button(self, height=50, width=5, background="#87014F", text="×")
        button.pack(side="right")


