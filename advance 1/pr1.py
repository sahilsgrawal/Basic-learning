# def readFile(filename):
#     try:
#         with open(filename, "r") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"file {filename} is not found")

# readFile("1.txt")
# readFile("2.txt")
# readFile("3.txt")

try:
    with open('1.txt', 'r') as f:
        f.read()
    with open('2.txt', 'r') as f:
        f.read()
    with open('3.txt', 'r') as f:
        f.read()

except Exception as e:
    print(f"The file is not present. Reason: {e}")

print("Thanks for using this program")