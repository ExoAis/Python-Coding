def isDecrypted(num):
    temp1,temp2,temp3,temp4=0,0,0,0
    size=len(num)
    if size<4 or size>4:
        print("You entered an invalid number.")
    else:
        temp1=num[2]
        temp2=num[3]
        temp3=num[0]
        temp4=num[1]
        temp1=int(temp1);temp2=int(temp2);temp3=int(temp3);temp4=int(temp4)
        temp1=((temp1+10)-7)%10
        temp2=((temp2+10)-7)%10
        temp3=((temp3+10)-7)%10
        temp4=((temp4+10)-7)%10
        temp1=str(temp1);temp2=str(temp2);temp3=str(temp3);temp4=str(temp4)
        num=""
        num=(temp1)+(temp2)+(temp3)+temp4
        return num

num=(input("Enter an encrypted number to decrypt without space before and after\n"))
print("Decrypted number is",isDecrypted(num))
