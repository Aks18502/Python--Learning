from abc import ABC,abstractmethod
class school(ABC):
    def __init__(self, name, location, students):
        self.name = name
        self.location = location
        self._students = students
    @abstractmethod
    def display(self):
        print(f"School Name: {self.name}\nLocation: {self.location}\nStudents: {self._students}")
class course(school):
    def __init__(self, name, location, students, course_name, duration):
        super().__init__(name, location, students)
        self.course_name = course_name
        self.duration = duration
    def dispay(self):
        super().dispay()
        print(f"Hii {self.name} this Course Name is: {self.course_name}\nDuration: {self.duration}")
stu=course("Aks","myd",123445,"Python","6 months")
stu.display()