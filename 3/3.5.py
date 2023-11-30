name = input("Enter the name: ")
date = input("Enter the date: ")

template = '''
dear <|name|>
u r selected
<|date|>
'''

print(template.replace('<|name|>', name).replace('<|date|>', date))