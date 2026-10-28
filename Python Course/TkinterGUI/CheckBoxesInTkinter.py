from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("CheckBoxes")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

var=StringVar()
chk=Checkbutton(root,text="Check this",variable=var,onvalue="On",offvalue="Off")
chk.deselect()
chk.pack()
def update():
    lab=Label(root,text=var.get()).pack()
btn=Button(root,text="Selection",command=update).pack()

mainloop()