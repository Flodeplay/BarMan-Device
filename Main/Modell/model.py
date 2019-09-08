from Main.Modell.connector import Connector
from Main.Modell.configuration import ConfigReader

class Model:
    def __init__(self):
        self.config = ConfigReader()
        self.connector = Connector(self.config.getkey())
        self.__loadcontent()

    def __loadcontent(self):
        if self.connector.connected:
            self.device = self.connector.getDevice()
            self.user = self.connector.getuser()
            self.profiles = self.connector.getrecipies()
            self.pumps = self.connector.getpumpconfiguration()
            #self.updateconfig()

        else:
            self.device = self.config.getDevice()
            self.user = self.config.getuser()
            self.profile = self.config.getrecipies()
            self.pumps = self.config.getpumpconfiguration()

    def updateconfig(self):
            if self.config.getuser() != self.user:
                self.config.setUser(self.user)
            if self.config.getrecipies() != self.profiles:
                #TODO implement Recepies update
                self.config.setUser(self.user)
            if self.config.getpumpconfiguration() != self.pumps:
                #TODO implement Pumps update
                self.config.setUser(self.user)
