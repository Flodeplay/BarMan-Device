import tkinter
from Main.View.Frames.Drink.cupselection.cupsize import Cupseletion

root = tkinter.Tk()
Cupseletion(root, beverage=1, height=400, width=800).grid()
root.mainloop()
