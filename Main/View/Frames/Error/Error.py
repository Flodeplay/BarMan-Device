import tkinter
from tkinter import ttk
from enum import Enum

class Mix_Exception(Exception):
    def __init__(self, message):
        self.message = message
        pass

    def show_error(self, window):
        screen = ErrorScreen(window, self)
        screen.tkraise()


class ErrorScreen(ttk.Frame):
    def __init__(self, parent, exception, **options):
        super().__init__(parent, **options)
        self.exception = exception
        self.init_content()
    def init_content(self):
        ttk.Style().configure('error.big.TLabel', background="#871352", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.small.TLabel', background="#871352", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.TLabel', background="#201F1E", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('error.top.TFrame', background="#871352")
        topframe = ttk.Frame(self, height=200, width=800, style="error.top.TFrame")

        ttk.Label(topframe, text="Fehler!", style="error.big.TLabel").place(x=400, y=70,
                                                                                                     anchor="center")
        ttk.Label(topframe, text=self.exception.message, style="error.small.TLabel").place(x=400, y=150, anchor="center")
        topframe.grid_propagate(0)
        topframe.grid(row=0)

class ErrorType(Enum):
        SHOW = 1
        HIDE = 2
        RETURN_MAINSCREEN = 3
        RETURN_SHUTDOWN = 4
        RETURN_NETWORK_SELECTION = 5


