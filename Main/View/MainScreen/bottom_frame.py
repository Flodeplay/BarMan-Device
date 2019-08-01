import tkinter as tk
import fontawesome as fa


class BottomFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content()

    def init_content(self):
        label = tk.Label(self, text="Status", width=8, font="Helvetica 12", fg="white")
        label['bg'] = self['bg']
        label.pack(side="left")
