from Main.Modell.connector import Connector
from Main.Modell.configuration import ConfigReader
from Main.Modell.Class.cupsize import Cupsize
class Model:
    def __init__(self):
        self.config = ConfigReader()
        self.key = self.config.getkey()
        self.connector = Connector(self.key)
        self.__loadcontent()
    def __loadcontent(self):
        if self.connector.connected:
            self.login()
        else:
            self.key = self.config.getkey()
            self.user = self.config.getuser()
            self.profile = self.config.getrecipies()
            self.pumps = self.config.getpumpconfiguration()

    def __updateconfig(self):
            if self.config.getuser() != self.user:
                self.config.setuser(self.user)
            # if self.config.getrecipies() != self.profiles:
            #     #TODO implement Recepies update
            # if self.config.getpumpconfiguration() != self.pumps:
            #     #TODO implement Pumps update
            self.config.tree.write('config.xml', encoding='UTF-8')

    def login(self):
        if self.connector.connected:
            user = self.connector.getuser()
            if user:
                self.user = self.connector.getuser()
                self.profiles = self.connector.getrecipies()
                self.pumps = self.connector.getpumpconfiguration()
                self.__updateconfig()
            else:
                raise Exception("No User Connected with this machine")
        else:
            raise Exception("Connection to DB could not be Established")

    def makedring(self, preset, cupsize):
         if preset:
             if cupsize:
                 for pump, amount in preset.items():
                    #TODO implement drink handling, implement method like "processDrink" to acces the gpio ports
                    return None
             else:
                 raise Exception("No Cupsize Selected")
         else:
             raise Exception("No Preset Configuration")



