oxford = {
    "lakdi": "wood",
    "kursi": "chair",
    "paani": "water"
}
key = input("enter the key\n")
if(oxford.get(key)== None):
    print("value not found")
else:
    print("the value corresponding to your key is: ", oxford.get(key))

