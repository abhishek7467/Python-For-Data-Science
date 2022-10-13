

from tkinter import *

from sqlalchemy import column

window = Tk()


# Adding a button widget
b1 = Button(window, text='xecute')

b1.grid(row=0, column=0)

window.mainloop()


# Entry amd Text Widgets

window = Tk()
b1 = Button(window, text="My Button")
b1.grid(row=0, column=1)
e1 = Entry(window)
e1.grid(row=1, column=2)
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)
window.mainloop()







# Convert kilometre into miles''''''''''''''''
from tkinter import *


window=Tk()
def km_to_miles():
    miles = float(e1_val.get())*1.6
    t1.delete("1.0",END)
    t1.insert(END, miles)
    print('Successfully Executed.........')

l1 = Label(window,text="Enter Kilometers  :  ")
l1.grid(row=0,column=0)
e1_val = StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)
l2 = Label(window,text="Kilometrs in Miles is : ")
l2.grid(row=1,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)
b1= Button(window,text="Convert",command=km_to_miles)
b1.grid(row=2,column=1)
window.mainloop()






