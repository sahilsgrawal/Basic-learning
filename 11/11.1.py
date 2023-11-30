# import random

# number = random.randint(1, 100)
# attempt = 1
# guess = int(input("guess the number: "))

# while(True):
#     if(guess>number):
#         guess = int(input("guess another number. this one is too big: "))
#         attempt +=1
#     elif(guess<number):
#         guess = int(input("guess another number. this one is too less: "))
#         attempt +=1

#     else:
#         print(f"yeah thats the number! you guessed it right in {attempt} attempts")
#         break

import random

number = random.randint(1,100)
att = 1
guess = int(input("guess the number: "))

while(True):
    if(guess>number):
        guess = int(input("guess another number, as this one is too big: "))
        att +=1
    elif(guess<number):
        guess = int(input("guess another number, as this one is too small: "))
        att +=1
    else:
        print(f"Yeah thats the number! You guessed it right in {att} attempts")
        break