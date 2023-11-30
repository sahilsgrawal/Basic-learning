with open("poems.txt", "r") as f:
    if('twinkle' in f.read()):
        print("Yes twinkle is present")
    else:
        print("the word twinkle is not present")