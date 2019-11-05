from tkinter import *
from tkinter import ttk
from Main.View.Frames.MainScreen.top_frame import TopFrame
from Main.View.Frames.MainScreen.Profiles.center_grid import CenterGrid
from Main.View.Frames.MainScreen.bottom_frame import BottomFrame


class MainScreen(ttk.Frame):
    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        self.init_content()

    def init_content(self):
        ttk.Style().configure('mainscreen.topframe.TFrame', background="#87014F")
        ttk.Style().configure('mainscreen.centerGrid.TFrame', background="#201F1E")
        ttk.Style().configure('mainscreen.bottomFrame.TFrame', background="#2E4147")

        frame1 = TopFrame(parent=self, width=800, height=50,padding=[20,0,0,0], style='mainscreen.topframe.TFrame')
        frame1.pack_propagate(0)
        centergrid = CenterGrid(self, profiles=[1, 2, 3], width=800, height=300,padding=[0,20],style='mainscreen.centerGrid.TFrame')
        centergrid.pack_propagate(0)
        frame2 = BottomFrame(self, width=800, height=50,padding=[20,0,0,0],style='mainscreen.bottomFrame.TFrame')
        frame2.pack_propagate(0)
        frame1.grid(row=0)
        centergrid.grid(row=1)
        frame2.grid(row=2)
