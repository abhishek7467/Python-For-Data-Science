
# Question 1
'''

Create a simple tkinter application to display a 
welcome message in a window using the label widget.

'''

import string
from tkinter import *
from turtle import bgcolor

from click import command
window=Tk()
l1=Label(window,text= "Welcome to the Python GUI...")
l1.grid(row=0,column=0)
window.mainloop()




# Question 2

'''
Create tkinter application to accept user name in a text widget. 
Then display the user name with a welcome message in a label widget


'''

from tkinter import * 
window=Tk()

def WelcomeMessege():
    welmsg=str(val.get())
    t1.delete("1.0",END)
    t1.insert(END,"Welcome "+welmsg)
    print('Successfully Executed...')

l1=Label(window,text="Enter your name   :  ")
l1.grid(row=0,column=0)
val = StringVar()
v1=Entry(window,textvariable=val) 
v1.grid(row=0,column=1)
l2 = Label(window,text="")
l2.grid(row=1,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)
b1=Button(window,text='Print',command=WelcomeMessege)
b1.grid(row=2,column=1)
window.mainloop()








# Question 3


'''

Modify the tkinter application developed in Q.No. 2 
so that it uses a grid layout
 

'''


from tkinter import * 
from tkinter.ttk import *

window=Tk()

def WelcomeMessege():
    welmsg=str(val.get())
    t1.delete("1.0",END)
    t1.insert(END,"Welcome "+welmsg)
    print('Successfully Executed...')

l1=Label(window,text="Enter your name   :  ")
l1.grid(row=0,column=0,sticky=W,pady=2)
val = StringVar()
v1=Entry(window,textvariable=val) 
v1.grid(row=0,column=1,pady=2)
l2 = Label(window,text="")
l2.grid(row=1,column=0,sticky=W,pady=2)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1,pady=2)
b1=Button(window,text='Print',command=WelcomeMessege)
b1.grid(row=2,column=1,pady=2)
window.mainloop()




# Question 4 

'''

Create a tkinter application 
to accept radius of a circle and display the area.

'''

from tkinter import * 
from tkinter.ttk import *
import math

window=Tk()

def area():
    r=float(val.get())
    areaOfCircle=math.pi*r*r
    t1.delete("1.0",END)
    t1.insert(END,areaOfCircle)
    print('Successfully Executed...')

l1=Label(window,text="Enter Radius of a circle  ")
l1.grid(row=0,column=0,sticky=W,pady=2)
val = StringVar()
v1=Entry(window,textvariable=val) 
v1.grid(row=0,column=1,pady=2)
l2 = Label(window,text="Area of the Circle ")
l2.grid(row=1,column=0,sticky=W,pady=2)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1,pady=2)
b1=Button(window,text='Calculate',command=area)
b1.grid(row=2,column=1,pady=2)
window.mainloop()







# Question 5 

'''

Create a tkinter application to accept temperature in Celsius 
and convert and display the temperature in Fahrenheit.

'''


from tkinter import * 
from tkinter.ttk import *
import math

window=Tk()

def Tempreture():
    celsius=float(val.get())
    fahrenheit= ((celsius*9)/5)+32  
    t1.delete("1.0",END)
    t1.insert(END,fahrenheit)
    print('Successfully Executed...')

l1=Label(window,text="Enter Temperature in Celsius  ")
l1.grid(row=0,column=0,sticky=W,pady=2)
val = StringVar()
v1=Entry(window,textvariable=val) 
v1.grid(row=0,column=1,pady=2)
l2 = Label(window,text="Temperature in Fahrenheit ")
l2.grid(row=1,column=0,sticky=W,pady=2)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1,pady=2)
b1=Button(window,text='Calculate',command=Tempreture)
b1.grid(row=2,column=1,pady=2)
window.mainloop()





# Question  6 

'''

Create a tkinter application to accept distance in kilometers
 and convert and display distance in miles.


'''
from tkinter import *


window=Tk()
def km_to_miles():
    miles = float(e1_val.get())*0.62137
    t1.delete("1.0",END)
    t1.insert(END, miles)
    print('Successfully Executed.........')

l1 = Label(window,text="Enter Kilometers  :  ")
l1.grid(row=0,column=0, sticky=W, pady=3)
e1_val = StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1,pady=3)
l2 = Label(window,text="Kilometrs in Miles is : ")
l2.grid(row=1,column=0,sticky=W, pady=3)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1,pady=3)
b1= Button(window,text="Convert",command=km_to_miles)
b1.grid(row=2,column=1, pady=3)
window.mainloop()






# Question  7

'''

Create a tkinter application to display a menu with three items.
 A separate message should be display when each of the three menu 
 items is clicked.
 

'''

from tkinter import *
window = Tk()
def hello():
    selection = "Hello World!" 
    label.config(text=selection,bg="#20F200")
    
def country():
    selection = "This is India." 
    label.config(text=selection,bg="#20F200")
    

def about():
    selection = "Hii, I am Abhishek Kumar." 
    label.config(text=selection,bg="#20F200")
    
menubar = Menu(window)
filemenu = Menu(menubar)
filemenu.add_command(label='Open', command=hello)
filemenu.add_separator()
filemenu.add_command(label='Country', command=country)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.destroy)
filemenu.add_separator()
filemenu.add_command(label='About', command=about)
filemenu.add_separator()
menubar.add_cascade(label='File', menu=filemenu)
window.config(menu=menubar)
label = Label(window)
label.pack()
window.mainloop()





# Question 8
'''

Create a tkinter application to display a radio button group with 
three items. A separate message should be 
display when each of the three radio buttons items is clicked.

'''
from tkinter import *
window = Tk()

def sel():
    selection = "You are selected the option " + str(var.get())
    label.config(text=selection,bg="#20F200")
var = IntVar()
R1 = Radiobutton(window, text='Option 1', variable=var, value=1, command=sel,bg="#7022BF")
R1.pack()  
R2 = Radiobutton(window, text='Option 2', variable=var, value=2, command=sel,bg="#EE434F")
R2.pack()
R3 = Radiobutton(window, text='Option 3', variable=var, value=3, command=sel,bg="#BFAF22")
R3.pack()
label = Label(window)
label.pack()
window.mainloop()






# Question 9

'''
Create a tkinter application to display three check boxes.
 A separate message should be display
 when each of the three check boxes items is selected.

'''

from tkinter import *
def sel():
    if  (CheckVar1.get()==1):
        selection = 'You  selected Python Programming option'

    else:
        selection="You de-selected the Python Programming option"

    label.config(text=selection,bg='#FF6782')
def sel2():
    if (CheckVar2.get()==1):
        selection='You selected tkinter option'
    else:
        selection="You de-selected the tkinter option"
    
    label.config(text=selection,bg='#FF6782')
window=Tk()
CheckVar1 = IntVar()
CheckVar2= IntVar()

C1= Checkbutton(window,text='Python Programming ', variable=CheckVar1,onvalue=1,offvalue=0, height=5,width=20,command=sel,bg='#B946C6')
C2=Checkbutton(window,text='Tkinter',variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20,command=sel2,bg='#FF3508' )
C1.pack()
C2.pack()
label=Label(window,)
label.pack()
window.mainloop()





# Question 10

'''

Create a tkinter application which contains a 
list box with five items. Whenever an item in the list box is selected,
 the item’s text should be displayed

'''


from tkinter import * 

window = Tk()

def my_Language():
    print(l1.get(ACTIVE))
l1= Listbox(window,height=5, bg='green')
l1.grid(row=1,column=1,sticky=W,pady=5 )
my_list = ['C','C++','Python ','HTML','JavaScript']
for lang in my_list:
    l1.insert(END,lang)
b1=Button(window,text='Show',width=10,bg='yellow',command=my_Language)
b1.grid(row=1,column=2,pady=5)
window.mainloop()

































