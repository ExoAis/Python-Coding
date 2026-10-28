from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Frames")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

frame=LabelFrame(root,text="My Frame",padx=5,pady=5)
frame.pack(padx=10,pady=10)
b=Button(frame,text="Nothing to do")
b.grid(row=0,column=0)

root.mainloop()

