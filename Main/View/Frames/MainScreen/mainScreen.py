import tkinter as tk
from Main.View.Frames.MainScreen.top_frame import Topframe
from Main.View.Frames.MainScreen.Profiles import CenterGrid
from Main.View.Frames.MainScreen.bottom_frame import BottomFrame


class MainScreen(tk.Frame):
    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content()

    def init_content(self):
        frame1 = Topframe(self, width=800, height=50, background="#787878")
        frame1.pack_propagate(0)
        centergrid = CenterGrid(self, profiles=[1, 2, 3], width=800, height=300)
        centergrid.pack_propagate(0)
        frame2 = BottomFrame(self, width=800, height=50, background="#b22222")
        frame2.pack_propagate(0)
        frame1.grid(row=0)
        centergrid.grid(row=1)
        frame2.grid(row=2)
