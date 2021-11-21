
import tkinter as tk
from tkinter import ttk

def dark_style(root):
    ''' Return a dark style to the window'''
    
    style = ttk.Style(root)
    root.tk.call('source', 'azure dark/azure dark.tcl')
    style.theme_use('azure')
    style.configure("Accentbutton", foreground='white')
    style.configure("Togglebutton", foreground='white')
    return style