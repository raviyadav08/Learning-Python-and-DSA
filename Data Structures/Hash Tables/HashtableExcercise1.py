import os
import csv
os.chdir('/Users/iamsu/Desktop/Demo/Data Structures/Hash Tables')

def avg_temp():
    avg = sum(weather[0:7])/len(weather[0:7])
    return avg

def max_temp():
    maxtemp = max(weather[0:10])
    return maxtemp

weather = []
with open('nyc_weather.csv','r') as file:
    for line in file:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            weather.append(temperature)
        except:
            print('Invalid Temperature. Ignore the row')
    

print(weather)
print(avg_temp())
print(max_temp())
    



