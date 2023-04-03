# 1. After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

# 1. Using for loop figure out how many times you got heads
count = 0
for outcome in result:
    if outcome == 'heads':
        count += 1
    else:
        continue
print('Total no of times you got heads is : ', count)

# 2. Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i**2)


# 3. Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ['January', 'February', 'March', 'April', 'May']
month = -1
# Write a program that asks you to enter an expense amount and program should tell you
# in which month that expense occurred. If expense is not found then it should print that
# as well.

expense_input = int(input('Enter the expense amount that you need to find : '))
for i in range(len(expense_list)):
    if expense_input == expense_list[i]:
        month = i
        break
if month != -1:
    print(f'You spent {expense_input} in the month of {month_list[month]}')
"""
Let's say you are running a 5 km race. Write a program that,
Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
"""
distance = 1
while distance <= 5:
    print(f'You ran {distance-1} km')
    reply = str(input('Are you tired? : '))
    if reply == 'yes':
        print('You did not finish the race!')
        break
    distance += 1
else:
    print('You have completed the 5km race!!!')

"""
Write a program that prints following shape
*
**
***
****
*****
"""

times = int(input("How many rows of stars do you want? : "))
star = '*'
for i in range(times+1):
    for j in range(i):
        print(star,end='')
    print()






