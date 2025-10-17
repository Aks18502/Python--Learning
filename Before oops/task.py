a=int(input("enter the no of values :"))
li=[]
for a in range(1,a+1):
    
        
    if(a==1):
        b=int(input(" enter ur "+ str(a) +"st num :"))
        li.append(b)
        if(a>=4 and a<=20):
            b=int(input("enter ur "+ str(a) +"th num :"))
            li.append(b)
    elif(a==2):
        b=int(input("enter ur "+ str(a) +"nd num :"))
        li.append(b)
        if(a>=4 and a<=20):
            b=int(input("enter ur "+ str(a) +"th num :"))
            li.append(b)
    elif(a==3):
        b=int(input("enter ur "+ str(a) +"rd num :"))
        li.append(b)
        if(a>=4 and a<=20):
            b=int(input("enter ur "+ str(a) +"th num :"))
            li.append(b)
    else:
        b=int(input("enter ur "+ str(a) +"th num :"))
        li.append(b)

print(li)
i=0
j=0
x=0
for x in li:
    if (x%2==0):
        print(x,"is even no")
        i+=x
for x in li:
    if(x%2!=0):
        print(x,"is odd no")
        j+=x
print("total of even no :",i)
print("total of odd no :",j)


        
