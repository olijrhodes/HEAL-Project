import tkinter as tk
from tkinter import *
import pandas as pd
from tkcalendar import Calendar
from tkcalendar import *


CREAM = "mint cream"  # setting constant variables(background and foreground)
BLUE = "Cyan4"
YELLOW = "Yellow2"
BLACK = "Black"

main = Tk()  # creating main window
main.geometry("1100x600")  # setting the windows size, resizable, title and starting background
main.resizable(False, False)
main.title("Healthcare Application")
main.config(bg=BLUE)

# df = pd.read_csv("MOCK_DATA.csv")

Booking_at_GP_Label = Label(text="Booking at...", width=15)
Booking_at_GP_Label.grid(column=0, row=0)

GP = tk.StringVar()
GP_var_label = Label(textvariable=GP, width=10)
GP_var_label.grid(column=1, row=0)


hour_string = StringVar()
min_string = StringVar()
#last_value_sec = ""
last_value = ""
f = ('Times', 20)


def display_msg():
    date = cal.get_date()
    m = min_sb.get()
    h = sec_hour.get()
    #s = sec.get()
    t = f"Your appointment is booked for {date} at {m}:{h}."
    msg_display.config(text=t)


if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
    last_value = min_string.get()

#if last_value_sec == "59" and sec_hour.get() == "0":
#    min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)
if last_value == "59":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
    last_value_sec = sec_hour.get()

fone = Frame(main)
ftwo = Frame(main)

fone.place(x=300, y=300)
ftwo.place(x=300, y=300)

cal = Calendar(
    fone,
    selectmode="day",
    year=2021,
    month=2,
    day=3
)
cal.place(x=500, y=500)

min_sb = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=f,
    justify=CENTER
)
sec_hour = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    width=2,
    justify=CENTER
)

'''sec = Spinbox(
    ftwo,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=2,
    font=f,
    justify=CENTER
)'''

min_sb.grid(column=4, row=4)
sec_hour.grid(column=4, row=5)
#sec.pack(side=LEFT, fill=X, expand=True)

msg = Label(
    main,
    text="Hour  Minute",
    font=("Times", 12),
    bg="#cd950c"
)
msg.place(x=300, y=1000)

actionBtn = Button(
    main,
    text="Book Appointment",
    padx=10,
    pady=10,
    command=display_msg
)
actionBtn.place(x=500, y=500)

msg_display = Label(
    main,
    text="",
    bg="#cd950c"
)
msg_display.grid(column=5, row=5)


main.mainloop()
