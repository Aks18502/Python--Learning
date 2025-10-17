class aks:
    def __init__(self,name,age,place,food):
        self.name=name  
        self.age=age   
        self._place=place  
        self.food=food    
    def display(self):
        print(f"student name:{self.name}\n age:{self.age}\n place:{self._place}\n food:{self.food}")

stu=aks("Atchu",17,"myd","briyani")
print(stu.name,stu.age,stu._place,stu.food)
stu.display()
 