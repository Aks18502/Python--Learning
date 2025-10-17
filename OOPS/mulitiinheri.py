class A:
    def a(self):
        print("A is there")
class B:
    def b(self):
        print("B is there")
c=[A(),B()]
print(c.a,c.b)