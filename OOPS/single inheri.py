class student(food):
    def __init__(self,name,age,place,cake,chocolate,biskate,icecream):
        super().__init__(cake,chocolate,biskate,icecream)
        self.name=name
        self.age=age
        self.place=place
    def show(self):
        print(f"student name:{self.name}\n age:{self.age}\n place:{self.place}\n cake:{self.cake} \n chocolate:{self.chocolate}\n biskate:{self.biskate}\n icecream:{self.icecream} ")
stu1=student("kanishka",17,"myd","browni","kitkat","dark","stawbery")
print(stu1.name,stu1.age,stu1.place,stu1.cake,stu1.chocolate,stu1.biskate,stu1.icecream)
stu1.show()

class Kanish:
    def __init__(self, name, age, place, food):
        self.name = name
        self.age = age  
        self.place = place 
        self.food = food    

    def display(self):
        print(f"Student Name: {self.name}\nAge: {self.age}\nPlace: {self.place}\nFood: {self.food}") 
stu = Kanish("Kanishka", 17, "Myd", "Biryani")
print(stu.name, stu.age, stu.place,stu.food)
stu.display() 
