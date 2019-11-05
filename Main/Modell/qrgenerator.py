
import pyqrcode
from Main.Modell.configuration import ConfigReader

def getQrCode(key,pwd):

    url = pyqrcode.create("https://f-parfuss.at")
    url.png('qrcode.png', scale=6, module_color=[0, 0, 0, 128], quiet_zone=7)
