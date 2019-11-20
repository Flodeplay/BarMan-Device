from tkinter import ttk
from Main.Model.qrgenerator import getQrCode
from Main.View.Frames.Startup.register.qrcodeFrame import QrcodeFrame
from Main.View.Frames.Startup.register.infoPanel import InfoPanel


class RegisterScreen(ttk.Frame):
    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        self.init_content()

    def init_content(self):
        getQrCode("1931011631969","123445")
        s = ttk.Style()
        s.configure('register.left.TFrame', background="#87014F")
        s.configure('register.right.TFrame', background="#201F1E")
        leftpanel = QrcodeFrame(parent=self, width=400, height=400, style="register.left.TFrame")
        leftpanel.pack_propagate(0)
        leftpanel.grid(row=0,column=0)
        leftpanel = InfoPanel(parent=self, width=400, height=400, padding=20, style="register.right.TFrame")
        leftpanel.grid_rowconfigure(0, weight=2)
        leftpanel.grid_columnconfigure(0, weight=2)
        leftpanel.grid_propagate(0)
        leftpanel.grid(row=0,column=1)


