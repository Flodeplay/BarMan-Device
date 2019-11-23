import tkinter as tk
from tkinter import *
from tkinter import ttk
from Main.View.Frames.MainScreen.Profiles.profile import Profile


class CenterGrid(ttk.Frame):

    def __init__(self, parent,profiles, **options):
        super().__init__(parent, **options)
        self.profiles = profiles
        self.profilesframes = []
        self.init_content()


    def init_content(self):
        for i in range(len(self.profiles)):
            ttk.Style().configure('mainscreen.centerGrid.profile.TFrame', background="#871352")
            frame = Profile(self, self.profiles[i], width=160, height=200, style='mainscreen.centerGrid.profile.TFrame')
            frame.grid_propagate(0)
            frame.grid(column=i, row=0,pady=45, padx=20)
            self.profilesframes.append(frame)



