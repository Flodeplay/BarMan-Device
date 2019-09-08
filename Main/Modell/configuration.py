import xml.etree.ElementTree as ET
from Main.Modell.Class.recipe import Recipe
from Main.Modell.Class.pump import Pump
from Main.Modell.Class.user import User
from Main.Modell.Class.device import Device

class ConfigReader:
    def __init__(self):
        tree = ET.parse('config.xml')
        self.root = tree.getroot()

    def getkey(self):
        return self.root[0][0].text

    def getDevice(self):
        return

    def getuser(self):
        return User(self.root[1][0].text, self.root[1][1].text)

    def setUser(self, user):
        return

    def getrecipies(self):
        return

    def getpumpconfiguration(self):
        return

