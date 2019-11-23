from Main.Model.connector import Connector
from Main.Model.configuration import ConfigReader


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
            if self.config.getuser():
                self.device = self.config.getDevice()
                self.user = self.config.getuser()
                self.profile = self.config.getProfile()
                self.pumps = self.config.getpumpconfiguration()
            else:
                raise Exception("No User Connected with this machine")

    def __updateconfig(self):
        if self.config.getuser() != self.user:
            self.config.setuser(self.user)
        if self.config.getbeverages() != self.profile.beverages:
            self.config.setbeverages(self.profile.beverages)
        if self.config.getpumpconfiguration() != self.pumps:
            self.config.setPumpconfiguration(self.pumps)
        self.config.tree.write('config.xml', encoding='UTF-8')

    def login(self):
        if self.connector.connected:
            self.device = self.connector.getdevice()
            if self.device:
                self.user = self.connector.getuser()
                if self.user:
                    self.profile = self.connector.getprofile()
                    self.pumps = self.connector.getpumpconfiguration()
                    self.__updateconfig()
                else:
                    raise Exception("No User Connected with this machine")
            else:
                raise Exception("Internal Error")
        else:
            raise Exception("Connection to DB could not be Established")

    def makedring(self, preset, cupsize):
        if preset:
            if cupsize:
                for pump, amount in preset.items():
                    # TODO implement drink handling, implement method like "processDrink" to acces the gpio ports
                    return None
            else:
                raise Exception("No Cupsize Selected")
        else:
            raise Exception("No Preset Configuration")
