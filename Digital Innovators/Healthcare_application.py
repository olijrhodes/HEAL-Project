from tkinter import *  # imports
import pandas as pd
from win10toast import ToastNotifier
import time
import string
import random
from tkcalendar import *
import datetime

selected_font = ("Microsoft YaHei UI Light", 11)

CREAM = "mint cream"  # setting constant variables(background and foreground)
BLUE = "Cyan4"
YELLOW = "Yellow2"
BLACK = "Black"

notifier = ToastNotifier()

dataframe = pd.read_csv("MOCK_DATA.csv", on_bad_lines='skip')

login_window = Tk()  # creating main window
login_window.geometry("1100x600")  # setting the windobooking_window size, resizable, title and starting background
login_window.resizable(False, False)
login_window.title("Healthcare Application - First Time Login")
login_window.config(bg=BLUE)

login_frame = Frame(login_window, height=560, width=400, bg=CREAM)
login_frame.pack(pady=20)
login_logo_frame = Frame(login_frame, bg=CREAM)
login_logo_frame.pack(pady=(0, 100))
login_details_Frame = Frame(login_frame, width=400, height=300, bg=CREAM)
login_details_Frame.pack(pady=(0, 175))

main = Toplevel()  # creating main window
main.geometry("1100x600")  # setting the windobooking_window size, resizable, title and starting background
main.resizable(False, False)
main.title("Healthcare Application - Home")
main.config(bg=BLUE)
main.withdraw()

setting_window = Toplevel()
setting_window.geometry("1100x600")
setting_window.resizable(False, False)
setting_window.title("Healthcare Application - Settings")
setting_window.config(bg=BLUE)
setting_window.withdraw()

second_login_window = Toplevel()  # creating main window
second_login_window.geometry("1100x600")
second_login_window.resizable(False, False)
second_login_window.title("Healthcare Application - Login")
second_login_window.config(bg=BLUE)
second_login_window.withdraw()

booking_selection = Toplevel()
booking_selection.resizable(False, False)
booking_selection.title("Healthcare Application - Booking Selection")
booking_selection.geometry("500x400")
booking_selection.config(bg=BLUE)
booking_selection.withdraw()

booking_window = Toplevel()
booking_window.resizable(False, False)
booking_window.title("Healthcare Application - Booking")
booking_window.geometry("500x400")
booking_window.config(bg=BLUE)
booking_window.withdraw()

second_login_background_frame = Frame(second_login_window, height=560, width=400, bg=CREAM)
second_login_background_frame.pack(pady=20)
second_login_logo_frame = Frame(second_login_background_frame, width=400, bg=CREAM)
second_login_logo_frame.pack(pady=10)
second_login_details_Frame = Frame(second_login_background_frame, width=400, bg=CREAM)
second_login_details_Frame.pack()

prescription_window = Toplevel()
prescription_window.resizable(False, False)
prescription_window.title("Healthcare Application - Prescriptions")
prescription_window.geometry("1100x600")
prescription_window.config(bg=BLUE)
prescription_window.withdraw()

checkInt = IntVar()  # creating the check button's integer variable to live update the value
checkInt.set(0)  # setting the IntVar to 0 by default

contrastMode = StringVar()  # creating a StringVar for the button text
contrastMode.set("High Contrast mode [off]")

header_frame = Frame(main, bg=BLUE)
header_frame.grid(row=0)


def on_enter_email(e):
    if email_entry.get() == "Email":
        email_entry.delete(0, "end")


def on_leave_email(e):
    username = email_entry.get()
    if username == "":
        email_entry.insert(0, "Email")


def on_enter_password(e):
    if password_entry.get() == "Password":
        password_entry.delete(0, "end")
        password_entry.config(show="*")


def on_leave_password(e):
    password = password_entry.get()
    if password == "":
        password_entry.insert(0, "Password")
        password_entry.config(show="")


def setting_btn_on():
    main.withdraw()
    setting_window.deiconify()


def setting_btn_off():
    main.deiconify()
    setting_window.withdraw()


def check_login_details():
    searching = dataframe.loc[dataframe["first_name"] + dataframe["last_name"] == firstname.get() + lastname.get()]
    index = searching.index
    print(index)
    print(searching)

    Lastname = dataframe["last_name"]
    Address = dataframe["street_address"]
    Postcode = dataframe["post_code"]
    Medical_number = dataframe["medical_number"]

    try:
        if str(Lastname[index].item()) == str(lastname.get()) and \
                str(Address[index].item()) == str(address.get()) and \
                str(Postcode[index].item()) == str(postcode.get()) and \
                str(Medical_number[index].item()) == str(healthnumber.get()):
            login_window.withdraw()
            main.deiconify()

            characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
            length = 12
            random.shuffle(characters)
            password = []
            for i in range(length):
                password.append(random.choice(characters))
            random.shuffle(password)
            dataframe.loc[dataframe[dataframe["first_name"] + dataframe[
                "last_name"] == firstname.get() + lastname.get()].index.values, "password"] = "".join(password)
            dataframe.to_csv("MOCK_DATA.csv")

        else:
            print("incorrect")
    except ValueError:
        notifier.show_toast("Details not in our database.",
                            "Please check spelling and try again",
                            duration=3,
                            threaded=True)
        login_enter["state"] = "disabled"
        time.sleep(3)
        login_enter["state"] = "normal"

    except EXCEPTION as e:
        print(e)


def show_login_page():
    second_login_window.deiconify()
    login_window.withdraw()


# Login Page
login_logo = PhotoImage(file="App Logo.png")
login_logo_label = Label(login_logo_frame, image=login_logo)
login_logo_label.pack(padx=125, pady=20)

second_login_logo = PhotoImage(file="App Logo.png")
second_login_logo_label = Label(second_login_logo_frame, image=second_login_logo)
second_login_logo_label.pack(padx=125, pady=20)

firstname = Entry(login_details_Frame)
firstname.insert(0, "Firstname")
firstname.grid(row=0, column=0, pady=(0, 10), padx=(0, 10))

lastname = Entry(login_details_Frame)
lastname.insert(0, "Lastname")
lastname.grid(row=0, column=1, pady=(0, 10), padx=(10, 0))

address = Entry(login_details_Frame)
address.insert(0, "Address")
address.grid(row=1, column=0, pady=(0, 10), padx=(0, 10))

postcode = Entry(login_details_Frame)
postcode.insert(0, "Postcode")
postcode.grid(row=1, column=1, pady=(0, 10), padx=(10, 0))

healthnumber = Entry(login_details_Frame)
healthnumber.insert(0, "Health Number")
healthnumber.grid(row=2, column=0, columnspan=2, pady=(0, 5))

login_enter = Button(login_details_Frame, text="Enter", command=check_login_details, width=17)
login_enter.grid(row=3, column=0, columnspan=2, pady=(5, 0))

login_option = Button(login_frame, text="Already have account? Login", command=show_login_page)
login_option.place(x=150, y=500)


def show_booking_selection():
    booking_selection.deiconify()
    main.withdraw()


# Main Window


booking_header_btn = Button(header_frame, bg=CREAM, text="Booking", height=2, width=20, command=show_booking_selection)
booking_header_btn.grid(row=0, column=0, padx=45, pady=10)

hour_string = IntVar()
min_string = IntVar()
# last_value_sec = ""
last_value = ""
f = ('Times', 20)


def booking_back():
    booking_window.withdraw()
    booking_selection.deiconify()


booking_back_btn = Button(booking_window, text="<--", command=booking_back)
booking_back_btn.place(x=0, y=0)


def show_booking_page():
    booking_selection.withdraw()
    booking_window.deiconify()


book_appointment_button = Button(booking_selection, text="Book an appointment", justify=CENTER, height=4, width=25,
                                 command=show_booking_page)
book_appointment_button.pack(pady=(25, 0))


def display_msg():
    date = cal.get_date()
    m = min_sb.get()
    h = sec_hour.get()
    # s = sec.get()
    t = f"Your appointment is booked for {date} at {m}:{h}."
    msg_display.config(text=t)


if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
    last_value = min_string.get()

# if last_value_sec == "59" and sec_hour.get() == "0":
#    min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)
# the code messaged out is to show that we can also add seconds in, but decided there is no need for that
if last_value == "59":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)

fone = Frame(booking_window)
ftwo = Frame(booking_window)

today = datetime.date.today()

fone.pack(pady=10)
ftwo.pack(pady=10)

cal = Calendar(
    fone,
    selectmode="day",
    year=today.year,
    month=today.month,
    day=today.month,
    locale='en_UK'

)
cal.pack()

min_sb = Spinbox(
    ftwo,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    font=selected_font,
    justify=CENTER,
    bg=BLUE
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

min_sb.pack(side=LEFT, fill=X, expand=True)
sec_hour.pack(side=LEFT, fill=X, expand=True)
# sec.pack(side=LEFT, fill=X, expand=True)

msg = Label(
    booking_window,
    text="Hour  Minute",
    font=("Times", 12),
    bg=BLUE
)
msg.pack(side=TOP)

actionBtn = Button(
    booking_window,
    text="Book Appointment",
    padx=10,
    pady=10,
    command=display_msg
)
actionBtn.pack(pady=10)

msg_display = Label(
    booking_window,
    text="",
    bg=BLUE
)
msg_display.pack(pady=10)

listbox = Listbox(prescription_window, width=100, height=46, bg="white")
listbox.place(x=50, y=155, width=500, height=400)

booking_back_btn = Button(booking_window, text="<--", command=booking_back)
booking_back_btn.place(x=0, y=0)


def prescription_window_open():
    listbox.delete(0, END)
    prescription_window.deiconify()
    main.withdraw()
    searching = dataframe.loc[dataframe["email"] == email_entry.get()]
    index = searching.index

    First = dataframe["first_name"]
    first_name = First[index].item()

    Surname = dataframe["last_name"]
    sur_name = Surname[index].item()

    name = "Showing medication for " + first_name + " " + sur_name
    nameLabel = Label(prescription_window, bg='cyan4', fg='white', font=("Verdana", 17))
    nameLabel.place(x=50, y=50)
    nameLabel.config(text=name)

    Medication = dataframe["med1"]
    medication = Medication[index].item()
    str_medication = str(medication)
    split_medication = str_medication.split(',')
    for item in split_medication:
        listbox.insert("end", item)


def prescription_back():
    prescription_window.withdraw()
    main.deiconify()


prescription_back_btn = Button(prescription_window, text="<--", command=prescription_back)
prescription_back_btn.place(x=0, y=0)

medication_header_btn = Button(header_frame, bg=CREAM, text="Medication", height=2, width=20)
medication_header_btn.grid(row=0, column=1, padx=45, pady=10)

prescriptions_header_btn = Button(header_frame, bg=CREAM, text="Prescriptions", command=prescription_window_open, height=2, width=20)
prescriptions_header_btn.grid(row=0, column=2, padx=45, pady=10)

after_app_chat = Button(header_frame, bg=CREAM, text="After Appointment Chat", height=2, width=20)
after_app_chat.grid(row=0, column=3, padx=45, pady=10)

setting_btn = Button(header_frame, bg=CREAM, text=u"\u2699", height=1, width=3, font=('Helvatical bold', 15),
                     command=setting_btn_on)
setting_btn.grid(row=0, column=4, padx=45, pady=10)


# first time login page


def login_confirm(e):
    searching = dataframe.loc[dataframe["email"] == email_entry.get()]
    index = searching.index
    Password = dataframe["password"]
    try:
        if str(Password[index].item()) == str(password_entry.get()):
            second_login_window.withdraw()
            main.deiconify()
        else:
            print("Incorrect email/password")
    except ValueError:
        print("Incorrect email/password")


email_entry = Entry(second_login_details_Frame, fg="Black", bg="White", font=("Microsoft YaHei UI Light", 11), bd=0)
email_entry.grid(row=0, column=0, pady=(100, 0))
email_entry.insert(0, "Email")

email_entry.bind("<FocusIn>", on_enter_email)
email_entry.bind("<FocusOut>", on_leave_email)

password_entry = Entry(second_login_details_Frame, show="", fg="Black", bg="White",
                       font=("Microsoft YaHei UI Light", 11), bd=0)

password_entry.grid(row=0, column=1, pady=(100, 0))
password_entry.insert(0, "Password")

password_entry.bind("<FocusIn>", on_enter_password)
password_entry.bind("<FocusOut>", on_leave_password)
password_entry.bind("<Return>", login_confirm)

second_login_confirm = Button(second_login_details_Frame, text="Confirm", command=login_confirm)
second_login_confirm.grid(row=1, column=0, columnspan=2, pady=(10, 300))

# Settings Page

settings_back_btn = Button(setting_window, text="<--", command=setting_btn_off)
settings_back_btn.grid(row=0, column=0)


def ContrastCheck():  # checking whether to change the accessibility options
    if checkInt.get() == 0:
        HighContrast()
        checkInt.set(1)
        contrastMode.set("High Contrast Mode [on]")  # changing the button text to show the accessibility status
    elif checkInt.get() == 1:
        LowContrast()
        checkInt.set(0)
        contrastMode.set("High Contrast Mode [off]")


windows = [main, header_frame, login_window, login_frame, login_logo_frame, login_details_Frame,
           setting_window, second_login_window, booking_window, second_login_background_frame,
           second_login_logo_frame, second_login_details_Frame, fone, ftwo]

widgets = [booking_header_btn,
           medication_header_btn, prescriptions_header_btn,
           after_app_chat, setting_btn, settings_back_btn,
           firstname, lastname, address, postcode, healthnumber,
           login_enter, login_option, login_logo_label, second_login_logo_label,
           login_enter, login_option, booking_back_btn, min_sb, sec_hour,
           actionBtn, second_login_confirm]

labels = [msg, msg_display]


def HighContrast():  # creating a block to change the background to black and the foreground to yellow
    for window in windows:
        window.config(bg=BLACK)
        setting_window.config(bg=BLACK)

    for widget in widgets:
        widget.configure(bg="Yellow")

    for label in labels:
        label.config(bg=BLACK, fg=YELLOW)


def LowContrast():  # creating a block to change the background to blue and the foreground to cream
    for window in windows:
        window.config(bg=BLUE)
        setting_window.config(bg=BLUE)

    for widget in widgets:
        widget.configure(bg=CREAM)

    for label in labels:
        label.config(bg=BLUE, fg=CREAM)


accessButton = Button(main,  # generic test button
                      textvariable=contrastMode,
                      bg=CREAM, relief=RAISED, command=ContrastCheck)
accessButton.grid(row=1, column=0)

main.mainloop()  # mainloop the main window
login_window.mainloop()
second_login_window.mainloop()
setting_window.mainloop()
booking_window.mainloop()
prescription_window.mainloop()
