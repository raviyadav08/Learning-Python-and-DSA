expenses = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(f'Difference in expense : {expenses[1]-expenses[0]}')


# 2. Find out your total expense in first quarter (first three months) of 
# the year.
print(f'Total expense in first quarters : {expenses[0]+expenses[1]+expenses[2]}')

# 3. Find out if you spent exactly 2000 dollars in any month
print(f'Spent exactly 2000 in any month? : {2000 in expenses}')

# 4. June month just finished and your expense is 1980 dollar. 
# Add this item to our monthly expense list
expenses.append(1980)
print(expenses)

'''
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
expenses[3] = expenses[3] - 200
print(expenses[3])



