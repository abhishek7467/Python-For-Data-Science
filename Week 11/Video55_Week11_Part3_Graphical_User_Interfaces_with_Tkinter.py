
'''           Menu OutPut          '''

# Creating Menus

from cProfile import label
from errno import WSAETIMEDOUT
from tkinter import *

window = Tk()


def hello():
    print('Hello World!')

# create a top level menu in the main window


menubar = Menu(window)

# Create a pulldown menu and add it to the menu bar

filemenu = Menu(menubar)

filemenu.add_command(label='Open', command=hello)

filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.destroy)

filemenu.add_separator()

menubar.add_cascade(label='File', menu=filemenu)
window.config(menu=menubar)
window.mainloop()


'''         Radio Button         '''
from tkinter import *
window = Tk()


def sel():
    selection = "You are selected the option " + str(var.get())
    label.config(text=selection)


var = IntVar()

R1 = Radiobutton(window, text='Option 1', variable=var, value=1, command=sel)
R1.pack()  # Use the packer geometry manager

R2 = Radiobutton(window, text='Option 2', variable=var, value=2, command=sel)
R2.pack()

R3 = Radiobutton(window, text='Option 3', variable=var, value=3, command=sel)
R3.pack()

label = Label(window)
label.pack()

window.mainloop()




from tkinter import *
window = Tk()


def sel():
    selection = "You are  " + str(var.get())
    label.config(text=selection)


var = IntVar()

R1 = Radiobutton(window, text='Male', variable=var, value='male', command=sel)
R1.pack()  # Use the packer geometry manager

R2 = Radiobutton(window, text='Female', variable=var, value='female', command=sel)
R2.pack()

R3 = Radiobutton(window, text='Others', variable=var, value='others', command=sel)
R3.pack()

label = Label(window)
label.pack()

window.mainloop()















