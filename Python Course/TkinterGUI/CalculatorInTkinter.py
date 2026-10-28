from tkinter import *
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def buttonClick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def buttonClear():
    e.delete(0,END)
def buttonAdd():
    global toDO
    toDO="Add"
    global firstNum
    firstNum=e.get()
    firstNum=eval(firstNum)
    e.delete(0,END)
def buttonEquals():
    secondNum=e.get()
    e.delete(0,END)
    if toDO=="Add":
        e.insert(0,firstNum+eval(secondNum))
    elif toDO=="Subtract":
        e.insert(0,firstNum-eval(secondNum))
    elif toDO=="Multiply":
        e.insert(0,firstNum*eval(secondNum))
    elif toDO=="Divide":
        e.insert(0,firstNum/eval(secondNum))
def buttonSubtract():
    global toDO
    toDO="Subtract"
    global firstNum
    firstNum=e.get()
    firstNum=eval(firstNum)
    e.delete(0,END)
def buttonMultiply():
    global toDO
    toDO="Multiply"
    global firstNum
    firstNum=e.get()
    firstNum=eval(firstNum)
    e.delete(0,END)
def buttonDivide(): 
    global toDO
    toDO="Divide"
    global firstNum
    firstNum=e.get()
    firstNum=eval(firstNum)
    e.delete(0,END)

Button1=Button(root,text="1",padx=40,pady=20,command=lambda:buttonClick(1))
Button2=Button(root,text="2",padx=40,pady=20,command=lambda:buttonClick(2))
Button3=Button(root,text="3",padx=40,pady=20,command=lambda:buttonClick(3))
Button4=Button(root,text="4",padx=40,pady=20,command=lambda:buttonClick(4))
Button5=Button(root,text="5",padx=40,pady=20,command=lambda:buttonClick(5))
Button6=Button(root,text="6",padx=40,pady=20,command=lambda:buttonClick(6))
Button7=Button(root,text="7",padx=40,pady=20,command=lambda:buttonClick(7))
Button8=Button(root,text="8",padx=40,pady=20,command=lambda:buttonClick(8))
Button9=Button(root,text="9",padx=40,pady=20,command=lambda:buttonClick(9))
Button0=Button(root,text="0",padx=40,pady=20,command=lambda:buttonClick(0))
ButtonAdd=Button(root,text="+",padx=39,pady=20,command=buttonAdd)
ButtonEquals=Button(root,text="=",padx=90,pady=20,command=buttonEquals)
ButtonClear=Button(root,text="Clear",padx=79,pady=20,command=buttonClear)
ButtonSubtract=Button(root,text="-",padx=41,pady=20,command=buttonSubtract)
ButtonMultiply=Button(root,text="*",padx=40,pady=20,command=buttonMultiply)
ButtonDivide=Button(root,text="/",padx=42,pady=20,command=buttonDivide)

Button1.grid(row=3,column=0)
Button2.grid(row=3,column=1)
Button3.grid(row=3,column=2)

Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)

Button7.grid(row=1,column=0)
Button8.grid(row=1,column=1)
Button9.grid(row=1,column=2)

Button0.grid(row=4,column=0)

ButtonAdd.grid(row=5,column=0)
ButtonSubtract.grid(row=6,column=0)
ButtonMultiply.grid(row=6,column=1)
ButtonDivide.grid(row=6,column=2)
ButtonEquals.grid(row=5,column=1,columnspan=2)
ButtonClear.grid(row=4,column=1,columnspan=2)

root.mainloop()