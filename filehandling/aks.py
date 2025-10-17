#open("akshay.txt","x")
file=open("akshay.txt","a")
a=input("Enter ur name:")
b=int(input("Enter ur age:"))
c=input("Enter ur place:")
file.write("\n"+a+"\t"+str(b)+"\t"+c)
file.close()

'''file=open("akshay.txt","r")
a=file.read().split("\n")
print(a)
for i in a:
    i=i.split("\t")
    print(i)'''
