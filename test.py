import tkinter
from tkinter import ttk
from Main.View.Frames.Error.Error import Mix_Exception

root = tkinter.Tk()
ttk.Style().configure('error.TFrame', background="#201F1E")
raise Mix_Exception("f")
root.mainloop()


main = []
