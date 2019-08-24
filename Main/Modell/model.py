from Main.Modell.connector import Connector
from Main.Modell.configreader import ConfigReader

class Model:
    def __init__(self):
        self.config = ConfigReader()
        self.connector = Connector(self.config.getkey())
        self.__loadcontent()

    def __loadcontent(self):
        if self.connector.connected:
            self.device = self.connector.getDevice()
            self.user = self.connector.getuser()
            self.profile = self.connector.getrecipies()
            self.pumps = self.connector.getpumpconfiguration()
        else:
            self.device = self.config.getDevice()
            self.user = self.config.getuser()
            self.profile = self.config.getrecipies()
            self.pumps = self.config.getpumpconfiguration()

