import tkinter as tk
from tkinter import *


CREAM = "mint cream"  # setting constant variables(background and foreground)
BLUE = "Cyan4"
YELLOW = "Yellow2"
BLACK = "Black"


history_window = Tk()   # creates a window
history_window.geometry("1100x600")  # setting the windobooking_window size, resizable, title and starting background
history_window.resizable(False, False)
history_window.title("Healthcare Application - First Time Login")
history_window.config(bg=BLUE)


history_window.mainloop()
