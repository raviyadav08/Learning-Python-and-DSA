# Program to Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

odd_num = []

max_num = int(input('Enter The Max Number to get odd number --> '))

for i in range(1, max_num+1):
    if(i%2 == 1):
        odd_num.append(i)

print('Odd Numbers : ',odd_num)