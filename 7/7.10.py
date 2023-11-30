# num = 6
num = int(input("enter any number: "))
for i in range(2, num):
    if (num%i == 0):
        print("not prime")
        break
else:
     print("this is prime")   