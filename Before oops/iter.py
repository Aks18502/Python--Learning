#iterators
'''a=("apple")
b=iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#generators
def number():
    a='atchaya'
    for i in a:
        yield i
num=number()
for x in num:
    print(x)

#closure
def a(x):
    def b():
        print(f"Value of a is : {x}")
    return b
closure=a(10)
closure()'''


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)
