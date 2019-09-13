import tkinter as tk
from tkinter import ttk
from Main.Modell.model import Model
from Main.View.Frames.Startup.startupscreen.startup import StartupScreen
class Application:

    def __init__(self, name):
        self.name = name


    def run(self):
        self.model = Model()
        self.root = self.__init_windows()
        self.root.mainloop()

    def __init_windows(self):
        root = tk.Tk()
        root.geometry("800x400")
        root.resizable(0, 0)
        root['bg'] = "#201F1E"
        if(self.model.user):
            ttk.Style().configure('startup.TFrame', padding=20,  background="#87014F")
            loader = StartupScreen(root, style="startup.TFrame", height=400, width=800)
            loader.pack_propagate(0)
            loader.pack()

        return root

