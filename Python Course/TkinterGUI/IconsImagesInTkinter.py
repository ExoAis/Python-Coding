from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Using Images, Icons and Buttons")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

myImg=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/AnimeIcon.jpg"))
myLabel=Label(image=myImg)
myLabel.pack()

buttonQuit=Button(root,padx=70,pady=20,text="Exit Program",command=root.quit)
buttonQuit.pack
root.mainloop()
