
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

