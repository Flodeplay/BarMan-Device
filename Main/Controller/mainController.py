from Main.View.application import Application
from tkinter import ttk
from tkinter import *
from Main.Model.model import Model
from Main.View.Frames.Startup.register.register import RegisterScreen
from Main.View.Frames.MainScreen.mainScreen import MainScreen
from Main.View.Frames.Drink.drink import *
import threading
import time

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
            mainscreen = MainScreen(self.root, username=self.model.user.name, beverages=self.model.profile.beverages, style="mainscreen.TFrame")
            mainscreen.topframe.logout.bind("<Button-1>", self.logout)
            for frame in mainscreen.centergrid.profilesframes:
                frame.bind("<Button-1>",
                                lambda event, beverage=frame.beverage:
                                self.__init_cupselection(beverage))
                for child in frame.winfo_children():
                    child.bind("<Button-1>",
                               lambda event, beverage=frame.beverage:
                               self.__init_cupselection(beverage))
            mainscreen.grid(row=0,column=0,sticky="nsew")
            self.root.frames["mainscreen"] = mainscreen

    def registerlogin(self):
        self.model.login()
        self.__init_mainscreen()
        frame = self.root.frames["mainscreen"]
        frame.tkraise()

    def __init_progress(self, beverage, cupsize):
        ttk.Style().configure('progressbar.TFrame', background="#201F1E")
        frame = ProgressBar(self.root,beverage=beverage,cupsize=cupsize, style="progressbar.TFrame")
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        return frame

    def __init_cupselection(self, beverage):
        ttk.Style().configure('cupselection.TFrame', background="#201F1E")
        cupselection = Cupselection(self.root, beverage=beverage, height=400, width=800, style="cupselection.TFrame")
        cupselection.grid(row=0, column=0, sticky="nsew")
        cupselection.tkraise()
        for frame in cupselection.centerframe.profilesframes:
            frame.bind("<Button-1>",
                       lambda event, beverage=beverage, cupsize=frame.size:
                       self.make_drink(beverage, cupsize))
            for child in frame.winfo_children():
                child.bind("<Button-1>",
                           lambda event, beverage=beverage, cupsize=frame.size:
                           self.make_drink(beverage, cupsize))

    def __init_drink_finished(self, beverage):
        ttk.Style().configure('drinkfinished.TFrame', background="#201F1E")
        drinkfinished = DrinkFinished(self.root, beverage=beverage, height=400, width=800, style="cupselection.TFrame")
        drinkfinished.grid(row=0, column=0, sticky="nsew")
        drinkfinished.tkraise()
        return drinkfinished

    def make_drink(self, beverage, cupsize):
        progressscreen = self.__init_progress(beverage, cupsize)
        if beverage:
            if cupsize:
                ratio = self.model.calc_ratio(beverage, cupsize)
                thread = threading.Thread(target=self.model.makedrink, args=(beverage,progressscreen, self.finished_mix, "mainscreen"))
                thread.start()
            else:
                raise Exception("No Cupsize Selected")
        else:
            raise Exception("No Preset Configuration")

    def raise_frame(self,frame):
        self.root.frames[frame].tkraise()

    def finished_mix(self, frame, beverage):
        drinkfinished = self.__init_drink_finished(beverage=beverage)
        time.sleep(5)
        self.root.frames[frame].tkraise()
        drinkfinished.destroy()

    def logout(self):
        raise Exception("not implemted")
