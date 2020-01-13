from tkinter import *
from tkinter import ttk
from enum import Enum
from PIL import ImageTk, Image

class Mix_Exception(BaseException):
    def __init__(self, message):
        super(Mix_Exception, self).__init__()
        self.message = message


class ErrorScreen(ttk.Frame):
    def __init__(self, parent, exception, callback, arg, **options):
        super().__init__(parent, **options)
        self.exception = exception
        self.init_content(callback,arg)
        self.grid(row=0, column=0, sticky="nsew")
        Grid.columnconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        self.tkraise()

    def init_content(self, callback, arg):
        ttk.Style().configure('error.big.TLabel', background="#201F1E", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.small.TLabel', background="#201F1E", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.TLabel', background="#201F1E", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.top.TFrame', background="#871352")
        topframe = TopFrame(self, callback=callback,arg=arg,padding=[20,10,0,10], style="error.top.TFrame")
        bottomframe = BottomFrame(self,self.exception)
        topframe.grid(row=0,sticky="nsew")
        bottomframe.grid(row=1,sticky="nsew")

class TopFrame(ttk.Frame):
    def __init__(self, parent, callback, arg, **options):
        super().__init__(parent, **options)
        ttk.Style().configure('pumps.topframe.TLabel', background="#87014F", font="Helvetica 18", foreground="white")
        logo = Image.open("images/chevron-left-solid.png")
        logo = logo.resize((17, 25), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        button = Label(self, background="#87014F", image=logo)
        button.bind("<Button-1>",
                   lambda event, arg=arg:
                   callback(arg))
        button.photo = logo
        button.pack(side="left")

class BottomFrame(ttk.Frame):
    def __init__(self, parent, exception, **options):
        super().__init__(parent, **options)
        ttk.Label(self, text="Fehler!", style="error.big.TLabel").pack(side=TOP, expand=YES, fill=BOTH)
        ttk.Label(self, text=exception.message, style="error.small.TLabel").pack(side=BOTTOM, expand=YES, fill=BOTH)


