import tkinter as tk
from tkinter import ttk
class DataLoading(tk.Frame):
    def __init__(self, master,name, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content(name)
        self['bg'] = self.master['bg']

    def init_content(self,name):
        l = tk.Label(self, text="Servus "+name+"!\nWir laden nur noch schnell deine Profile")
        l['bg'] = self.master['bg']
        l['fg'] = "white"
        l['font'] = "Arial 25"
        l['justify'] = "left"
        l.place(x=400, y=150, anchor="center")
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", troughcolor=self.master['bg'], background='#55A990',
                    lightcolor="#55A990", darkcolor="#55A990", bordercolor="white")
        progressbar = ttk.Progressbar(self, style="red.Horizontal.TProgressbar", orient="horizontal",length=600, mode="determinate")
        progressbar["value"] = 50
        progressbar.place(x=400, y=300,anchor="center")
