from Main.Model.connector import Connector
from Main.Model.configuration import ConfigReader
from Main.Model.GPIO import *
import time
import logging
import traceback

class Model:
    def __init__(self):
        self.config = ConfigReader()
        self.key = self.config.getkey()
        self.connector = Connector(self.key)
        self.__load_content()

    def __load_content(self):
        if self.connector.connected:
            try:
                self.login_from_db()
                logging.info("Login from DB Complete")
            except:
                self.user = None
        else:
            if self.config.getuser():
                self.login_from_config()
                logging.info("Login from XML Complete")
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

    def generatePin(self):
        import random, string
        x = ''.join(random.choices(string.digits, k=6))
        self.device.pin = x
        self.config.setDevice(self.device)
        self.connector.set_pin(self.device.pin)

    def login_from_db(self):
        if self.connector.connected:
            self.device = self.connector.getdevice()
            if self.device and self.device.userid:
                self.user = self.connector.getuser()
                if self.user:
                    self.profile = self.connector.getprofile()
                    self.pumps = self.connector.getpumpconfiguration()
                    self.__update_config()
                else:
                    raise Exception("No User Connected with this machine")
            else:
                raise Exception("No User Connected with this machine")
        else:
            raise Exception("Connection to DB could not be Established")

    def calc_ratio(self, beverage, cupsize):
        relations = {}
        if beverage:
            if cupsize:
                for liquid in beverage.pumps:
                    relation = (int(liquid.amount) / int(beverage.volume())) * int(cupsize)
                    relations[liquid.containerid] = relation
                return relations
            else:
                raise Exception("No Cupsize Selected")
        else:
            raise Exception("No Drink Configuration")

    def makedrink(self, beverage, progressscreen, callback, args):
        ports = [[17,20],[27,20],[22,18],[23,18]]
        progresss = 100/len(beverage.pumps)
        #Relai
        #17, 27, 22, 23
        for pump in beverage.pumps:
            acessPort(ports[pump.containerid-1][0],(pump.amount/ports[pump.containerid-1][1]))
            progressscreen.setprogress(progresss*pump.containerid-1)

        callback(args,beverage)

    def login_new_user(self, callback):
        logging.info("Creating new request for userdata")
        try:
            if self.user:
                if self.user.id != self.connector.getdevice().userid:
                    callback()
                else:
                    time.sleep(3)
                    self.login_new_user(callback)
            else:
                if self.connector.getdevice().userid:
                    callback()
                else:
                    time.sleep(3)
                    self.login_new_user(callback)
        except Exception as e:
            traceback.print_exc()
            print(e)
            self.login_new_user(callback)


