from tkinter import ttk
from tkinter import *
from Main.Model.qrgenerator import getQrCode
from Main.View.Frames.Startup.register.qrcodeFrame import QrcodeFrame
from Main.View.Frames.Startup.register.infoPanel import InfoPanel


class RegisterScreen(ttk.Frame):
    def __init__(self, key, pin, parent, **options):
        super().__init__(parent, **options)
        self.key = key
        self.pin = pin
        self.init_content()

    def init_content(self):
        getQrCode(self.key, self.pin)
        s = ttk.Style()
        s.configure('register.left.TFrame', background="#87014F")
        s.configure('register.right.TFrame', background="#201F1E")
        leftpanel = QrcodeFrame(parent=self, width=400, height=400, style="register.left.TFrame")
        leftpanel.pack(side=LEFT, expand=YES, fill=BOTH)
        leftpanel = InfoPanel(parent=self, key=self.key, pin=self.pin, width=400, height=400, padding=20, style="register.right.TFrame")
        leftpanel.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.leftpanel = leftpanel


