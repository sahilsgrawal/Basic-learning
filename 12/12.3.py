# a very basic sample class 
class Employee:
    name = "Sahil" #a class attribute
    marks = 34
    center = "delhi"

    def printObj(self):
        print(f"the name is {self.name}")
        

    @staticmethod
    def greet():
        print("good day")

Employee.name = "Sahilnew" #setting a class attribute for employee
sahil = Employee() # A basic object
shyam = Employee() #a basic object
print(sahil.name)
print(shyam.name)
shyam.name = "Shyam" # setting an instance attribute to shyam
print(shyam.name)
print(sahil.name)
sahil.greet()
Employee.greet()