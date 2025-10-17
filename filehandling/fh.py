#open("at.txt","x")
file = open("at.txt", "a")
a=input("enter the email:")
b=input("enter the password:")
c=int(input("enter the option:"))
if c==1:
    print(a)
elif(c==2):
    print(b)
else:
    print("invalid option")
file.write(a+"\n"+b+"\n")
file.close()
