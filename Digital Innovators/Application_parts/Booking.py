import tkinter as tk
from tkinter import *
import pandas as pd

CREAM = "mint cream"  # setting constant variables(background and foreground)
BLUE = "Cyan4"
YELLOW = "Yellow2"
BLACK = "Black"

main = Tk()  # creating main window
main.geometry("1100x600")  # setting the windows size, resizable, title and starting background
main.resizable(False, False)
main.title("Healthcare Application")
main.config(bg=BLUE)

df = pd.read_csv("MOCK_DATA.csv")
#print(df['city'][0:5])


#for city in df:
    #for n in city:
        #print(n)

Booking_at_GP_Label = Label(text="Booking at")
Booking_at_GP_Label.place(x=10, y=10)

GP = tk.StringVar()
GP_var_label = Label(textvariable=GP, width=10)
GP_var_label.place(x=80, y=10)

main.mainloop()