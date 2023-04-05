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