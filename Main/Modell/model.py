from Main.Modell.connector import Connector
from Main.Modell.configreader import ConfigReader

class Model:
    def __init__(self):
        self.username = "Fritz"
        self.config = ConfigReader
        self.connector = Connector("193101163196977")
        self.__loadcontent()

    def __loadcontent(self):
        if self.connector.connected:
            self.device = self.connector.getDevice()
            self.user = self.connector.getuser()
            self.profile = self.connector.getrecipies()
            self.pumps = self.connector.getpumpconfiguration()
        else:
            #todo implement reader
            self.user = None



