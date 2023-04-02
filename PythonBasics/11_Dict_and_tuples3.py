"""Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and
returns area, circumference and diameter. You should get these values in your main program by calling circle_calc
function and then print them"""


def circle_calc(radius):
    pi = 3.14
    area = round(pi * (radius ** 2), 2)
    diameter = round(radius + radius, 2)
    circumference = round(2 * pi * radius, 2)
    return area, diameter, circumference


if __name__ == "__main__":
    user_input = float(input("Enter the radius of the circle : "))
    area, diameter, circumference = circle_calc(user_input)
    print(f"\nArea of Circle : {area} \nDiameter of Circle : {diameter} \nCircumference of Circle : {circumference}")

