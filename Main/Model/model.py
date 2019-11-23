from Main.Model.connector import Connector
from Main.Model.configuration import ConfigReader


class Model:
    def __init__(self):
        self.config = ConfigReader()
        self.key = self.config.getkey()
        self.connector = Connector(self.key)
        self.__load_content()

    def __load_content(self):
        if self.connector.connected:
            self.login_from_db()
        else:
            if self.config.getuser():
                self.login_from_config()
            else:
                raise Exception("No User Connected with this machine")

    def __update_config(self):
        if self.config.getuser() != self.user:
            self.config.setuser(self.user)
        if self.config.getbeverages() != self.profile.beverages:
            self.config.setbeverages(self.profile.beverages)
        if self.config.getpumpconfiguration() != self.pumps:
            self.config.setPumpconfiguration(self.pumps)
        self.config.tree.write('config.xml', encoding='UTF-8')

    def login_from_config(self):
        self.device = self.config.getDevice()
        self.user = self.config.getuser()
        self.profile = self.config.getProfile()
        self.pumps = self.config.getpumpconfiguration()

    def login_from_db(self):
        if self.connector.connected:
            self.device = self.connector.getdevice()
            if self.device:
                self.user = self.connector.getuser()
                if self.user:
                    self.profile = self.connector.getprofile()
                    self.pumps = self.connector.getpumpconfiguration()
                    self.__update_config()
                else:
                    raise Exception("No User Connected with this machine")
            else:
                raise Exception("Internal Error")
        else:
            raise Exception("Connection to DB could not be Established")


    def calc_ratio(self, beverage, cupsize):
        relations={}
        if beverage:
            if cupsize:
                for liquid in beverage.pumps:
                    relation = (int(liquid.amount)/int(beverage.volume))*int(cupsize)
                    relations[liquid.containerid] = relation
                return relations
            else:
                raise Exception("No Cupsize Selected")
        else:
            raise Exception("No Drink Configuration")
