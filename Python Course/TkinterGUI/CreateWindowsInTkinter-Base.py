from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Message Box")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

def open():
    global img
    top=Toplevel()
    img=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/Ecchi4.png"))
    lbl=Label(top,image=img).pack()
    btn1=Button(top,text="Close this image",command=top.destroy).pack()
btn=Button(root,text="Open new window",command=open).pack()

mainloop()