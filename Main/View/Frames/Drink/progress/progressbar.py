import tkinter as tk
from tkinter import *
from tkinter import ttk
from Main.View.Frames.MainScreen.Profiles.profile import Profile


class ProgressBar(ttk.Frame):

    def __init__(self, parent, beverage, **options):
        super().__init__(parent, **options)
        self.init_content(beverage)

    def init_content(self, beverage):
        ttk.Style().configure('progressbar.big.TLabel', background="#201F1E", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('progressbar.small.TLabel', background="#201F1E", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('progressbar.TLabel', background="#201F1E", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Label(self, text="Dein Getränk wird gerade gemixt", style="progressbar.big.TLabel").place(x=400,y=70,anchor="center")
        ttk.Label(self, text="gleich ist es soweit :)", style="progressbar.small.TLabel").place(x=400,y=150,anchor="center")
        ttk.Label(self, text="Dein Getränk: "+beverage.name, style="progressbar.small.TLabel").place(x=400,y=350,anchor="center")
        TROUGH_COLOR = '#201F1E'
        BAR_COLOR = '#871352'
        ttk.Style().configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR, bordercolor=TROUGH_COLOR,
                        background=BAR_COLOR, lightcolor=BAR_COLOR, darkcolor=BAR_COLOR)
        self.progressbar = ttk.Progressbar(self, style="bar.Horizontal.TProgressbar", orient="horizontal",length=600, mode="determinate")
        self.progressbar.place(x=400,y=250,anchor="center")

    def setprogress(self,value):
        self.progressbar["value"] = int(value)
