from tkinter import *
from tkinter import ttk
from enum import Enum

class Mix_Exception(Exception):
    def __init__(self, message):
        super(Mix_Exception, self).__init__()
        self.message = message


class ErrorScreen(ttk.Frame):
    def __init__(self, parent, exception, callback, arg, **options):
        super().__init__(parent, **options)
        self.exception = exception
        self.callback = callback
        self.init_content()
        self.grid(row=0)

    def init_content(self):
        ttk.Style().configure('error.big.TLabel', background="#871352", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.small.TLabel', background="#871352", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.TLabel', background="#201F1E", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.top.TFrame', background="#871352")
        topframe = ttk.Frame(self, height=200, width=800, style="error.top.TFrame")

        ttk.Label(topframe, text="Fehler!", style="error.big.TLabel").pack(side=TOP,expand=YES, fill=BOTH)
        ttk.Label(topframe, text=self.exception.message, style="error.small.TLabel").pack(side=BOTTOM,expand=YES,fill=BOTH)
        topframe.pack(side=TOP,expand=YES,fill=BOTH)

