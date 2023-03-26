#Months from Jan to May in order from 0th to 4th
expense = [2200,2350,2600,2130,2190]


print('\n \n \n-------------------------------------------------------------------')
# 1. Finding the Difference of expenditure in month of Jan and Feb.
if(expense[0] > expense[1]):
    diff = expense[0] - expense[1]
    print(f'Spent More money in JAN by -->{diff} Rs')
else:
    diff = expense[1] - expense[0]
    print(f'Extra money spent in FEB comapred to JAN --> {diff}Rs')

# 2. Finding quarters expenditure in first 3 months of year
quarter_expense = expense[0] + expense[1] + expense[2]
print(f'Expense generated in this quarter is --> {quarter_expense}Rs')

# 3. Finding out if you spent exactly 2000 dollar in any month
for amount in expense:
    if amount == 2000:
        print(f'Index of Month where we spent 2000Rs --> {expense.index(2000)}')
        break
else:
    print('Did not spend exactly 2000Rs in any month ')

'''
4. June month just finished and your expense is 1980 dollar.
Add this item to our monthly expense list 
'''
expense.insert(5,1980)
print(f'Expense in month of Jun --> {expense} Rs')

'''
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
expense[3] = expense[3] - 200
print(f'After adding the returned amount expenditure of april --> {expense} Rs')


print('-------------------------------------------------------------------')
print('\n\n\n')