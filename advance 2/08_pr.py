from functools import reduce

def max(m, n):
    if m>n:
        return m
    return n


a = [1,2,3,54,675,34]

maxNum = reduce(max, a)

print(maxNum)