from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class TopFrame(ttk.Frame):
    def __init__(self, parent,username, **options):
        super().__init__(parent, **options)
        self.init_content(username)

    def init_content(self, username):
        ttk.Style().configure('mainscreen.topframe.TLabel', background="#87014F",font="Helvetica 18", foreground="white")
        label = ttk.Label(self, text="Barman", width=8,style="mainscreen.topframe.TLabel")
        label.pack(side="left")

        frame = ttk.Frame(self, style='mainscreen.topframe.TFrame')
        frame.pack(side="right")
        label = ttk.Label(frame, text=username, style="mainscreen.topframe.TLabel", padding=[10,0])
        label.grid(row=0,column=0)
        image = Image.open("images/user-solid.png")
        image = image.resize((30, 30), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(image)
        button = Label(frame, background="#87014F",image=logo)
        button.photo = logo
        button.grid(row=0,column=1, padx=(10,0))
        label = ttk.Label(frame, text="|", style="mainscreen.topframe.TLabel", padding=[10, 0])
        label.grid(row=0, column=2)
        settings_image = Image.open("images/cog-solid.png")
        settings_image = settings_image.resize((30, 30), Image.ANTIALIAS)
        settings_logo = ImageTk.PhotoImage(settings_image)
        settings = Label(frame, background="#87014F", image=settings_logo)
        settings.photo = settings_logo
        settings.grid(row=0, column=3, padx=(0, 10))


