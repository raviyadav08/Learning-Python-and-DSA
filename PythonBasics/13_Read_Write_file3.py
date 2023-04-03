"""
stocks.csv contains stock price, earnings per share and book value.
You are writing a stock market application that will process this file and create a new file with financial metrics
such as pe ratio and price to book ratio. These are calculated as,
"""

with open('C:/Users/iamsu/Desktop/Python Codes/Data/stocks.csv', 'r') as file, open('C:/Users/iamsu/Desktop/Python Codes/Data/Output.csv', 'w') as out:
    out.write("Company Name,PE Ratio,PB Ration\n")
    next(file)
    for line in file:
        tokens = line.split(',')
        stock = (tokens[0])
        price = float(tokens[1])
        share = float(tokens[2])
        value = float(tokens[3])
        pe = round(price/share,2)
        pb = round(price/value,2)
        out.write(f'{stock},{pe},{pb}\n')
