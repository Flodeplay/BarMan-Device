from Main.Controller.mainController import MainController
from Main.View.application import Application
root = Application()
app = MainController(root)
root.mainloop()
