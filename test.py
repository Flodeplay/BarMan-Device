from Main.Model.configuration import ConfigReader
from Main.Model.Class.user import User
from Main.Model.Class.pump import Pump
from Main.Model.connector import Connector

config = ConfigReader()
key = config.getkey()
connector = Connector(key)
device = connector.getdevice()
user = connector.getuser()
profile = connector.getprofile()
pumps = connector.getpumpconfiguration()

config.setDevice(device)
config.setuser(user)
config.setProfile(profile)
config.setPumpconfiguration(pumps)
config.setbeverages(profile.beverages)
config.tree.write('config.xml', encoding='UTF-8')
