import tkinter as tk
from tkinter import *
from tkinter import ttk, ttk as ttk


class CenterGrid(ttk.Frame):

    def __init__(self, parent,profiles, **options):
        super().__init__(parent, **options)
        self.profiles = profiles
        self.profilesframes = []
        self.init_content()


    def init_content(self):
        for i in range(len(self.profiles)):
            ttk.Style().configure('mainscreen.centerGrid.profile.TFrame', background="#871352")
            frame = Profile(self, self.profiles[i], width=150, height=200, style='mainscreen.centerGrid.profile.TFrame')
            frame.grid_propagate(0)
            frame.grid(column=i, row=0,pady=45, padx=20)
            Grid.columnconfigure(frame, 0, weight=1)
            Grid.rowconfigure(frame, 0, weight=1)
            Grid.columnconfigure(frame, 2, weight=1)
            Grid.rowconfigure(frame, 2, weight=1)
            self.profilesframes.append(frame)
            self.update()


class Profile(ttk.Frame):
    def __init__(self, parent,beverage, **options):
        super().__init__(parent, **options)
        self.beverage = beverage
        self.init_content(beverage)
        Grid.grid_columnconfigure(self, 0, weight=1)
        Grid.grid_columnconfigure(self,1, weight=1)
        Grid.grid_columnconfigure(self,2, weight=1)
        Grid.grid_rowconfigure(self,0, weight=1)
        Grid.grid_rowconfigure(self,2, weight=1)

    def init_content(self, beverage):
        ttk.Style().configure('mainscreen.centerGrid.profile.TLabel', background="#871352", font="Helvetica 15",
                              foreground="white",justify="center", anchor="center")
        ttk.Style().configure('mainscreen.centerGrid.profile.small.TLabel', background="#871352", font="Helvetica 12",
                              foreground="white", justify="center", anchor="center")
        label = ttk.Label(self, text=beverage.name, style="mainscreen.centerGrid.profile.TLabel", wraplength=180)
        label.grid(row=0, sticky="nsew", pady=(20, 10))
        ttk.Style().configure('mainscreen.centerGrid.profile.TSeparator', justify="center", anchor="center")
        ttk.Separator(self, style="mainscreen.centerGrid.profile.TSeparator").grid(column=0, row=1, sticky="nsew",padx=(10, 10), pady=(10, 20))
        label = ttk.Label(self, text=beverage.getingredients(), style="mainscreen.centerGrid.profile.small.TLabel", wraplength=145)
        label.grid(row=2,sticky="nsew",pady=(0,20), padx=(20, 20))
