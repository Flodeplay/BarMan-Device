from Main.Controller.mainController import MainController
from Main.View.application import Application
import logging
logging.getLogger().setLevel(logging.INFO)
root = Application()
app = MainController(root)
root.mainloop()
