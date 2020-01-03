from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class QrcodeFrame(ttk.Frame):
    def __init__(self, parent, **options):
        super().__init__(parent, **options)
        self.init_content()

    def init_content(self):
        s = ttk.Style()
        s.configure('register.left.TLabel', font="Helvetica 25", foreground="white", padding=20, background="#87014F")
        ttk.Label(self, text="QR-Code", style="register.left.TLabel").pack(side="top")
        settings_image = Image.open("qrcode.png")
        settings_image = settings_image.resize((300, 300), Image.ANTIALIAS)
        settings_logo = ImageTk.PhotoImage(settings_image)
        settings = Label(self, background="#87014F", image=settings_logo)
        settings.photo = settings_logo
        settings.pack(side="top")





