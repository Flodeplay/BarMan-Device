import tkinter as tk
from Main.Modell.model import Model
from Main.View.Frames.Startup.register.register import RegisterScreen
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
            loader = RegisterScreen(self, height=400, width=800)
            loader.pack_propagate(0)
            loader.pack()

        return root

