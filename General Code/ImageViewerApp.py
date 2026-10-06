from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Using Images, Icons and Buttons")
root.iconbitmap("D:/IconsForTkinter/AnimeIcon.ico")

myImg=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/AnimeIcon.jpg"))
myImg1=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/Ecchi1.png"))
myImg2=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/Ecchi2.png"))
myImg3=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/Ecchi3.png"))
myImg4=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/Ecchi4.png"))
myImg5=ImageTk.PhotoImage(Image.open("D:/IconsForTkinter/Ecchi5.png"))
imageList=[myImg,myImg1,myImg2,myImg3,myImg4,myImg5]

status=Label(root,text="Image 1 out of "+str(len(imageList)),bd=1,relief=SUNKEN) #Use anchor=E/W/N/S to shift status text to left or right

myLabel=Label(image=myImg)
myLabel.grid(row=0,column=0,columnspan=3)

def forward(imageNumber):
    global myLabel
    global buttonForward
    global buttonBackward
    myLabel.grid_forget()
    myLabel=Label(image=imageList[imageNumber])
    buttonBack=Button(root,text="Previous",command=lambda:back(imageNumber-1))
    status=Label(root,text="Image "+str(imageNumber+1)+ " out of "+str(len(imageList)),bd=1,relief=SUNKEN)
    if imageNumber==5:
        buttonNext=Button(root,text="Next",state=DISABLED)
    else:
        buttonNext=Button(root,text="Next",command=lambda:forward(imageNumber+1))
    myLabel.grid(row=0,column=0,columnspan=3)
    buttonBack.grid(row=1,column=0)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    buttonNext.grid(row=1,column=2)
def back(imageNumber):
    global myLabel
    global buttonForward
    global buttonBackward
    myLabel.grid_forget()
    myLabel=Label(image=imageList[imageNumber])
    status=Label(root,text="Image "+str(imageNumber+1)+ " out of "+str(len(imageList)),bd=1,relief=SUNKEN)
    if imageNumber==0:
        buttonNext=Button(root,text="Next",command=lambda:forward(imageNumber+1))
        buttonBack=Button(root,text="Previous",state=DISABLED)
    else:
        buttonNext=Button(root,text="Next",command=lambda:forward(imageNumber+1))
        buttonBack=Button(root,text="Previous",command=lambda:back(imageNumber-1))
    myLabel.grid(row=0,column=0,columnspan=3)
    buttonBack.grid(row=1,column=0)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    buttonNext.grid(row=1,column=2)

buttonBack=Button(root,text="Previous",state=DISABLED,command=lambda:back(0))
buttonQuit=Button(root,text="Exit Program",command=root.quit)
buttonNext=Button(root,text="Next",command=lambda:forward(1))

buttonBack.grid(row=1,column=0)
buttonQuit.grid(row=1,column=1,pady=10)
buttonNext.grid(row=1,column=2)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
