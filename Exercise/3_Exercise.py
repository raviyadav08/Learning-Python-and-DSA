"""
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count 
as show below. Think about the best data structure that you can use to 
solve this problem and figure out why you selected that specific data 
structure.
"""
import os
os.chdir("C:/Users/iamsu/Desktop/Python Codes/Data Structures and Algorithms/Exercise")

words = []
word_count = {}
count = 1
with open("poem.txt",'r') as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token.replace('\n', " ")
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1
    print(word_count)

w = list(word_count.values())
k = list(word_count.keys())

print(k[w.index(max(w))])




