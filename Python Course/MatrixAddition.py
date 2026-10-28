import random
def nMatrix(n,m):
    if n!=m:
        return "Enter same values for n and m"
    matrix=[]
    for i in range(m):
        l=[]
        for j in range(n):
            l.append(random.randint(10,49))
        matrix.append(l)
    return matrix
def addMatrix():
    l3=nMatrix(n,m)
    for i in range(m):
        for j in range(n):
            l3[i][j]=l1[i][j]+l2[i][j]
    return l3
def printMatrices():
    space=2*n+1
    for i in range(n):
      if i!=n//2:
          for j in range(m):
              print(l1[i][j]," ",end="")
          for j in range(space):
              print(end=" ")
          for j in range(m):
              print(l2[i][j]," ",end="")
          for j in range(space):
              print(end=" ")
          for j in range(m):
              print(resMatrix[i][j]," ",end="")
      else:
        for j in range(m):
            print(l1[i][j]," ",end="")
        for j in range(space):
            if j==(space//2)-1:
                print("+",end="")
            else:
                print(end=" ")
        for j in range(m):
            print(l2[i][j]," ",end="")
        for j in range(space):
            if j==(space//2)-1:
                print("=",end="")
            else:
                print(end=" ")
        for j in range(m):
            print(resMatrix[i][j]," ",end="")
      print("\n",end="")
    
n,m=input("Enter n and m values for a 2D n by m matrix\n").split()
n=int(n);m=int(m)
l1=nMatrix(n,m)
l2=nMatrix(n,m)
resMatrix=addMatrix()
print("\n")
printMatrices()





            