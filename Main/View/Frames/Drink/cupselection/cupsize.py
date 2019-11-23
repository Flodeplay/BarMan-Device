import tkinter as tk
from tkinter import *
from tkinter import ttk
from Main.View.Frames.MainScreen.Profiles.profile import Profile


# TODO implement error feedback
class Cupseletion(ttk.Frame):

    def __init__(self, parent, beverage, **options):
        super().__init__(parent, **options)
        self.init_content(beverage)

    def init_content(self, beverage):
        ttk.Style().configure('cupseletion.top.TLabel', background="#871352", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('cupseletion.big.TLabel', background="#201F1E", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('cupseletion.small', background="#201F1E", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('cupseletion.top.TFrame', background="#871352")
        topframe = ttk.Frame(self, height=120, width=800, style="cupseletion.top.TFrame")
        ttk.Label(topframe, text="Bitte Wähle eine Größe aus", style="cupseletion.top.TLabel").place(x=400, y=60, anchor="center")
        topframe.grid_propagate(0)
        topframe.grid(row=0)

        #TODO implemnt the selcetions

