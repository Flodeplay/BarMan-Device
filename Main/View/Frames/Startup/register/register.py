from tkinter import ttk
from Main.Modell.qrgenerator import getQrCode
from Main.View.Frames.Startup.register.qrcodeFrame import QrcodeFrame
from Main.View.Frames.Startup.register.infoPanel import InfoPanel


class RegisterScreen(ttk.Frame):
    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content()

    def init_content(self):
        #generate QR Code
        getQrCode("","")
        s = ttk.Style()
        s.configure('register.left.TFrame', padding=20, background="#87014F")
        s.configure('register.right.TFrame', spacing=20, background="#201F1E")
        leftpanel = QrcodeFrame(master=self, width=400, height=400, style="register.left.TFrame")
        leftpanel.pack_propagate(0)
        leftpanel.pack(side="left")
        leftpanel = InfoPanel(master=self, width=400, height=400, style="register.right.TFrame")
        leftpanel.pack_propagate(0)
        leftpanel.pack(side="right")

