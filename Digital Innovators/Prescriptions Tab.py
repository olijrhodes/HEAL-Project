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

#for index, row in dataframe.iterrows():
    #print(index, row["med1"])

#first_name = dataframe.loc("first_name")

#meds = StringVar
#meds = dataframe.loc[dataframe["med1"].str.contains(first_name, flags=re.I, regex=True)]
#print(meds.to_string)

firstname = "Daryle"
surname = "Playle"

name = "Showing medication for " + firstname + " " + surname
nameLabel = Label(window, bg='cyan4', fg='white', font=("Verdana", 17))
nameLabel.place(x=50,y=50)
nameLabel.config(text=name)

searching = dataframe.loc[dataframe["first_name"] + dataframe["last_name"] == firstname + surname]  # change firstname surname .get()
index = searching.index

Medication = dataframe["med1"] #seperate medication from each other and find out how to specify items in csv are lists

for med in Medication[index].item():
    if len(med) >= 1:
        listbox.insert("end", med)
    else:
        listbox.insert("end", med)


window.mainloop()