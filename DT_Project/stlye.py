import tkinter as tk
from tkinter import ttk

def set_styles():
    style = ttk.Style()

    # Set the style for the main window
    style.configure('TFrame', background='#f0f0f0', padding=5)
    style.configure('TButton', background='#4CAF50', foreground='#FFFFFF', padding=(10, 5))
    style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 12), padding=(0, 5))
    style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'), background = '#333', foreground = '#FFFFFF')



def create_header_frame(parent, title):
    header_frame = ttk.Frame(parent, style='TFrame')
    header_frame.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    header_label = ttk.Label(header_frame, text=title, style='Header.TLabel')
    header_label.grid(row=0, column=0)

    return header_frame
