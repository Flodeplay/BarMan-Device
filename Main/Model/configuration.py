import xml.etree.ElementTree as ET
from Main.Model.Class.profile import Profile
from Main.Model.Class.liquidsforbeverages import Liquidforbeverage
from Main.Model.Class.user import User
from Main.Model.Class.beverage import Beverage
from Main.Model.Class.device import Device
from Main.Model.Class.pump import Pump


class ConfigReader:
    def __init__(self):
        self.tree = ET.parse('config.xml')
        self.root = self.tree.getroot()

    def getkey(self):
        return int(self.root[0].find("key").text)

    def getDevice(self):
        return Device(self.root[0].find("key").text, self.root[0].find("pin").text, None,
                      self.root[0].find("userid").text, self.root[0].find("userprofile").text)

    def setDevice(self, device):
        self.root[0].find("pin").text = str(device.pin)
        self.root[0].find("userid").text = str(device.userid)
        self.root[0].find("userprofile").text = str(device.userprofile)

    def getuser(self):
        return User(self.root[1][0].text, self.root[1][1].text)

    def setuser(self, user):
        self.root[1][0].text = str(user.id)
        self.root[1][1].text = str(user.name)

    def getProfile(self):
        profile = self.root.find("profile")
        return Profile(profile[0].text, profile[1].text, self.getbeverages())

    def setProfile(self, profile):
        profilecontainer = self.root.find("profile")
        profilecontainer.find("id").text = str(profile.id)
        profilecontainer.find("name").text = str(profile.name)

    def getbeverages(self):
        beverages = []
        for beveragetree in self.root.find("beverages").findall('beverage'):
            pumps = []
            for pumptree in beveragetree.find("pumps").findall('pump'):
                pump = Liquidforbeverage(pumptree.find('containerID').text, pumptree.find('name').text,
                                         pumptree.find('amount').text)
                pumps.append(pump)
            beverage = Beverage(beveragetree.find('name').text, beveragetree.find('capacity').text, pumps)
            beverages.append(beverage)
        return beverages

    def setbeverages(self, beverages):
        beveragescontainer = self.root.find("beverages")
        for beverage in beveragescontainer.findall('beverage'):
            beveragescontainer.remove(beverage)
        for beverage in beverages:
            beverageelement = ET.SubElement(beveragescontainer, 'beverage')
            ET.SubElement(beverageelement, "name").text = str(beverage.name)
            ET.SubElement(beverageelement, "capacity").text = str(beverage.volume)
            pumpcontainer = ET.SubElement(beverageelement, "pumps")
            for pump in pumpcontainer.findall('pump'):
                pumpcontainer.remove(pump)
            for pump in beverage.pumps:
                pumpelement = ET.SubElement(pumpcontainer, 'pump')
                ET.SubElement(pumpelement, "containerID").text = str(pump.containerid)
                ET.SubElement(pumpelement, "name").text = str(pump.name)
                ET.SubElement(pumpelement, "amount").text = str(pump.amount)
                ET.dump(pumpelement)
            ET.dump(beverageelement)

    def getpumpconfiguration(self):
        pumps = []
        for pump in self.root.find("pumps").findall('pump'):
            pumpconfig = Pump(int(pump.find('containerID').text), pump.find('name').text)
            pumps.append(pumpconfig)
        return pumps

    def setPumpconfiguration(self, pumps):
        pumpcontainer = self.root.find("pumps")
        for pump in pumpcontainer.findall('pump'):
            pumpcontainer.remove(pump)
        for pump in pumps:
            pumpelement = ET.SubElement(pumpcontainer, 'pump')
            ET.SubElement(pumpelement, "name").text = str(pump.name)
            ET.SubElement(pumpelement, "containerID").text = str(pump.containerid)
            ET.dump(pumpelement)
