import os
import csv
os.chdir('/Users/iamsu/Desktop/Demo/Data Structures/Hash Tables')


words_count = {}

with open('poem.txt','r') as file:
    for line in file:
        count = 0
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n',' ')
            if token in words_count:
                words_count[token]+= 1
            else:
                words_count[token]=1

print(words_count)


        
