from tkinter import ttk, Canvas, Image, S
from PIL import Image,ImageTk

class Cupselection(ttk.Frame):

    def __init__(self, parent, beverage, **options):
        super().__init__(parent, **options)
        self.init_content(beverage)

    def init_content(self, beverage):
        ttk.Style().configure('cupselection.top.TLabel', background="#871352", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('cupselection.big.TLabel', background="#201F1E", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('cupselection.small.TLabel', background="#201F1E", font="Helvetica 15",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('cupselection.center.TFrame', background="#201F1E")
        ttk.Style().configure('cupselection.top.TFrame', background="#871352")
        topframe = ttk.Frame(self, height=120, width=800, style="cupselection.top.TFrame")
        ttk.Label(topframe, text="Bitte Wähle eine Größe aus", style="cupselection.top.TLabel").place(x=400, y=60, anchor="center")
        topframe.grid_propagate(0)
        topframe.grid(row=0)

        centerframe = CupselectionCenter(self, beverage, height=280, width=800, style="cupselection.center.TFrame")
        centerframe.pack_propagate(0)
        centerframe.grid(row=1)
        self.centerframe = centerframe


class CupselectionCenter(ttk.Frame):
    def __init__(self, parent, beverage, **options):
        super().__init__(parent, **options)
        self.profilesframes = []
        self.init_content(beverage)

    def init_content(self, beverage):
        #Todo calc ratio
        sizes = {"Small": 100, "Medium": 200, "Big": 300}
        index = 0
        for type, size in sizes.items():
            ttk.Style().configure('cupselection.center.cupsize.TFrame', background="#201F1E")
            frame = CupselectionProfile(self,size=size, type=type, width=160, height=200, style='cupselection.center.cupsize.TFrame')
            frame.grid_propagate(0)
            frame.grid(column=index, row=0,pady=45, padx=20)
            index += 1
            self.profilesframes.append(frame)


class CupselectionProfile(ttk.Frame):
    def __init__(self, parent, size, type, **options):
        super().__init__(parent, **options)
        self.size = size
        self.init_content(size, type)

    def init_content(self, size, type):
        canvas = Canvas(self,width=160, height=100, bg="#201F1E", bd=0, highlightthickness=0, relief='ridge')
        image = Image.open("images/cup.png")
        if type == "Small":
            image = image.resize((60, 60), Image.ANTIALIAS)
        if type == "Medium":
            image = image.resize((80, 80), Image.ANTIALIAS)
        if type == "Big":
            image = image.resize((100, 100), Image.ANTIALIAS)
        self.gif1 = ImageTk.PhotoImage(image)
        canvas.create_image(80, 100, image=self.gif1, anchor=S)
        canvas.grid(row=0, sticky="nsew", pady=(10, 10))
        label = ttk.Label(self, text=type, style="cupselection.big.TLabel")
        label.grid(row=1, sticky="nsew", pady=(10, 10))
        label = ttk.Label(self, text="("+str(size)+"ml"+")" , style="cupselection.small.TLabel",)
        label.grid(row=2, padx=(10, 10))


class ProgressBar(ttk.Frame):

    def __init__(self, parent, beverage,cupsize, **options):
        super().__init__(parent, **options)
        self.init_content(beverage, cupsize)

    def init_content(self, beverage,cupsize):
        ttk.Style().configure('progressbar.big.TLabel', background="#871352", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('progressbar.small.TLabel', background="#871352", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('progressbar.TLabel', background="#201F1E", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('progressbar.top.TFrame', background="#871352")
        topframe = ttk.Frame(self, height=200, width=800, style="progressbar.top.TFrame")
        ttk.Label(topframe, text="Dein Getränk wird gerade gemixt", style="progressbar.big.TLabel").place(x=400, y=70,
                                                                                                      anchor="center")
        ttk.Label(topframe, text="gleich ist es soweit :)", style="progressbar.small.TLabel").place(x=400, y=150,
                                                                                                anchor="center")
        topframe.grid_propagate(0)
        topframe.grid(row=0)

        ttk.Label(self, text="Dein Getränk: " + beverage.name +", "+str(cupsize)+"ml", style="progressbar.TLabel").place(x=400, y=350,
                                                                                                       anchor="center")
        TROUGH_COLOR = '#201F1E'
        BAR_COLOR = '#871352'
        ttk.Style().configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR, bordercolor=TROUGH_COLOR,
                              background=BAR_COLOR, lightcolor=BAR_COLOR, darkcolor=BAR_COLOR)
        self.progressbar = ttk.Progressbar(self, style="bar.Horizontal.TProgressbar", orient="horizontal", length=600,
                                           mode="determinate")
        self.progressbar.place(x=400, y=250, anchor="center")

    def setprogress(self, value):
        self.progressbar["value"] = int(value)

class DrinkFinished(ttk.Frame):
    def __init__(self, parent, beverage, **options):
        super().__init__(parent, **options)
        self.__init_content(beverage)

    def __init_content(self, beverage):
        ttk.Style().configure('drinkfinished.big.TLabel', background="#871352", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('drinkfinished.small.TLabel', background="#871352", font="Helvetica 20",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('drinkfinished.TLabel', background="#201F1E", font="Helvetica 35",
                              foreground="white", justify="center", anchor="center")
        ttk.Style().configure('drinkfinished.top.TFrame', background="#871352")
        topframe = ttk.Frame(self, height=200, width=800, style="drinkfinished.top.TFrame")

        ttk.Label(topframe, text="Dein Getränk ist fertig!", style="drinkfinished.big.TLabel").place(x=400, y=70,
                                                                                             anchor="center")
        #ttk.Label(topframe, text="", style="progressbar.small.TLabel").place(x=400, y=150, anchor="center")
        topframe.grid_propagate(0)
        topframe.grid(row=0)
        ttk.Label(self, text="Dein Getränk: " +str(beverage.name) , style="drinkfinished.TLabel").place(x=400, y=300,
                                                                                                       anchor="center")
