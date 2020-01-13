
import pyqrcode
from Main.Model.configuration import ConfigReader

def getQrCode(key,pwd):

    url = pyqrcode.create("f-parfuss.at/barman/app/login.php?key="+str(key)+"&pwd="+str(pwd))
    url.png('qrcode.png', scale=6, module_color=[0, 0, 0, 128], quiet_zone=7)
