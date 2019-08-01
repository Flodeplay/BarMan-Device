import tkinter as tk

class Profile(tk.Frame):

    def init_content(self, name):
        canvas = tk.Canvas(self, width=200, height=260)
        canvas.pack()
        canvas['bg'] = self['bg']
        canvas.create_oval(5, 25, 195, 215, fill='gray', outline="")
        canvas.create_text(100,130, text="MK", fill="lightgray", font=("Helvetica", 80), width=200)
