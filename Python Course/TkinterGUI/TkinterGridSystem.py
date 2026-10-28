from tkinter import *
root=Tk()
col=4
for i in range(5):
    myLabel1=Label(root,text="Sadeed").grid(row=i,column=i)
    if i!=(5//2) and col>=0:
        myLabel1=Label(root,text="Sadeed").grid(row=i,column=col)
    elif i==(5//2):
        col-=1
        continue;
    col-=1
root.mainloop()

0,4 
1,3
2,2
3,1
4,0
