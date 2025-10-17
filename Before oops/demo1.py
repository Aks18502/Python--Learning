'''for i in range(1,10):
    if i==5:
        continue
    if i==7:
        break
    print(i)


i=0
while(i<=6):
    i+=1
    if i==5:
        continue
    print(i)'''


num = int(input("Enter a number: "))
factorial = 1

for i in range(1,num+1):
    factorial *= i

print(factorial)
