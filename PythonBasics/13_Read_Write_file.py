# with open('C:/Users/iamsu/Desktop/Python Codes/Data/funny.txt', 'a') as rf:
#     rf.write("\nI love PHP")
import csv

with open('C:/Users/iamsu/Desktop/Python Codes/Data/funny.txt', 'r') as file:
    for line in file:
        count = 0
        tokens = line.split(" ")
        with open('C:/Users/iamsu/Desktop/Python Codes/Data/funny1.txt', 'a') as new_file:
            new_file.write(" Word Count: "+ str(len(tokens))+'\t'+line)
