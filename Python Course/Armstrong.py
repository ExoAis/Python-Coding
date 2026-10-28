def isArmstrong(num):
    sum,r=0,0
    temp=num
    while num>0:
        r=num%10
        num=num//10
        sum+=r**3
    num=temp
    if sum==num:
        return True
    else:
        return False
num=int(input("Enter the number"))
if isArmstrong(num)==True:
    print("Given number is armstrong number.")
else:
    print("Given number isn't armstrong.")

