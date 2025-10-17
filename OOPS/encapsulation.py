class aks:
    def __init__(self,name,age):
        self.__name=name
        self.age=age
    def gettername(self):
        return self.__name
    def settername(self,name):
        self.__name=name
ak=aks("Aksh",23)
print(ak.gettername())
ak.settername("akshaya")
print(ak.gettername())