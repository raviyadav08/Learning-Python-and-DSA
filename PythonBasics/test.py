
with open('C:/Users/iamsu/Desktop/Python Codes/Data/stocks.csv', 'r') as file, open('C:/Users/iamsu/Desktop/Python Codes/Data/output1.csv','w') as out:
    out.write("Company Name,PE Ratio,PB Ratio\n")
    next(file)
    for line in file:
        tokens = line.split(',')
        stocks = tokens[0]
        price = float(tokens[1])
        share = float(tokens[2])
        value = float(tokens[3])
        pe = round(price/share,2)
        pb = round(price/value,2)
        out.write(f'{stocks},{pe},{pb}\n')


