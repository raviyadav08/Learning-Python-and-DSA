import csv

book = {}
book['tom'] = {
    'name' : 'tom',
    'address' : '1 red street, NY',
    'phone' : 98989898
}
book['bob'] = {
    'name' : 'bob',
    'address' : '1 green street, NY',
    'phone' : 23232323
}

import json
conv_to_json = json.dumps(book)
# print(conv_to_json)

with open('C:/Users/iamsu/Desktop/Python Codes/Data/books.txt','w') as bookfile:
    bookfile.write(conv_to_json)
