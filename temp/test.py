import tkinter
from tkinter import ttk
from Main.View.Frames.MainScreen.center_grid import CenterGrid
def setup():
    root = tkinter.Tk()
    root.geometry('800x480')
    canvas = tkinter.Canvas(root, bg='white')
    ttk.Style().configure('mainscreen.centerGrid.TFrame', background="#201F1E")
    profiles = [1, 2, 3, 4]
    frame_left = CenterGrid(canvas, profiles, style='mainscreen.centerGrid.TFrame')
    vertscroll = tkinter.Scrollbar(canvas, orient='horizontal', command=canvas.xview())
    canvas.configure(xscrollcommand=vertscroll.set)

    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def chat_width(event, canvas_frame):
        canvas.itemconfig(canvas_frame, width=len(profiles)*(250+40)+20)

    def mouse_scroll(event, canvas):
        if event.delta:
            canvas.xview_scroll(int(-1*(event.delta/120)), 'units')
        else:
            if event.num == 5:
                move = 2
            else:
                move = -1

            canvas.yview_scroll(move, 'units')

    offset_x = 0

    def on_press(evt):
        offset_x = evt.x_root

    def on_touch_scroll(evt):
        if evt.x_root - offset_x < 0:
            evt.delta = -1
        else:
            evt.delta = 1
        # canvas.yview_scroll(-1*(evt.delta), 'units') # For MacOS
        canvas.xview_scroll(int(-1 * (evt.delta / 120)), 'units')  # For windows

    root.bind("<Enter>", lambda _: root.bind_all('<Button-1>', on_press), '+')
    root.bind("<Leave>", lambda _: root.unbind_all('<Button-1>'), '+')
    root.bind("<Enter>", lambda _: root.bind_all('<B1-Motion>', on_touch_scroll), '+')
    root.bind("<Leave>", lambda _: root.unbind_all('<B1-Motion>'), '+')
    root.bind('<Configure>', lambda event, canvas=canvas: onFrameConfigure(canvas))
    root.bind_all('<MouseWheel>', lambda event, canvas=canvas: mouse_scroll(event, canvas))
    root.bind_all('<Button-4>', lambda event, canvas=canvas: mouse_scroll(event, canvas))
    root.bind_all('<Button-5>', lambda event, canvas=canvas: mouse_scroll(event, canvas))

    canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
    canvas_frame = canvas.create_window((4, 4), window=frame_left, anchor="nw")
    vertscroll.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.bind('<Configure>', lambda event, canvas_frame=canvas_frame: chat_width(event, canvas_frame))


    return root

root = setup()
root.mainloop()
