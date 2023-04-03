india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]


def finding_country(city1):
    if city1 in india:
        print('This city is present in India')
    elif city1 in pakistan:
        print('This city is present in pakistan')
    elif city1 in bangladesh:
        print('This city is present in bangladesh')
    else:
        print('I do not know which country this city is in.')


def two_cities(city1, city2):
    if city1 in india and city2 in india:
        print('Both cities are in India')
    elif city1 in pakistan and city2 in pakistan:
        print('Both cities are in Pakistan')
    elif city1 in bangladesh and city2 in bangladesh:
        print('Both cities are in Bangladesh')
    else:
        print('They dont belong to the same country')


# 1. Write a program that asks user to enter a city name and
# it should tell which country the city belongs to
city1 = str(input('Enter first city name: '))
city2 = str(input('Enter second city name: '))
finding_country(city1)
'''
2. Write a program that asks user to enter two cities and it tells you 
if they both are in same country or not. For example if I enter mumbai 
and chennai, it will print "Both cities are in India" but if I enter 
mumbai and dhaka it should print "They don't belong to same country"
'''
two_cities(city1, city2)
