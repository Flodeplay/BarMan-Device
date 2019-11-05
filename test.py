from Main.Modell.configuration import ConfigReader
from Main.Modell.Class.user import User
config = ConfigReader()
config.setuser(User(2, "Fritz"))
print(config.getuser())

