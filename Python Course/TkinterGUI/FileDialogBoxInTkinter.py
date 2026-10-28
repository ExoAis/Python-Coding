from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root=Tk()
root.title("Message Box")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

def open():
    global img
    root.filename=filedialog.askopenfilename(initialdir="C:/",title="File Dialog Box",filetypes=(("Python Files","*.py"),("All Files","*.*")))
    mylabel=Label(root,text=root.filename).pack()
    img=ImageTk.PhotoImage(Image.open(root.filename))
    lbl=Label(root,image=img).pack()
   
btn=Button(root,text="Click to open dialog box",command=open).pack()

mainloop()