from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Radio")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

#var=IntVar()
#var.set("1")
FLAVOURS=[
    ("Malai","Malai"),
    ("Supreme","Supreme"),
    ("Cheesy","Cheesy"),
    ("Arabic","Arabic")
]
pizza=StringVar()
pizza.set("Malai")
def clicked(value):
    myLabel=Label(root,text=value)
    myLabel.pack()
for text,FLAVOUR in FLAVOURS:
    Radiobutton(root,text=text,variable=pizza,value=FLAVOUR,command=lambda:clicked(pizza.get())).pack(anchor=W)
#for i in range(10):
#Radiobutton(root,text="Option 1",variable=var,value=1,command=lambda:clicked(var.get())).pack() 
#Radiobutton(root,text="Option 2",variable=var,value=2,command=lambda:clicked(var.get())).pack() 
myLabel=Label(root,text=pizza.get()).pack()
#myButton=Button(root,text="Click me",command=lambda:clicked(pizza.get()))
#myButton.pack()

root.mainloop()

