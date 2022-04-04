checkInt = IntVar()  # creating the check button's integer variable to live update the value
checkInt.set(0)  # setting the IntVar to 0 by default

contrastMode = StringVar()  # creating a StringVar for the button text
contrastMode.set("High Contrast mode [off]")


def ContrastCheck():  # checking whether to change the accessibility options
    if checkInt.get() == 0:
        HighContrast()
        checkInt.set(1)
        contrastMode.set("High Contrast mode [on]")  # changing the button text to show the accessibility status
    elif checkInt.get() == 1:
        LowContrast()
        checkInt.set(0)
        contrastMode.set("High Contrast mode [off]")


def HighContrast():  # creating a block to change the background to black and the foreground to yellow
    main.config(bg=BLACK)
    widgets = [accessButton]
    for widget in widgets:
        widget.configure(bg="Yellow")


def LowContrast():  # creating a block to change the background to blue and the foreground to cream
    main.config(bg=BLUE)
    widgets = [accessButton]
    for widget in widgets:
        widget.configure(bg=CREAM)


accessButton = Button(main,  # generic test button
                      textvariable=contrastMode,
                      bg=CREAM, relief=RAISED, command=ContrastCheck)
accessButton.place(x=930, y=2)