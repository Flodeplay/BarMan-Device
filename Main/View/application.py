from tkinter import *

class Application(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self['bg'] = "#201F1E"
        self.frames = {}
        self.attributes('-fullscreen', True)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 0, weight=1)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
