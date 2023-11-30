# a very basic sample class 
class Employee:
    center = "not known"
    def __init__(self, name, marks, center):
        self.name = name
        self.marks = marks
        self.center = center

    def printObj(self):
        print(f"the name is {self.name}")
        print(f"the marks is {self.marks}")
        print(f"the center is {self.center}")

    @staticmethod
    def greet():
        print("good day")

sahil = Employee("sahil", 34, "Delhi")
rohan = Employee("rohan", 34, "agra")
sahil.printObj()
rohan.printObj()