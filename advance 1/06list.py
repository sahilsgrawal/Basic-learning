a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# shortcut to write the same:

b = [i*i for i in a]

# b = [i for i in a if i%2==0]
print(b)

t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}

print(s)