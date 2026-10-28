from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Message Box")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")
root.geometry("300x300")

def slide():
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

vertical=Scale(root,from_=0,to=1000)
vertical.pack()
horizontal=Scale(root,from_=0,to=1000,orient=HORIZONTAL)
btn=Button(root,text="Click",command=slide).pack()
horizontal.pack()

mainloop()