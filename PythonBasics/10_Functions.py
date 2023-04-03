"""
1. Write a function called calculate_area that takes base
and height as an input and returns and area of a triangle.
Equation of an area of a triangle is, area = (1/2)*base*height
"""


def area_of_triangle(base, height):
    return (1 / 2) * base * height


print(area_of_triangle(5, 10))

"""
2. Modify above function to take third parameter shape type.
It can be either "triangle" or "rectangle". Based on shape type
it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
"""


def area_of_objects(base, height, shape='triangle'):
    if shape == 'rectangle':
        return base * height

    elif shape == 'triangle':
        return (1 / 2) * base * height


rectangle = area_of_objects(5, 10, 'rectangle')
triangle = area_of_objects(5, 10, 'triangle')
object1 = area_of_objects(5, 10)

print(f'Area of rectangle = {rectangle}')
print(f'Area of triangle = {triangle}')
print(f'Default Area of triangle = {object1}')

"""
3. Write a function called print_pattern that takes integer number as an 
argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print
*
**
***
****
"""


def print_pattern(number_of_rows):
    for i in range(0, number_of_rows + 1):
        for j in range(0, i):
            print('*', end='')
        print('')


numbers_of_rows = int(input('Enter the amount of star rows you need : '))
print_pattern(numbers_of_rows)
