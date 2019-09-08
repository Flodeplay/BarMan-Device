import tkinter as tk
from tkinter import ttk

class InfoPanel(ttk.Frame):
    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content()

    def init_content(self):
        s = ttk.Style()
        s.configure('register.right.TLabel', font="Helvetica 10",foreground="white", padding=5, background="#201F1E")
        ttk.Label(self, text="Website: barman.at", style="register.right.TLabel").pack(side="top")
        ttk.Label(self, text="Key: ", style="register.right.TLabel").pack(side="top")
        ttk.Label(self, text="PWD: ", style="register.right.TLabel").pack(side="top")



