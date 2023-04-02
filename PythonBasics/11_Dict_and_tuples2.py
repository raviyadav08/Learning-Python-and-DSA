"""
You are given following list of stocks and their prices in last 3 days,
Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]

Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33

add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc)
then it will append the price to the list. Otherwise it will create new entry in your dictionary.
For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
"""

stock_prices = {'info': [600, 630, 620], 'ril': [1430, 1490, 1567], 'mtl':[234, 180, 160]}

while exit:
    print('\nCommands:')
    print("Enter 'print' to print the stock prices.")
    print("Enter 'add' to add  a stock and their prices.")
    print("Enter 'exit' to exit the program.")
    input_operation = str(input('\nEnter the operation you want to perform : '))

    if input_operation == 'exit':
        exit()

    elif input_operation == 'print':
        for key, value in stock_prices.items():

            avg_price = round(sum(value) / len(value), 2)
            print(f'{key} ==> {value} ==> avg : {avg_price}')

    elif input_operation == 'add':
        input_stock_name = str(input('Enter the name of stock that you want to enter : '))
        input_stock_price = float(input('Enter the price of the stock : '))

        if input_stock_name in stock_prices:
            stock_prices[input_stock_name] += [input_stock_price]
        else:
            stock_prices[input_stock_name] = [input_stock_price]


