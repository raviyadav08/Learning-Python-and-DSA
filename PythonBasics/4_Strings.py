'''
1. Create 3 variables to store street, city and country, 
now create address variable to store entire address. 
Use two ways of creating this variable, one using + operator and 
the other using f-string. Now Print the address in such a way that the 
street, city and country prints in a separate line
'''
streetvar = 'Warje-411058'
cityvar = 'Pune'
countryvar = 'India'
# using + operator
print(streetvar +'\n'+ cityvar +'\n'+ countryvar)
# using f string
print(f' {streetvar} \n {cityvar} \n {countryvar}')

'''
2. Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index
'''
# string1 = 'Earth Revolves around the sun'
# print(string1[6:14])
# print(string1[-3:])

'''
3.Create two variables to store how many fruits and vegetables you eat in 
a day. Now Print "I eat x veggies and y fruits daily" where x and y 
presents vegetables and fruits that you eat everyday. 
Use python f string for this.
'''
x = 10
y = 20
print(f'I eat {x} veggies and {y} fruits daily')

'''
I have a string variable called s='maine 200 banana khaye'. 
This of course is a wrong statement, 
the correct statement is 'maine 10 samosa khaye'. 
Replace incorrect words in original strong with new ones and 
print the new string. Also try to do this in one line.
'''
# MY approach
s = 'maine 200 banana khaye'
print(f'{s[:5]} 10 samosa {s[-5:]}')

#another approach
s = s.replace('200','10').replace('banana','samosa')
print(s)



