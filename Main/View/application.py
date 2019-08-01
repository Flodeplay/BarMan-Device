import tkinter as tk
from Main.View.MainScreen.mainScreen import MainScreen
from Main.Modell.model import Model
from Main.View.Startup.dataLoading import  DataLoading
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
        if(self.model.username):
            loader = DataLoading(self, self.model.username,height=400,width=800)
            loader.pack_propagate(0)
            loader.pack()
        return root

