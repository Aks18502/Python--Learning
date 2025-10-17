b="Hi"

try:
    print(a)
except:
    print("error finds")


try :
    print(a)
except NameError:
    print("A is not define")
except:
    print("other else")

    
try:
    print(a)
except:
    print("something error")
else:
    print("nothing went wrong")


try:
    print(a)
except:
    print("eror")
finally:
    print("finished")


