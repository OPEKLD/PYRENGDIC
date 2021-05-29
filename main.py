from tkinter import *

words = {}
order = 0  # Default order 0 is eng-pyr, 1 is pyr-eng
container = "empty"


def switchOrder():
    engWordList.delete(0, END)
    pyrWordList.delete(0, END)

    for key, value in words.items():
        container = key
        key = value
        value = container

    global order

    if order == 0:

        for key, value in sorted(words.items()):
            engWordList.insert(END, value)
            pyrWordList.insert(END, key)

        labelEng.config(text="Pyrainian")
        labelPyr.config(text="English")

        buttonSwitch.config(text="Eng-Pyr")

        order = 1

    elif order == 1:
        for key, value in sorted(words.items()):
            engWordList.insert(END, key)
            pyrWordList.insert(END, value)

        labelEng.config(text="English")
        labelPyr.config(text="Pyrainian")

        buttonSwitch.config(text="Pyr-Eng")

        order = 0


def submitDefinition(defeng, defpyr):
    engWordList.delete(0, END)
    pyrWordList.delete(0, END)

    newKey = defeng
    newValue = defpyr

    words.update({newKey: newValue})

    for key, value in sorted(words.items()):
        if order == 0:
            engWordList.insert(END, key)
            pyrWordList.insert(END, value)

        elif order == 1:
            engWordList.insert(END, value)
            pyrWordList.insert(END, key)


def remove_word():
    selected = engWordList.get(engWordList.curselection())

    words.pop(selected, None)

    engWordList.delete(0, END)
    pyrWordList.delete(0, END)

    for key, value in sorted(words.items()):
        engWordList.insert(END, key)
        pyrWordList.insert(END, value)


def add_word_window():

    # Create new window

    new_window = Toplevel()
    new_window.geometry("600x180")
    new_window.title("Add word")
    new_window.config(background="#a5e8bc")

    # Generate Labels

    newLabelEng = Label(new_window, text="English",
                        font=('Meiryo bold', 10),
                        bg='#8bc9a0',
                        fg='#5d1b69',
                        bd=3,
                        relief="groove",
                        padx=5,
                        pady=3)

    newLabelPyr = Label(new_window, text="Pyrainian",
                        font=('Meiryo bold', 10),
                        bg='#8bc9a0',
                        fg='#5d1b69',
                        bd=3,
                        relief="groove",
                        padx=5,
                        pady=3)

    # Place labels

    newLabelEng.place(x=95, y=18)
    newLabelPyr.place(x=390, y=18)

    # Define user input spot

    entryEng = Entry(new_window, font=("Meiryo", 10))
    entryPyr = Entry(new_window, font=("Meiryo", 10))

    # Place user input areas

    entryEng.place(x=50, y=70)
    entryPyr.place(x=350, y=70)

    # Define Buttons

    buttonSubmit = Button(new_window,
                          text='Submit',
                          command=lambda: submitDefinition(entryEng.get(), entryPyr.get()),
                          font=('Meiryo bold', 10),
                          fg='#c4214d',
                          bg='#c5fad7',
                          bd=5,
                          relief='ridge',
                          padx=3,
                          pady=2)

    # Place Buttons

    buttonSubmit.place(x=250, y=100)


# Creates window
window = Tk()  # Create a window
window.geometry("1280x720")
window.title("Official Pyrainian Dictionary")

# Sets window icon
icon = PhotoImage(file='PyrainianFlag.png')
window.iconphoto(True, icon)

# Sets window background
window.config(background="#a5e8bc")

# Generate labels

labelEng = Label(window, text="English",
                 font=('Meiryo bold', 15),
                 bg='#8bc9a0',
                 fg='#5d1b69',
                 bd=10,
                 relief="groove",
                 padx=5,
                 pady=3)

labelPyr = Label(window, text="Pyrainian",
                 font=('Meiryo bold', 15),
                 bg='#8bc9a0',
                 fg='#5d1b69',
                 bd=10,
                 relief="groove",
                 padx=5,
                 pady=3)

# Place labels

labelEng.place(x=50, y=100)
labelPyr.place(x=650, y=100)

# Generate listboxes

engWordList = Listbox(window,
                      font=('Meiryo', 8),
                      fg='#c4214d',
                      bg='#c5fad7',
                      bd=10,
                      relief="groove",
                      width=50,
                      height=25,
                      justify=CENTER)

pyrWordList = Listbox(window,
                      font=('Meiryo', 8),
                      fg='#c4214d',
                      bg='#c5fad7',
                      bd=10,
                      relief="groove",
                      width=50,
                      height=25,
                      justify=CENTER)

# Place List Boxes

engWordList.place(x=50, y=200)
pyrWordList.place(x=650, y=200)

# Generate Buttons

buttonAddWord = Button(window,
                       text='Add Word',
                       command=add_word_window,
                       font=('Meiryo bold', 10),
                       fg='#c4214d',
                       bg='#c5fad7',
                       bd=5,
                       relief='ridge',
                       padx=3,
                       pady=2)

buttonRemoveWord = Button(window,
                          text='Delete',
                          command=remove_word,
                          font=('Meiryo bold', 10),
                          fg='#c4214d',
                          bg='#c5fad7',
                          bd=5,
                          relief='ridge',
                          padx=3,
                          pady=2)

buttonSwitch = Button(window,
                      text='Pyr-Eng',
                      command=switchOrder,
                      font=('Meiryo bold', 10),
                      fg='#c4214d',
                      bg='#c5fad7',
                      bd=5,
                      relief='ridge',
                      padx=3,
                      pady=2)

# Place buttons

buttonAddWord.place(x=0, y=0)
buttonRemoveWord.place(x=95, y=0)
buttonSwitch.place(x=165, y=0)

# Generate Scroll bar

scrollBar = Scrollbar(window)
scrollBar.pack(side=RIGHT, fill=BOTH)


window.mainloop()  # Place window on computer screen
