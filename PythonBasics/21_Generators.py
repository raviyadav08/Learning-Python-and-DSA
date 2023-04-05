"""
Create Generator method such that every time it will returns a 
next square number

for exmaple : 1 4 9 16 ..
"""

def square():
    i = 1
    while True:
        j = i
        square = 0
        square = j**2
        yield square
        i+=1

for i in square():
    if i > 100:
        break
    else:
        print(i)