import json

with open('C:/Users/iamsu/Desktop/Python Codes/Data/books.txt','r') as rf:
    s = rf.read()
    print(type(s))
    print(s)

book = json.loads(s)
print(book)
print(type(book))

print(book['bob'])
print(book['bob']['phone'])

for person in book:
    print(book[person])


