from tkinter import *
root=Tk()
e=Entry(root,fg="#FFFFFF",bg="#000000")
e.pack()
e.insert(0,"Enter your name")
def numFunc():
    myLabel=Label(root,text="I love you Master "+e.get())
    myLabel.pack()
myButton=Button(root,text="Press for suprise UWU", state="active",padx=2,pady=2,command=numFunc,fg="#FFFFFF",bg="#000000")
myButton.pack()
root.mainloop()