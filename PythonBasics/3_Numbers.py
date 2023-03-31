'''
1. You have a football field that is 92 meter long and 48.8 meter wide. 
Find out total area using python and print it.
'''
fieldLength = 92
fieldBreadth = 48.8
fieldArea = fieldLength * fieldBreadth
roundedfieldArea = round(fieldArea,1)
print(f'1. Total area of football field is {roundedfieldArea}')

'''
2. You bought 9 packets of potato chips from a store. 
Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
Find out, how many dollars is the shopkeeper going to give you back?
'''
totalpackets = 9
packetcost = 1.49
totalamount = 20
amountReturned = totalamount - (totalpackets * packetcost)
roundedAmountReturned = round(amountReturned,2)
print(f'2. Amount Returned : {roundedAmountReturned}')

'''
3. You want to replace tiles in your bathroom which is exactly square 
and 5.5 feet is its length. If tiles cost 500 rs per square feet, 
how much will be the total cost to replace all tiles. 
Calculate and print the cost using python
(Hint: Use power operator ** to find area of a square)
'''
squarelength = 5.5
areaofSquare = squarelength ** 2
totalcost = areaofSquare * 500
print(f'3. Total cost of tilling would be : {totalcost}')

'''
4. Print binary representation of number 17
'''
num = format(17,'b')
print(f'4. Binary of number 17 is : {num}')
