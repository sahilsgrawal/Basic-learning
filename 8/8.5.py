'''
factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    #base condition
    if(n ==0 or n ==1):
        return 1
    return n * factorial(n - 1)

a = factorial(10)  
print(a)  