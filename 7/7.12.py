n = int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*n-i):
        print("*", end="")
    for j in range(n-i):
        print(" ", end="")
    print("\n", end="")  
    