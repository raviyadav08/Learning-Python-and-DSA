x = input('Enter x number: ')
y = input("Enter y number:")

"""
The try block lets you test a block of code for errors. 
The except block lets you handle the error. 
The else block lets you execute code when there is no error. 
The finally block lets you execute code, regardless of the result 
of the try- and except blocks.
"""
try:
    z = int(x)/int(y)
    """
    Exception code block is written where you think the error
    is most probably gonna rise.
    """
except ZeroDivisionError as e:
    print("You tried to divide a number by 0!!!")
    z = None

except Exception as e:
    """
    We use type to know what type of exception has arised
    or we could just focus on what exception most probably is gonna
    arise and can singly focus on handling that exception
    for example Zero division error.
    """
    print("Exception: ", type(e))
    z = None
else:
    print("Division of 2 number is : ", z)
finally:
    print("The division process has ended!!!")