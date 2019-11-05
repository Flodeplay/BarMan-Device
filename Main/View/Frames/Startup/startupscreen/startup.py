from tkinter import ttk
import tkinter as tk

class StartupScreen(ttk.Frame):
    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content()

    def init_content(self):
        ttk.Style().configure('startup.TLabel',font="Helvetica 80", foreground="white", background=ttk.Style().lookup("startup.TFrame","background"), height=400, width=800, justify="center", anchor="center")
        text = ttk.Label(self, text="BarMan", style="startup.TLabel")
        text.pack_propagate(0)
        text.pack()

