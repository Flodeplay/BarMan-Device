import tkinter as tk


class Topframe(tk.Frame):
    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content()

    def init_content(self):
        label = tk.Label(self, text="Barman", width=8, font="Helvetica 20", fg="white")
        label['bg'] = self['bg']
        label.pack(side="left")
        button = tk.Button(self, height=50, width=5, background="white", text="×")
        button.pack(side="right")


