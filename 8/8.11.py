def process(l, word):
    word = word.strip()
    if word in l:
        l.remove(word)
    return l1

l1 = ['sahil', 'rohan', 'ram', 'shubh', 'deep']
l1 = process(l1, 'sahil')
print(l1) 