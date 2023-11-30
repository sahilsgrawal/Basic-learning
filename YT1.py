def CalUno(num):
    sum = 0
    while(num!=0):
        temp = num%10
        num = num//10
        sum =+ temp

    if sum>=0 and sum<=9:
        return sum
    else:
        return CalUno(sum)

if __name__ == '__main__':
    num = int(input())
    n = CalUno(num)
    print("Value of n: ", n)
    if n == 1:
        print("UNO")
    else:
        print("NOT UNO")

