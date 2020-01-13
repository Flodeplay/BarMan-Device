from Main.Controller.mainController import MainController
from Main.View.application import Application
import logging

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    root = Application()
    app = MainController(root)
    root.mainloop()
