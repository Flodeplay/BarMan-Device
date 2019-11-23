import tkinter
from tkinter import ttk
from Main.View.Frames.Drink.progress.progressbar import ProgressBar
def setup():
    root = tkinter.Tk()
    root.geometry('800x480')
    ttk.Style().configure('progressbar.TFrame', background="#201F1E")
    frame = ProgressBar(root, style="progressbar.TFrame", height=400, width=800)
    frame.grid_propagate(0)
    frame.grid(row=0, column=0, sticky="nsew")

    frame.tkraise()
    root.mainloop()

setup()
