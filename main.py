
import tkinter as tk
from tkinter import ttk
from tkinter import font


windowed_title = "this window should be fullscreen"

root = tk.Tk()

root.tk.call('source', './theme.tcl')
style = ttk.Style()
style.theme_use('azure')
# style.configure('.', font=default_font)

root.title(windowed_title)
root.geometry('600x400+200+200')

default_font = font.nametofont("TkDefaultFont")
default_font.configure(family='Ariel', size=24)

label = ttk.Button(root, text='Switch', style='Accentbutton').grid()

root.mainloop()