
from tkinter import *
root=Tk()
Top = Frame(root, width=900, height=50, bd=2, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=2, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=2, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=2, relief="raise")
Buttons.pack(side=BOTTOM)
root.mainloop()