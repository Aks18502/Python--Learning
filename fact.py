a=int(input())
fact=1
while a>0:
    n=a%10
    fact=fact*n
    a=a//10
print(fact)
