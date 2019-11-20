import tkinter as tk
from tkinter import ttk
from Main.Model.model import Model
from Main.View.Frames.Startup.startupscreen.startup import StartupScreen
from Main.View.Frames.Startup.register.register import RegisterScreen
from Main.View.Frames.MainScreen.mainScreen import MainScreen

class Application:

    def __init__(self):
        root = tk.Tk()
        root.geometry("800x400")
        root.resizable(0, 0)
        root['bg'] = "#201F1E"
        self.root = root
        self.model = Model()
        self.frames = {}
        self.__init_windows()
        self.root.mainloop()

    def __init_windows(self):
        self.clear()
        if not self.model.user:
            ttk.Style().configure('mainscreen.TFrame', background="#201F1E")
            mainscreen = MainScreen(self.root, style="mainscreen.TFrame", height=400, width=800)
            mainscreen.grid_propagate(0)
            mainscreen.grid()
            self.frames["mainscreen"] = mainscreen
        else:
            ttk.Style().configure('register.TFrame', background="#201F1E")
            register = RegisterScreen(self.root, style="register.TFrame", height=400, width=800)
            register.grid_propagate(0)
            register.grid()
            self.frames["register"] = register

    def clear(self):
        list = self.root.slaves()
        for l in list:
            l.destroy()
