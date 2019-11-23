import tkinter as tk

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.resizable(0, 0)
        self['bg'] = "#201F1E"
        self.frames = {}
