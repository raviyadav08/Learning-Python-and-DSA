def check_arg(func):
    def inner(*args):
       for i in args:
            if i < 0:
                print("Negative integer entered")
                return
            elif not isinstance(i,int):
                print("Only integers have factorials")
                return
            return func(*args)
    return inner
       
    
@check_arg
def factorial(num):
    fact = 1
    if num == 0:
        print("Factorial of 0 is : ",fact)
    else: 
        for i in range(1,num+1):
            fact += fact * i
        print(fact)

factorial(5)
factorial(1.232)






            

