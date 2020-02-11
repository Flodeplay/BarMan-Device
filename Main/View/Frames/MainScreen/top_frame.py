from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class TopFrame(ttk.Frame):
    def __init__(self, parent,username, **options):
        super().__init__(parent, **options)
        self.init_content(username)

    def init_content(self, username):
        ttk.Style().configure('mainscreen.topframe.TLabel', background="#87014F",font="Helvetica 25", foreground="white")
        label = ttk.Label(self, text=username+"'s Barman",style="mainscreen.topframe.TLabel")
        label.pack(side="left")

        frame = ttk.Frame(self, style='mainscreen.topframe.TFrame')
        frame.pack(side="right")
        logo = Image.open("images/tint-solid.png")
        logo = logo.resize((25, 32), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        button = Label(frame, background="#87014F",image=logo)
        button.photo = logo
        button.grid(row=0,column=2, padx=(15))
        self.cleanButton = button
        label = ttk.Label(frame, text="|", style="mainscreen.topframe.TLabel", padding=[10, 10])
        label.grid(row=0, column=3)
        settings_image = Image.open("images/sign-out-alt-solid.png")
        settings_image = settings_image.resize((40, 30), Image.ANTIALIAS)
        settings_logo = ImageTk.PhotoImage(settings_image)
        settings = Label(frame, background="#87014F", image=settings_logo)
        settings.photo = settings_logo
        settings.grid(row=0, column=4, padx=(15))
        self.logout = settings


