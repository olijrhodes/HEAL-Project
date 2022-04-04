import pandas as pd
from tkinter import *

window = Tk()
window.geometry("1100x600")
window.resizable(False,False)
window.title("Healthcare Application - Prescriptions")

BLUE = "cyan4"
window.config(bg=BLUE)

dataframe = pd.read_csv("MOCK_DATA.csv", on_bad_lines='skip')
print(dataframe)
var1 = StringVar()

listbox = Listbox(window, width= 100, height=46, bg="white")
listbox.place(x=50,y=155,width=500,height=400)

firstname = "Daryle"
sirname = "Playle"

name = "Showing medication for " + firstname + " " + sirname
nameLabel = Label(window, bg='cyan4', fg='white', font=("Verdana", 17))
nameLabel.place(x=50,y=50)
nameLabel.config(text=name)
scrollbar = Scrollbar

def search():
    pass
    #specific_person = dataframe.loc[dataframe["first_name"] + dataframe["last_name"] == firstname.get()= lastname.get()]
    #id = specific_person.index
    #print(id)
    #print(specific_person)

def clickevent(self):
    val = listbox.get(listbox.curselection)
    meds = dataframe.loc[dataframe["med1"] == val] #finds the data on the row
    print(val)

listbox.bind('<<ListboxSelect>>', clickevent)

window.mainloop()