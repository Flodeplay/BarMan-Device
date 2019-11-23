from Main.View.application import Application
from tkinter import ttk
from Main.Model.model import Model
from Main.View.Frames.Startup.startupscreen.startup import StartupScreen
from Main.View.Frames.Startup.register.register import RegisterScreen
from Main.View.Frames.MainScreen.mainScreen import MainScreen
from Main.View.Frames.Drink.progress.progressbar import ProgressBar

class MainController:
    def __init__(self, root):
        self.model = Model()
        self.root = root
        self.__init_register()

    def __init_register(self):
        if self.model.user:
            self.__init_mainscreen()
        else:
            if self.model.connector.connected:
                ttk.Style().configure('register.TFrame', background="#201F1E")
                register = RegisterScreen(parent=self.root, key=self.model.key, pin=self.model.device.pin, style="register.TFrame", height=400, width=800)
                register.leftpanel.refresh.config(command=self.registerlogin)
                register.grid_propagate(0)
                register.grid(row=0,column=0,sticky="nsew")
                self.root.frames["register"] = register
            #else:
                #todo implement errror screen

    def __init_mainscreen(self):
            ttk.Style().configure('mainscreen.TFrame', background="#201F1E")
            mainscreen = MainScreen(self.root, username=self.model.user.name, beverages=self.model.profile.beverages, style="mainscreen.TFrame", height=400, width=800)
            for frame in mainscreen.centergrid.profilesframes:
                frame.bind("<Button-1>",
                                lambda event, profile=frame.beverage:
                                self.makedrink(profile))
            mainscreen.grid_propagate(0)
            mainscreen.grid(row=0,column=0,sticky="nsew")
            self.root.frames["mainscreen"] = mainscreen

    def registerlogin(self):
        self.model.login()
        self.__init_mainscreen()
        frame = self.root.frames["mainscreen"]
        frame.tkraise()

    def __init_progress(self, beverage):
        ttk.Style().configure('progressbar.TFrame', background="#201F1E")
        frame = ProgressBar(self.root,beverage=beverage, style="progressbar.TFrame", height=400, width=800)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        return frame

    def __init_cupselection(self, beverage):
        

    def makedrink(self, beverage, cupsize):
        self.__init_progress(beverage)
        if beverage:
            if cupsize:
                ratio = self.calc_ratio(beverage, cupsize)
                #Todo start thread
                #Todo eventually move to controller class
            else:
                raise Exception("No Cupsize Selected")
        else:
            raise Exception("No Preset Configuration")
