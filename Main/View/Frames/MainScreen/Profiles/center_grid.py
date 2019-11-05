from tkinter import *
from tkinter import ttk
from Main.View.Frames.MainScreen.Profiles.profile import Profile


class CenterGrid(ttk.Frame):

    def __init__(self, parent,profiles, **options):
        super().__init__(parent, **options)
        self.profiles = profiles
        self.init_content()

    def init_content(self):
        for i in range(len(self.profiles)):
            ttk.Style().configure('mainscreen.centerGrid.profile.TFrame', background="#87014F")
            frame = Profile(self, self.profiles[i], width=(800/len(self.profiles)-20*len(self.profiles)), height=260,style='mainscreen.centerGrid.profile.TFrame')
            frame.grid_propagate(0)
            frame.grid(column=i, row=1,padx=20)

