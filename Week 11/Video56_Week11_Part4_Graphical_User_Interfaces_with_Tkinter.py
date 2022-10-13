'''          Adding Checkboxes'''


from operator import ipow
from tkinter import *

# Checkbutton example 

def sel():
    if  (CheckVar1.get()==1):
        selection = 'You  selected Python Programming option'

    else:
        selection="You de-selected the Python Programming option"

    label.config(text=selection)

def sel2():
    if (CheckVar2.get()==1):
        selection='You selected tkinter option'
    else:
        selection="You de-selected the tkinter option"
    
    label.config(text=selection)


window=Tk()

CheckVar1 = IntVar()
CheckVar2= IntVar()

C1= Checkbutton(window,text='Python Programming ', variable=CheckVar1,onvalue=1,offvalue=0, height=5,width=20,command=sel)

C2=Checkbutton(window,text='Tkinter',variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20,command=sel2 )

C1.pack()
C2.pack()

label=Label(window)
label.pack()

window.mainloop()




'''                             List  boxes                     '''


from tkinter import * 

window = Tk()

def my_upd():
    print(l1.get(ACTIVE))# Get the ACtive  / selected element
l1= Listbox(window,height=4)
l1.grid(row=1,column=1)

my_list = ['tkinter','Python ','Numpy','Abhishek','Kumar']

for element in my_list:
    l1.insert(END,element)

b1=Button(window,text='Show',width=10,bg='yellow',command=my_upd)
b1.grid(row=1,column=2)
window.mainloop()





from tkinter import * 

window = Tk()

def my_upd():
    print(l1.get(ACTIVE))# Get the ACtive  / selected element
l1= Listbox(window,height=4)
l1.pack()

my_list = ['tkinter','Python ','Numpy','Abhishek','Kumar']

for element in my_list:
    l1.insert(END,element)

b1=Button(window,text='Show',width=10,bg='yellow',command=my_upd)
b1.pack()
window.mainloop()











