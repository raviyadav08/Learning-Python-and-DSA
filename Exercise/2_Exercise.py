"""
nyc_weather.csv contains new york city weather for 
first few days in the month of January. 
Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?
"""
import os
os.chdir("C:/Users/iamsu/Desktop/Python Codes/Data Structures and Algorithms/Exercise")

weather_dict = {}
with open("nyc_weather.csv",'r') as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temperature = float(tokens[1])
        weather_dict[day] = temperature
    print(weather_dict)

print(weather_dict['Jan 9'])
print(weather_dict['Jan 4'])

