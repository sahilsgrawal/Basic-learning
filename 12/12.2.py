# a very basic sample class 
class Employee:
    name = "Sahil"
    marks = 34
    center = "delhi"

    def printObj(self):
        print(f"the name is {self.name}")

sahil = Employee() # A basic object
print(sahil.marks)
print(sahil.center)
print(sahil.name)
sahil.printObj() #employee.printObj(sahil)
Employee.printObj(sahil)