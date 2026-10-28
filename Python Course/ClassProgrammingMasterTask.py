def printXs(string,count):
    li=[]
    gap=count-1
    if count==2:
        gap=count
    for i in range(count):
        for j in range(count):
            if i==j or j-i==gap:
                li.append(string)
            else:
                li.append("X")
        gap=gap-2
        for z in li:
            print(z,end="")
        print("\n",end="")
        li=[]

count=int(input("Enter the count\n"))
string=input("Enter letter\n")
printXs(string,count)