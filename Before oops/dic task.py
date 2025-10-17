list=[]
n=int(input("How number of details:"))
for i in range(1,n+1):
    print("Enter the ",i," details")
    name=input("Enter the name:")
    age=int(input("Enter the age:"))
    place=input("Enter the place:")
    dic={"name":name,"age":age,"place":place}
    list.append(dic)
print(list)
