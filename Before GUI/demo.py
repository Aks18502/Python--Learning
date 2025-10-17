#closure
'''def outer(a):
    def inner(b):
        print(a-b)
    return inner

ab=outer(5)
ab(11)
ab(13)'''

#decorator
def aks():
    print("Hi Aks")
h=aks
h()