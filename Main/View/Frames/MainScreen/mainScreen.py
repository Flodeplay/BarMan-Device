from tkinter import *
from tkinter import ttk
from Main.View.Frames.MainScreen.top_frame import TopFrame
from Main.View.Frames.MainScreen.center_grid import CenterGrid
from Main.View.Frames.MainScreen.bottom_frame import BottomFrame


class MainScreen(ttk.Frame):
    def __init__(self, parent, username, beverages, **options):
        super().__init__(parent, **options)
        self.init_content(username, beverages)

    def init_content(self,username, beverages):
        ttk.Style().configure('mainscreen.topframe.TFrame', background="#87014F")
        ttk.Style().configure('mainscreen.centerGrid.TFrame', background="#201F1E")
        ttk.Style().configure('mainscreen.bottomFrame.TFrame', background="#2E4147")

        topframe = TopFrame(parent=self, username=username, width=800, height=50,padding=[10,0,0,0], style='mainscreen.topframe.TFrame')
        topframe.pack_propagate(0)
        topframe.grid(row=0)
        self.topframe = topframe

        bottomframe = BottomFrame(self, width=800, height=50,padding=[10,0,0,0],style='mainscreen.bottomFrame.TFrame')
        bottomframe.pack_propagate(0)
        bottomframe.grid(row=2)
        self.bottomframe = bottomframe

        self.offset_x = 0
        canvas = Canvas(self, bg="#201F1E", width=800, height=300, bd=0, highlightthickness=0, relief='ridge')
        ttk.Style().configure('mainscreen.centerGrid.TFrame', background="#201F1E")
        frame_left = CenterGrid(canvas, beverages, style='mainscreen.centerGrid.TFrame')
        self.centergrid = frame_left
        if (len(beverages) * (180 + 40) + 20) > 800:
            vertscroll = Scrollbar(canvas, orient='horizontal', command=canvas.xview())
            canvas.configure(xscrollcommand=vertscroll.set)

            def onFrameConfigure(canvas):
                canvas.configure(scrollregion=canvas.bbox("all"))

            def chat_width(event, canvas_frame):
                canvas.itemconfig(canvas_frame, width=len(beverages) * (180 + 40) + 20)

            def mouse_scroll(event, canvas):
                if event.delta:
                    canvas.xview_scroll(int(-1 * (event.delta / 120)), 'units')
                else:
                    if event.num == 5:
                        move = 2
                    else:
                        move = -1

                    canvas.yview_scroll(move, 'units')



            def on_press(evt):
                self.offset_x = evt.x_root

            def on_touch_scroll(evt):
                if evt.x_root - self.offset_x < 0:
                    evt.delta = -1
                else:
                    evt.delta = 1
                # canvas.yview_scroll(-1*(evt.delta), 'units') # For MacOS
                canvas.xview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows

            self.bind("<Enter>", lambda _: self.bind_all('<Button-1>', on_press), '+')
            self.bind("<Leave>", lambda _: self.unbind_all('<Button-1>'), '+')
            self.bind("<Enter>", lambda _: self.bind_all('<B1-Motion>', on_touch_scroll), '+')
            self.bind("<Leave>", lambda _: self.unbind_all('<B1-Motion>'), '+')
            self.bind('<Configure>', lambda event, canvas=canvas: onFrameConfigure(canvas))
            self.bind_all('<MouseWheel>', lambda event, canvas=canvas: mouse_scroll(event, canvas))
            self.bind_all('<Button-4>', lambda event, canvas=canvas: mouse_scroll(event, canvas))
            self.bind_all('<Button-5>', lambda event, canvas=canvas: mouse_scroll(event, canvas))
            vertscroll.pack(side=BOTTOM, fill=X)
            canvas.pack_propagate(0)
            canvas.grid(row=1)
            canvas_frame = canvas.create_window((4, 4), window=frame_left, anchor="center")
            canvas.bind('<Configure>', lambda event, canvas_frame=canvas_frame: chat_width(event, canvas_frame))
        else:
            canvas.pack_propagate(0)
            canvas.grid(row=1)
            frame_left.pack()

