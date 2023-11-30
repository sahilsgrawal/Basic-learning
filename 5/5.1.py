oxford = {
    "gift": "something willingly given to someone to appreciate",
    "this": "a keyword in c++",
    "youtube": "a video sharing platform",
    "instagram": "a picture sharig platform",
    "mylist": [1, 3, 45],
}

oxford.update({"sahil":"good boy", "mylist": [56, 8]})
# print(oxford)
print(oxford.items())
for a, b in oxford.items():
    print(a,"=", b)

for key in oxford.keys():
    print(key)

