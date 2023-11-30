# def mean(mylist):
#     print("Function started!")
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# mymean = mean([1 , 2 , 3])
# print(mymean + 10)


#2
# def mean(value):
#     if type(value) == dict:
#         the_mean = sum(value.values()) / len(value)
#     else:
#         the_mean = sum(value) / len(value)

#     return the_mean

# temp = [8.8 , 9.1 , 9.4]
# grades = {"Sahil" : 10 , "saurabh" : 8.9 , "Ankit" : 9}

# print(mean(temp))

#3

# # name = input("Enter your name: ")
# # surname = input("Enter your surname: ")

# # message = "hello %s %s" % (name , surname)

# # print(message)


# def sentence_maker(phrase):
#     interrogatives = ("how" , "what" , "why")
#     capitalize = phrase.capitalize()
#     if phrase.startswith(interrogatives):
#         return "{}?".format(capitalize)
#     else:
#         return "{}.".format(capitalize)

# result = []
# while True:
#     user_input = input("Say something: ")
#     if user_input == "\end":
#         break
#     else:
#         result.append(sentence_maker(user_input))

# print(" ".join(result))


import time
import os

while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())

    else:
        print("Files does not exist.")
    
    time.sleep(10)