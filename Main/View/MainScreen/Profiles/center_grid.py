import tkinter as tk
from Main.View.MainScreen.Profiles.profile import Profile


class CenterGrid(tk.Frame):

    def __init__(self, master, profiles, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.profiles = profiles
        self.init_content()

    def init_content(self):
        for i in range(len(self.profiles)):
            frame = Profile(self, width=(600/len(self.profiles)), height=260)
            frame.init_content(self.profiles[i])
            frame.pack_propagate(0)
            frame.grid(column=i, row=1, padx=20, pady=20)

