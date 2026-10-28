from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("CheckBoxes")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

options=["Monday","Tuesday","Wednesday","Thursday","Friday"]
def show():
    mylbl=Label(root,text=click.get()).pack()
click=StringVar()
click.set(options[0])
drop=OptionMenu(root,click,*options).pack()
mybtn=Button(root,text="Show selection",command=show).pack()

mainloop()