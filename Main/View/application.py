from tkinter import *

class Application(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self['bg'] = "#201F1E"
        self.frames = {}
        #self.resizable(0, 0)
        #self._geom='200x200+0+0'
        #self.geometry("{0}x{0}+0+0".format(
        #self.winfo_screenwidth(), self.winfo_screenheight()))
        #self.bind('<Escape>',self.toggle_geom)
        #self.attributes('-fullscreen', True)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 0, weight=1)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
