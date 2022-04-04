from tkinter import *  # imports
import pandas as pd
from win10toast import ToastNotifier
import time
import string
import random

CREAM = "mint cream"  # setting constant variables(background and foreground)
BLUE = "Cyan4"
YELLOW = "Yellow2"
BLACK = "Black"

notifier = ToastNotifier()

dataframe = pd.read_csv("MOCK_DATA.csv")

login_window = Tk()  # creating main window
login_window.geometry("1100x600")  # setting the windows size, resizable, title and starting background
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
main.geometry("1100x600")  # setting the windows size, resizable, title and starting background
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

login1_window = Toplevel()  # creating main window
login1_window.geometry("1100x600")  # setting the windows size, resizable, title and starting background
login1_window.resizable(False, False)
login1_window.title("Healthcare Application - Login")
login1_window.config(bg=BLUE)
login1_window.withdraw()

login1_background_frame = Frame(login1_window, height=560, width=400, bg=CREAM)
login1_background_frame.pack(pady=20)
login1_logo_frame = Frame(login1_background_frame, width=400, bg=CREAM)
login1_logo_frame.pack(pady=10)
login1_details_Frame = Frame(login1_background_frame, width=400, bg=CREAM)
login1_details_Frame.pack()

checkInt = IntVar()  # creating the check button's integer variable to live update the value
checkInt.set(0)  # setting the IntVar to 0 by default

contrastMode = StringVar()  # creating a StringVar for the button text
contrastMode.set("High Contrast mode [off]")

header_frame = Frame(main, bg=BLUE)
header_frame.grid(row=0)


def on_enter_email(e):
    email_entry.delete(0, "end")


def on_leave_email(e):
    username = email_entry.get()
    if username == "":
        email_entry.insert(0, "Email")


def on_enter_password(e):
    password_entry.delete(0, "end")


def on_leave_password(e):
    password = password_entry.get()
    if password == "":
        password_entry.insert(0, "Password")


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
    login1_window.deiconify()
    login_window.withdraw()


# Login Page
login_logo = PhotoImage(file="App Logo.png")
login_logo_label = Label(login_logo_frame, image=login_logo)
login_logo_label.pack(padx=125, pady=20)

login1_logo = PhotoImage(file="App Logo.png")
login1_logo_label = Label(login1_logo_frame, image=login1_logo)
login1_logo_label.pack(padx=125, pady=20)

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

# Main Window
booking_header_btn = Button(header_frame, bg=CREAM, text="Booking", height=2, width=20)
booking_header_btn.grid(row=0, column=0, padx=45, pady=10)
medication_header_btn = Button(header_frame, bg=CREAM, text="Medication", height=2, width=20)
medication_header_btn.grid(row=0, column=1, padx=45, pady=10)

prescriptions_header_btn = Button(header_frame, bg=CREAM, text="prescriptions", height=2, width=20)
prescriptions_header_btn.grid(row=0, column=2, padx=45, pady=10)

after_app_chat = Button(header_frame, bg=CREAM, text="After Appointment Chat", height=2, width=20)
after_app_chat.grid(row=0, column=3, padx=45, pady=10)

setting_btn = Button(header_frame, bg=CREAM, text=u"\u2699", height=1, width=3, font=('Helvatical bold', 15),
                     command=setting_btn_on)
setting_btn.grid(row=0, column=4, padx=45, pady=10)

# first time login page

email_entry = Entry(login1_details_Frame, fg="Black", bg="White", font=("Microsoft YaHei UI Light", 11), bd=0)
email_entry.grid(row=0, column=0, pady=(100, 0))
email_entry.insert(0, "Email")

email_entry.bind("<FocusIn>", on_enter_email)
email_entry.bind("<FocusOut>", on_leave_email)

password_entry = Entry(login1_details_Frame, fg="Black", bg="White", font=("Microsoft YaHei UI Light", 11), bd=0)
password_entry.grid(row=0, column=1, pady=(100, 0))
password_entry.insert(0, "Password")

password_entry.bind("<FocusIn>", on_enter_password)
password_entry.bind("<FocusOut>", on_leave_password)


def login_confirm():
    if email_entry.get() in dataframe["email"] and password_entry.get() in dataframe["password"]:
        print("access granted")


login1_confirm = Button(login1_details_Frame, text="Confirm", command=login_confirm)
login1_confirm.grid(row=1, column=0, columnspan=2, pady=(10, 300))

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


def HighContrast():  # creating a block to change the background to black and the foreground to yellow
    windows = [main, header_frame]
    for window in windows:
        window.config(bg=BLACK)
        setting_window.config(bg=BLACK)

    widgets = [accessButton, booking_header_btn,
               medication_header_btn, prescriptions_header_btn,
               after_app_chat, setting_btn, settings_back_btn,
               firstname, lastname, address, postcode, healthnumber,
               login_enter, login_option]
    for widget in widgets:
        widget.configure(bg="Yellow")


def LowContrast():  # creating a block to change the background to blue and the foreground to cream
    windows = [main, header_frame, login1_window, login_frame, login_window,
               login_logo_frame, login_details_Frame]
    for window in windows:
        window.config(bg=BLUE)
        setting_window.config(bg=BLUE)

    widgets = [accessButton, booking_header_btn,
               medication_header_btn, prescriptions_header_btn,
               after_app_chat, setting_btn, settings_back_btn]
    for widget in widgets:
        widget.configure(bg=CREAM)


accessButton = Button(main,  # generic test button
                      textvariable=contrastMode,
                      bg=CREAM, relief=RAISED, command=ContrastCheck)
accessButton.grid(row=1, column=0)

main.mainloop()  # mainloop the main window
login_window.mainloop()
setting_window.mainloop()
