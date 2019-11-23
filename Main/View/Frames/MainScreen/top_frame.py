from tkinter import *
from tkinter import ttk


class TopFrame(ttk.Frame):
    def __init__(self, parent,username, **options):
        super().__init__(parent, **options)
        self.init_content(username)

    def init_content(self, username):
        ttk.Style().configure('mainscreen.topframe.TLabel', background="#87014F",font="Helvetica 18", foreground="white")
        label = ttk.Label(self, text="Barman", width=8,style="mainscreen.topframe.TLabel")
        label.pack(side="left")

        frame = ttk.Frame(self, style='mainscreen.topframe.TFrame')
        frame.pack(side="right")
        label = ttk.Label(frame, text=username, style="mainscreen.topframe.TLabel", padding=[10,0])
        label.pack(side="left")
        button = Button(frame, height=50, width=5, background="#87014F", text="×")
        button.pack(side="right")


