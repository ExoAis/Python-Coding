from tkinter import *
root=Tk()
def numFunc():
    myLabel=Label(root,text="9")
    myLabel.pack()
myButton=Button(root,text="5+4=", state="disable",padx=2,pady=2,command=numFunc,fg="red",bg="#000000")
myButton.pack()
root.mainloop()