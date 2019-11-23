
import pyqrcode
from Main.Model.configuration import ConfigReader

def getQrCode(key,pwd):

    url = pyqrcode.create("barMan.at?key="+str(key)+"&pwd="+str(pwd))
    url.png('qrcode.png', scale=6, module_color=[0, 0, 0, 128], quiet_zone=7)
