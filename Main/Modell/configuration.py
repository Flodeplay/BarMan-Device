import xml.etree.ElementTree as ET
from Main.Modell.Class.recipe import Recipe
from Main.Modell.Class.pump import Pump
from Main.Modell.Class.user import User
from Main.Modell.Class.device import Device

class ConfigReader:
    def __init__(self):
        self.tree = ET.parse('config.xml')
        self.root = self.tree.getroot()

    def getkey(self):
        return int(self.root.find("key").text)

    def getuser(self):
        return User(self.root[1][0].text, self.root[1][1].text)

    def setuser(self, user):
        self.root[1][0].text = str(user.id)
        self.root[1][1].text = user.name

    def getrecipies(self):
        recipies = []
        for recipie in self.root.findall('recipie'):
            profile = Recipe(int(recipie.find('id').text), recipie.find('name').text, recipie.find('preset').text)
            recipies.append(profile)
        return recipies

    #def setRecipies(self):

    def getpumpconfiguration(self):
        pumps = []
        for pump in self.root.findall('pump'):
            pumpconfig = Recipe(int(pump.find('id').text),pump.find('name').text,pump.find('amount').text)
            pumps.append(pumpconfig)
        return pumps

    def get(self, name):
        return self.root.find(name).text


