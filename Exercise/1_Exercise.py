"""
nyc_weather.csv contains new york city weather for first few days in the 
month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
"""

import os
os.chdir("C:/Users/iamsu/Desktop/Python Codes/Data Structures and Algorithms/Exercise")

weather = []
with open("nyc_weather.csv",'r') as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temp = float(tokens[1])
        weather.append(temp)
    print(weather)

avg_temp = round(sum(weather[0:7])/ len(weather[0:7]),2)
print(f"Average tempurature during the first week: {avg_temp}")
print(max(weather))
