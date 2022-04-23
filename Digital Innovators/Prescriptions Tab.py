from tkinter import *
import pandas as pd

email_entry = "ollierhodes@gmail.com"
def prescription_tab():
    prescription_window = Tk()
    prescription_window.geometry("1100x600")
    prescription_window.resizable(False, False)
    prescription_window.title("Healthcare Application - Prescriptions")

    BLUE = "cyan4"
    prescription_window.config(bg=BLUE)
    prescription_dataframe = pd.read_csv("MOCK_DATA.csv")

    listbox = Listbox(prescription_window, width=100, height=46, bg="white")
    listbox.place(x=50, y=155, width=500, height=400)

    searching = prescription_dataframe.loc[prescription_dataframe["email"] == email_entry]
    index = searching.index

    First = prescription_dataframe["first_name"]
    first_name = First[index].item()

    Surname = prescription_dataframe["last_name"]
    sur_name = Surname[index].item()

    name = "Showing medication for " + first_name + " " + sur_name
    nameLabel = Label(prescription_window, bg='cyan4', fg='white', font=("Verdana", 17))
    nameLabel.place(x=50, y=50)
    nameLabel.config(text=name)

    Medication = prescription_dataframe["med1"]
    for item in Medication[index]:
        listbox.insert("end", item)

    prescription_window.mainloop()

prescription_tab()
