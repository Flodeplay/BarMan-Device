import tkinter as tk
from tkinter import ttk

class QrcodeFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        self.master = master
        super().__init__(**kwargs)
        self.init_content()

    def init_content(self):
        s = ttk.Style()
        s.configure('register.left.TLabel', font="Helvetica 25", foreground="white", padding=20, background="#87014F")
        ttk.Label(self, text="QR-Code", style="register.left.TLabel").pack(side="top")
        logo = tk.PhotoImage(file="qrcode.png")
        w1 = tk.Label(self, image=logo).pack(side="top")





