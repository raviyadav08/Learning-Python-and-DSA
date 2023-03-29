import os
import csv
os.chdir('/Users/iamsu/Desktop/Demo/Data Structures/Hash Tables')

weather = {}
with open('nyc_weather.csv','r') as file:
    for line in file:
        tokens = line.split(',')
        day = tokens[0]
        try:    
            temperature = int(tokens[1])
            weather[day] = temperature
        except:
            print('Invalid Temperature')    

# print(weather)
print(weather['Jan 9'])
print(weather['Jan 4'])



