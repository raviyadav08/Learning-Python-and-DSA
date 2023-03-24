flag = int(input('Enter 1 to perform an operation and 0 to end the program : '))

while flag == 1 :
    print('---------------------------------------CALCULATOR------------------------------------------------------------------------')
    print(' 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division')
    print('-------------------------------------------------------------------------------------------------------------------------')
    operation_num = int(input('\n Enter a number to perform a arithmetic operation : '))

    if (operation_num == 1):
        num1 = int(input('\n Enter first number to perform a arithmetic operation : '))
        num2 = int(input('\n Enter second number to perform a arithmetic operation : '))
        result =  num1 + num2
        print(f'\n Addition of 2 number is = {result}')

    elif(operation_num == 2):
        num1 = int(input('\n Enter first number to perform a arithmetic operation : '))
        num2 = int(input('\n Enter second number to perform a arithmetic operation : '))
        result =  num1 - num2
        print(f'\n Substraction of 2 number is = {result}')

    elif(operation_num == 3):
        num1 = int(input('\n Enter first number to perform a arithmetic operation : '))
        num2 = int(input('\n Enter second number to perform a arithmetic operation : '))
        result =  num1 * num2
        print(f'\n Multiplication of 2 number is = {result}')

    elif(operation_num == 4):
        num1 = int(input('\n Enter first number to perform a arithmetic operation : '))
        num2 = int(input('\n Enter second number to perform a arithmetic operation : '))
        result =  num1 / num2
        print(f'\n Division of 2 number is = {result}')
    else:
        print('\n Enter a valid operation Number.......')

    flag = int(input('\n Enter 1 to perform an operation and 0 to end the program : '))
    
    
    



