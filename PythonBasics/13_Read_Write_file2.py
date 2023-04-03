"""
poem.txt contains famous poem "Road not taken" by poet Robert Frost.
You have to read this file in your python program and find out words with maximum
occurrence.
"""
word_stats = {}
with open('C:/Users/iamsu/Desktop/Python Codes/Data/poem.txt', 'r') as file:
    for line in file:
        tokens = line.split(" ")
        for word in tokens:
            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1

print(word_stats)

word_occurence = list(word_stats.values())
max_count = max(word_occurence)

print(f"Max occurrence of any word is : {max_count}")
print('')

for words,count in word_stats.items():
    if count == max_count:
        print(f'Word : {words}      Count:{count}')

