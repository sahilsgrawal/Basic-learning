class Employee:
    a = 34


class Programmer(Employee):
    b = 31

pr = Programmer()
print(pr.a)
print(pr.b)

em = Employee()
print(em.a)
# print(em.b) #error line